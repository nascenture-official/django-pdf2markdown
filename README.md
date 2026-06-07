# Django PDF to Markdown Converter

A web application built with Django that allows users to upload PDF files and instantly convert them into Markdown (`.md`) format using the `pymupdf4llm` library. The application features a clean, responsive interface built with Bootstrap 5 and includes user authentication, file management, and Markdown preview functionality.

## Features

- User authentication and account management
- PDF upload and conversion to Markdown
- High-quality conversion powered by `pymupdf4llm`
- Conversion history and file management
- Download original PDFs and generated Markdown files
- Secure record deletion
- Local file storage for improved performance
- Markdown preview and copy-to-clipboard functionality
- Responsive Bootstrap 5 interface

## Requirements

- Python 3.10+
- Django 5+
- See `requirements.txt` for the complete list of dependencies

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Djangopdftomd
```

### 2. Create and Activate a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy the example environment file:

**Windows**

```bash
copy .env.example .env
```

**macOS/Linux**

```bash
cp .env.example .env
```

Generate a Django secret key:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Add the generated key to your `.env` file:

```env
SECRET_KEY="your-generated-secret-key"
DEBUG=True
```

| Variable | Description |
|-----------|------------|
| SECRET_KEY | Django's secret key. Keep this private and never commit it to version control. |
| DEBUG | Enable or disable Django debug mode. Use `False` in production environments. |

> The `.env` file is excluded from version control and should remain private.

### 5. Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create an Administrator Account

```bash
python manage.py createsuperuser
```

Follow the prompts to create your administrator account.

## Running the Application

Start the development server:

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## Directory Structure

```text
pdf2md_project/   Main Django project configuration
converter/        Core application logic
templates/        HTML templates
static/           CSS, JavaScript, and static assets
media/            Uploaded PDFs and generated Markdown files
```

## Example Use Cases

- Knowledge base migration
- Content management systems
- AI and LLM document processing
- Internal documentation workflows
- PDF content extraction pipelines
- Research document processing
- Content archiving and migration
- Document digitization projects

## Why Use Django PDF2Markdown?

Many organizations store valuable information in PDF documents. Converting this content into Markdown makes it easier to search, edit, organize, and integrate with modern applications.

Django PDF2Markdown provides a simple and efficient solution for developers who need PDF-to-Markdown conversion capabilities within Django-powered systems.

## Tech Stack

- Django
- Python
- Bootstrap 5
- SQLite
- PyMuPDF
- pymupdf4llm

## Contributing

Contributions, bug reports, and feature requests are welcome.

To contribute:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

## License

This project is released under the MIT License.

## About the Maintainer

This project is maintained by Nascenture, a software development company specializing in Django development, custom software solutions, web applications, and cloud-based platforms.

- Django Development Services: https://www.nascenture.com/django-development/
- Company Website: https://www.nascenture.com/
