from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup
from transformers import pipeline
from deep_translator import GoogleTranslator, exceptions
import time

app = Flask(__name__)

# Load the summarization model
summarizer = pipeline("summarization")

def scrape_website(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 403:
        return "Access denied: 403 Forbidden error."
    
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text(separator=' ', strip=True)
    return text

def translate_text(text):
    translated_chunks = []
    max_chunk_length = 500  # Adjust as necessary
    chunks = [text[i:i + max_chunk_length] for i in range(0, len(text), max_chunk_length)]
    
    for chunk in chunks:
        attempts = 3  # Number of attempts
        for attempt in range(attempts):
            try:
                translated = GoogleTranslator(source='auto', target='en').translate(chunk)
                translated_chunks.append(translated)
                break  # Exit loop on success
            except exceptions.RequestError:
                if attempt < attempts - 1:  # If not the last attempt
                    time.sleep(1)  # Wait before retrying
                else:
                    print("Translation failed after multiple attempts.")
                    translated_chunks.append(chunk)  # Append original text

    return " ".join(translated_chunks)

def summarize_text(text):
    max_chunk_length = 1000
    chunks = [text[i:i + max_chunk_length] for i in range(0, len(text), max_chunk_length)]
    
    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=150, min_length=30, do_sample=False)
        summaries.append(summary[0]['summary_text'])
    
    return " ".join(summaries)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    url = request.form['url']
    website_text = scrape_website(url)
    
    translated_text = translate_text(website_text)
    summary = summarize_text(translated_text)
    
    return render_template('result.html', processed_text=website_text, summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
