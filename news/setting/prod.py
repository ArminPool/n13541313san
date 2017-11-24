DEBUG = False
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'navasan',
        'USER': 'armin.oldboy',
        'PASSWORD': '123555888mysql',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}