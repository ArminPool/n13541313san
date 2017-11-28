from ..settings import *
DEBUG = True
ALLOWED_HOSTS = [u'navasangold.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'navasang_navasangold',
        'USER': 'navasang_armin',
        'PASSWORD': '123555888armin',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
        'HOST':'localhost'

    }
}