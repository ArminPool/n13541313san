from ..settings import *

DEBUG = True
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