# Django PDF to Markdown Converter

A web application built with Django that allows users to upload PDF files and instantly convert them into Markdown (`.md`) format using the `pymupdf4llm` library. The app features a beautiful, responsive user interface styled with Bootstrap 5.

## Features

- **User Authentication**: Secure login system for users to manage their personal conversions.
- **PDF Uploads**: Easy-to-use drag-and-drop interface for uploading PDF documents.
- **Instant Conversion**: High-quality conversion from PDF to Markdown using `pymupdf4llm`.
- **File Management**: View past conversions, download original PDFs or generated Markdown files, and securely delete records.
- **Local Storage**: Files are saved securely to the local `media` directory, keeping the SQLite database fast and lightweight.
- **Preview & Copy**: Built-in Markdown previewer with a convenient "Copy to Clipboard" feature.

## Requirements

- Python 3.10+
- See `requirements.txt` for specific Python dependencies.

## Installation

1. **Clone the repository or download the source code:**
   ```bash
   git clone <repository-url>
   cd Djangopdftomd
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   A `.env.example` file is included as a template. Follow these steps:

   **Step 1 — Copy the example file:**
   ```bash
   # Windows
   copy .env.example .env

   # macOS/Linux
   cp .env.example .env
   ```

   **Step 2 — Generate your own Django secret key:**
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```
   This prints a unique secret key. Copy the output.

   **Step 3 — Paste it into your `.env` file:**
   ```env
   SECRET_KEY = "paste-your-generated-key-here"
   DEBUG = True
   ```

   | Variable     | Description                                                                   | Example Value          |
   |--------------|-------------------------------------------------------------------------------|------------------------|
   | `SECRET_KEY` | Django's cryptographic secret key. **Keep this private and never commit it.** | `django-insecure-xxxx` |
   | `DEBUG`      | Enables Django debug mode. Set to `False` in production.                      | `True` / `False`       |

   > **Important:** The `.env` file is listed in `.gitignore` and will **not** be committed to version control.
   > Every developer and every deployment should have their **own unique** `SECRET_KEY`.

5. **Run Database Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser (Optional, but recommended):**
   ```bash
   python manage.py createsuperuser
   ```

## Running the Application

1. **Start the Django development server:**
   ```bash
   python manage.py runserver
   ```

2. **Access the web interface:**
   Open your browser and navigate to `http://127.0.0.1:8000/`.

## Default Credentials

If you set up the default superuser during the initial setup via the automated script, you can log in with:
- **Username:** `admin`
- **Password:** `admin123`

## Directory Structure

- `pdf2md_project/` - Main Django project configuration settings.
- `converter/` - The core Django app handling models, views, and routing.
- `templates/` - HTML templates structured with Bootstrap 5.
- `static/` - Contains custom CSS and other static assets.
- `media/` - (Created dynamically) Stores uploaded PDFs and converted `.md` files.

## Developed By

[Nascenture](https://www.nascenture.com/) — a software development company specializing in innovative digital solutions.

