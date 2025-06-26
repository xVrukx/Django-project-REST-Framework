# imports

from pathlib import Path
from decouple import config
import os
import pymysql
#-----------------------------------------------
# primry setup

pymysql.install_as_MySQLdb()

BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = ['localhost','127.0.0.1']

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG',default = False, cast = bool)

CELERY_BROKER_URL = 'redis://localhost:6380/0'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CELERY_ACCEPT_CONTENT = ['json']

CELERY_TASK_SERIALIZER = 'json'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
#-----------------------------------------------
# Application definition

INSTALLED_APPS = [
    'core',
    'rest_framework',
    'rest_framework.authtoken',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
#-----------------------------------------------
#middleware

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
#-----------------------------------------------

ROOT_URLCONF = 'body.urls'
#-----------------------------------------------
#templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "core" / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages', 
                
            ],
        },
    },
]
#-----------------------------------------------

WSGI_APPLICATION = 'body.wsgi.application'
#-----------------------------------------------
# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST',default = 'localhost'),
        'PORT': config('DB_PORT',default = '3306'),

    }
}
#-----------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
#-----------------------------------------------
# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
#-----------------------------------------------
# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'
#-----------------------------------------------
# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#-----------------------------------------------
#rest

REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (
                'rest_framework.authentication.TokenAuthentication',
                                      ),
    'DEFAULT_PERMISSION_CLASSES': (
                'rest_framework.permissions.IsAuthenticated',
                                      ),
                }