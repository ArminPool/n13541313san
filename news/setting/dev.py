from ..settings import *

DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'arminoldboy$navasan',
        'USER': 'arminoldboy',
        'PASSWORD': '123555888mysql',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
        'HOST':'arminoldboy.mysql.pythonanywhere-services.com'
    }
}