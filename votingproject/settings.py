"""
Django settings for votingproject project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path
from django.contrib import messages
import django_heroku
import cloudinary

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("CLEVER_VOTING")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (os.environ.get("DEBUG_VALUE") == 'True')

CSRF_TRUSTED_ORIGINS = os.environ.get(
    "CLEVER_VOTING_CSRF_TRUSTED_ORIGINS").split(",")

ALLOWED_HOSTS = os.environ.get(
    "CLEVER_VOTING_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

HASHID_SALT = os.environ.get('HASHID_SALT')

# clodinary setup
# SET ENVIRONMENT VARIABLES
cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key=os.environ.get('CLOUDINARY_API_KEY'),
    api_secret=os.environ.get(
        'CLOUDINARY_API_SECRET'),
    secure=os.environ.get('CLOUDINARY_SECURE')
)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    # USER APPS
    'contestants',
    'voters',
    'django.contrib.humanize',
    'blog',
    'award',
    'payments',

]

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'votingproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'votingproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

CLEVER_VOTING_PG_PASSWORD = os.environ.get("CLEVER_VOTING_PG_PASSWORD")
CLEVER_VOTING_PG_PORT = os.environ.get("CLEVER_VOTING_PG_PORT")
CLEVER_VOTING_PG_HOST = os.environ.get("CLEVER_VOTING_PG_HOST")
CLEVER_VOTING_PG_USER = os.environ.get("CLEVER_VOTING_PG_USER")

DATABASES = dict()
IS_LIVE = os.environ.get("IS_LIVE")

if IS_LIVE == "True":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'railway',
            'USER': CLEVER_VOTING_PG_USER,
            'HOST': CLEVER_VOTING_PG_HOST,
            'PASSWORD': CLEVER_VOTING_PG_PASSWORD,
            'PORT': CLEVER_VOTING_PG_PORT,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_TZ = True

USE_L10N = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Managing staitc files
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MESSAGE_TAGS = {
    messages.ERROR: "danger"
}

# PAYSTACK KEYS
PAYSTACKPUBKEY = os.environ.get("PAY_STACK_TEST_PUBKEY")
PAYSTACK_SECRET_KEY = os.environ.get("PAYSTACKSCRTKEY")

MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
MEDIA_URL = '/media/'


django_heroku.settings(locals())
