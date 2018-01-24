from ..settings import *

DEBUG = False
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
ALLOWED_HOSTS = [u'navasangold.com', 'www.navasangold.com']
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

MEDIA_ROOT = os.path.join(STATIC_ROOT, 'media')
MEDIA_URL = '/static/media/'
