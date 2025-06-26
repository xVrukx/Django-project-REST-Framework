# Django Backend Assignment by Kanhaiyalal Bohra🚀

This is a Django REST Framework-based backend system with:

- ✅ Token & Web-based Authentication
- ✅ Celery + Redis for async email sending
- ✅ Telegram Bot Integration
- ✅ Clean code with inline comments
- ✅ Bootstrap Dark UI for Web Pages

---

## 🔧 Features

- **Register/Login** (via Web and API)
- **Public & Protected API endpoints**
- **Welcome email** after registration via Celery
- **Telegram Bot** that stores usernames on /start

---

## 🛠 Setup Instructions

```bash
git clone https://github.com/xVrukx/Django-project-REST-Framework.git
cd your-repo-name

# Create virtualenv
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# How to run locally (terminal one)
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

# How to start celery
  # (Terminal 2)
  redis-server.exe --port 6380
  # (Terminal 3)
  celery -A body worker --loglevel = info --pool = solo

#How to run telegram bot (Terminal 4)
python Telegram_bot.py

# API End points in detail

Method |	Endpoint	|   Description	             |    Auth Required
GET	   |    /public/	|   Public view	             |          ❌
GET	   |   /private/	|   Private view (DRF token) |       	✅
POST   |  /api/register/|	API user registration	 |          ❌
POST   | /api/login/	|   API token login	         |          ❌

# Folder structure

project/
├── .env.example
├── manage.py
├── Telegram_bot.py
├── requirements.txt
├── README.md
├── body/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── celery.py
├── core/
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tasks.py
│ ├── views.py
│ ├── tests.py
│ ├── urls.py
│ ├── migrations/
│ └── templates/
│ ├── base.html
│ ├── head.html
│ ├── home.html
│ ├── login.html
│ ├── register.html
│ ├── public.html
│ └── private.html