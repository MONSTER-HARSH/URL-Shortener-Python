# URL Shortener

A simple URL shortener built using Flask and SQLite.

## Features
- Shortens long URLs into unique hash-based short links.
- Stores URLs in an SQLite database.
- Redirects users to the original URL when they access the shortened link.

## Prerequisites
- Python 3.12 installed
- Flask installed via Pipenv (`pip install pipenv`)

## Installation

Clone this repository and navigate into the project directory:
```sh
git clone https://github.com/MONSTER-HARSH/URL-Shortener-Python.git
cd url-shortener
```

### Setting up the environment
Create and activate a virtual environment using Pipenv:
```sh
pipenv install
pipenv shell
```

### Setting up the database
Initialize the SQLite database by running:
```sh
python3 init_db.py
```
This will create `database.db` using the schema defined in `schema.sql`.

### Running the Application
Start the Flask application by running:
```sh
python3 app.py
```
The application will be available at `http://127.0.0.1:5000/`.

## Project Structure
```
URL-Shortener-Python/
│── app.py         # Main Flask application
│── init_db.py     # Initializes the SQLite database
│── schema.sql     # Database schema
│── Pipfile        # Dependency management with Pipenv
│── templates/
│   └── index.html # HTML template for the web interface
│── README.md      # Project documentation
```

## Usage
1. Open `http://127.0.0.1:5000/` in your browser.
2. Enter a full URL and select a hash range (between 5 and 10).
3. Click **Shorten URL**.
4. Copy the generated short URL and use it to redirect to the original URL.

## Security Considerations
- **Sanitization**: Ensure user inputs are properly validated to prevent SQL injection.
- **Error Handling**: Implement better error handling to inform users of incorrect inputs.

## License
This project is open-source under the MIT License.
