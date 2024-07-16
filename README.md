# Translator

This project is a simple web-based text translation application. It allows users to translate text from one language to another using a web interface.

## Project Structure

- `translate_api.py`: This is the main backend file that contains the Flask application and handles the translation requests.
- `main.html`: This is the frontend file that provides the user interface for the translation application.
- `styles.css`: This file contains the styles for the frontend (not shown in the provided context).

## Endpoints

### POST /translate

This endpoint translates the provided text to the specified destination language.

**Request:**
- Method: `POST`
- Content-Type: `application/json`
- Body:
  ```json
  {
    "text": "Text to be translated",
    "dest_lang": "Destination language code"
  }
  ```

**Response:**
- Success: `200 OK`
  ```json
  {
    "original_text": "Text to be translated",
    "translated_text": "Translated text",
    "dest_lang": "Destination language code"
  }
  ```
- Error: `400 Bad Request`
  ```json
  {
    "error": "Please provide 'text' and 'dest_lang' fields."
  }
  ```

### GET /translate

This endpoint serves the main HTML file for the translation application.

**Request:**
- Method: `GET`

**Response:**
- Success: `200 OK`
  - Content-Type: `text/html`
  - Body: `main.html` content

### GET /translate_version

This endpoint returns the version of the translation library being used.

**Request:**
- Method: `GET`

**Response:**
- Success: `200 OK`
  ```json
  {
    "version": "version_number"
  }
  ```

## How to Run

1. Ensure you have Python and Flask installed.
2. Install the `translate` library.
3. Run the Flask application:
   ```bash
   python translate_api.py
   ```
4. Open your web browser and navigate to `http://127.0.0.1:5000/translate` to access the translation application.

## Usage

1. Enter the text you want to translate in the "Type your text" input field.
2. Enter the destination language code in the "Type your destination language" input field.
3. Click the "Translate" button to get the translated text.

## Example

- Original Text: "Hello"
- Destination Language: "es" (Spanish)
- Translated Text: "Hola"
