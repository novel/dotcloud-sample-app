import os
import os.path

# celery configuration
import djcelery
djcelery.setup_loader()

BROKER_BACKEND = "redis"
BROKER_HOST = "redis.CHANGE_THIS.dotcloud.com"
BROKER_PORT = 2894
BROKER_VHOST = 0
BROKER_PASSWORD = "PASSWORD"

CELERY_RESULT_BACKEND = "redis"
REDIS_HOST = "redis.CHANGE_THIS.dotcloud.com"
REDIS_PORT = 2894
REDIS_DB = 0
REDIS_PASSWORD = "PASSWORD"
REDIS_CONNECT_RETRY = True

# general configuration

PROJECT_DIR = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dotping',
        'USER': 'root',
        'PASSWORD': 'PASSWORD',
        'HOST': 'db.CHANGE_ME.dotcloud.com',
        'PORT': '2865',
    }
}

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = ''

MEDIA_URL = ''

ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = ''

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'frontend.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'djcelery',
    'frontend.ping',
)
