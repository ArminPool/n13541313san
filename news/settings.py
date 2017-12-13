"""
Django settings for news project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_g+$23mmc_n@@)_*j#8-l)r60d6*ci$7^3n6605((un33(72k1'

# SECURITY WARNING: don't run with debug turned on in production!


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django_mysql',
    'posts',
    'users',
    'specificpages',
    'jalali_date',
    'ckeditor',
    'imagekit',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'news.middleware.TimezoneMiddleware',

]

ROOT_URLCONF = 'news.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'news.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DEBUG = True

if DEBUG:

    ALLOWED_HOSTS = ['www.navasangold.com', '127.0.0.1']
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'navasan',
            'USER': 'root',
            'PASSWORD': '123555888mysql',
            'OPTIONS': {
                'charset': 'utf8mb4',
            },
        }
    }
else:

    ALLOWED_HOSTS = [u'navasangold.com', 'www.navasangold.com']
    # correct database character :ALTER TABLE your_table_name CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'navasang_navasangold',
            'USER': 'navasang_armin',
            'PASSWORD': '123555888armin',
            'OPTIONS': {
                'charset': 'utf8mb4',
            },
            'HOST': 'localhost'

        }
    }

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
CKEDITOR_CONFIGS = {
    'awesome_ckeditor': {

        'toolbar': 'full',
        'skin': 'office2013',
        'height': 300,
        'width': 600,
    },
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 300,
    },
}

LOGIN_REDIRECT_URL = '/user'

LOGIN_URL = '/user/login/'

LOGIN_EXEMPT_URLS = (
    r'^user/logout/$',
    r'^user/register/$'
)
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST = 'ir-hs01.serversgig.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'support@navasangold.com'
EMAIL_HOST_PASSWORD = '123555888navasan'

# Internationalization

# https://docs.djangoproject.com/en/1.11/topics/i18n/




LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
CKEDITOR_UPLOAD_PATH = "uploaded/"
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "public_html", "static")
MEDIA_ROOT = os.path.join(BASE_DIR, 'news/media')

# STATIC_ROOT='/home/navasang/public_html/'
MEDIA_URL = '/media/'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}
