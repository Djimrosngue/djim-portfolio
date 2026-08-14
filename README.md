# Django Developer Portfolio

> A modern, responsive and bilingual developer portfolio built with Django.

## Overview

This project is my personal developer portfolio, designed to present my technical skills, professional profile, services and software projects through a clean and responsive web interface.

The application is built with Django and includes bilingual support, a dynamic project management system, an administration dashboard and production-ready deployment configuration.

---

## Features

- 🌍 French / English bilingual interface
- 👤 Personal profile and professional information
- 💼 Projects portfolio
- 🛠️ Technical skills management
- 📋 Services presentation
- 🔐 Secure Django authentication
- 📊 Administration dashboard
- 🌐 REST API support
- 🗄️ SQLite for local development
- 🐘 PostgreSQL for production
- 🚀 Render deployment support
- ⚡ WhiteNoise for static files
- 📱 Responsive design
- 🔒 Production security configuration

---

## Tech Stack

### Backend

- Python
- Django
- Django REST Framework
- PostgreSQL
- SQLite
- django-modeltranslation

### Frontend

- HTML5
- CSS3
- JavaScript
- Django Templates

### Deployment

- Render
- WhiteNoise
- PostgreSQL

### Development Tools

- Git
- GitHub
- Visual Studio Code


Local Installation

1. Clone the repository

git clone https://github.com/Djimrosngue/djim-portfolio.git

cd djim-portfolio 

2. Create a virtual environment
   
Windows:
python -m venv venv
venv\Scripts\activate

Linux / macOS:
python3 -m venv venv
source venv/bin/activate

3.Install dependencies
   
pip install -r requirements.txt

4. Configure environment variables
   
Create a .env file from .env.example.
Example:
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DATABASE_URL=
RENDER_EXTERNAL_HOSTNAME=
CUSTOM_DOMAIN=

5. Apply migrations
    
python manage.py migrate

6. Create an administrator
    
python manage.py createsuperuser

7. Collect static files
    
python manage.py collectstatic

8. Run the development server
    
python manage.py runserver
The application will be available at:
http://127.0.0.1:8000/

Database

The project automatically uses:

Development

SQLite when DATABASE_URL is not configured.

Production

PostgreSQL when DATABASE_URL is provided.
This allows the same project to work locally and in production without changing the source code.

Internationalization

The portfolio supports:

🇫🇷 French

🇬🇧 English

Language management is implemented using Django internationalization and django-modeltranslation.
French is the default language.

Security

Production security settings include:
HTTPS redirection
Secure session cookies
Secure CSRF cookies
HSTS
X-Frame-Options
Content-type protection
Environment-based secret management
Sensitive configuration is stored outside the source code using environment variables.

Deployment

The project is configured for deployment on Render.

Production uses:
Django
PostgreSQL
WhiteNoise
Environment variables
Gunicorn
Before deployment, configure the required environment variables in the Render dashboard.

Future Improvements

Planned improvements may include:

📧 Production email service

📈 Portfolio analytics

🔎 Advanced project filtering

📝 Blog section

📬 Contact form improvements

🌐 Custom domain

🧪 Automated testing

🔄 CI/CD with GitHub Actions

Author

Djimrosngue Ngarhodjim Justin

Python / Django Developer
Interested in:
Web Development
IoT
Mobile Development
Software Engineering
Data & Business Intelligence

Contact

For professional opportunities, collaborations or technical projects, feel free to connect with me through my professional profiles.

License
This project is available for educational and portfolio purposes.
Please contact the author before reusing significant parts of the source code or design.
