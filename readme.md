# Multilingual Web Summarizer

This web application allows users to input a URL, scrape its content, translate it to English (if necessary), and summarize it using a pre-trained model.

## Features

- Scrapes text content from a given website.
- Translates non-English content to English.
- Summarizes the content using the BART summarization model.

## Installation

1. Clone the repository or download the files.
2. Navigate to the project directory.
3. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```
5. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```bash
    python app.py
    ```
2. Open a web browser and navigate to `http://127.0.0.1:5000/`.
3. Enter the URL of the website you want to summarize and click "Summarize".

## Files

- `app.py`: Main application file containing the Flask app and core logic.
- `index.html`: Input form for entering the website URL.
- `result.html`: Displays the processed content and the summary.

## License

This project is licensed under the MIT License.
