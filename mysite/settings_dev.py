# Для запуска на локальной машине запустить команду:
# DJANGO_SETTINGS_MODULE=mysite.settings_dev python3 manage.py runserver
# или
# alias .bash_profile:
# alias django='DJANGO_SETTINGS_MODULE=mysite.settings_dev pyon3 manage.py runserver'

from .settings import *

DEBUG = True

SECRET_KEY = 'y%fs-22vt4y+krzt5-!^khz1!=^h(vf84=-%1nf4o+*-u8wsjn'

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DjangoBlog',
        'USER': 'admin123',
        'PASSWORD': 'admin123',
        'HOST': 'localhost',
        'PORT': '',
        'TEST': {
            'NAME': 'tests'
        }


    },

}
