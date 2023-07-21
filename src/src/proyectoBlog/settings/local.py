from .base import *
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'paginablog',
        'USER':'root123',
        'PASSWORD':'nicolas2',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
