from ..settings import *

DEBUG = False
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
