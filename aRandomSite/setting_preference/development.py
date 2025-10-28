from aRandomSite.settings import * # noqa
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s9f)7xpgy$olp4ys4ty#90-q83swa%h1(-=1olcn$f-47=+=pd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # noqa: F405
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # noqa: F405
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # noqa: F405

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # noqa: F405

SITE_ID = 2

COMPRESS_OFFLINE = False 
COMPRESS_ENABLED = False  
