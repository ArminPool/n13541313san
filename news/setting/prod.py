from ..settings import *
DEBUG = False
ALLOWED_HOSTS = ['*']
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