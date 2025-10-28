"""
Django settings for production environment
"""

import os
from pathlib import Path
from aRandomSite.settings import * # noqa

BASE_DIR = Path(__file__).resolve().parent.parent


# Security - Use environment variable
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# CRITICAL: Set to False in production
DEBUG = False

ALLOWED_HOSTS = ['shayanborzu.ir', 'www.shayanborzu.ir']


# Same INSTALLED_APPS and MIDDLEWARE as development


# Database - MySQL/PostgreSQL for production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '3306'),
    }
}


# Static files - Different paths for production
STATIC_URL = '/static/'
STATIC_ROOT = '/home/cpanelusername/public_html/static'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/cpanelusername/public_html/media'


# Email - Real SMTP for production
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
DEFAULT_FROM_EMAIL = 'noreply@yourdomain.com'


# Security settings - Strict for production
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
