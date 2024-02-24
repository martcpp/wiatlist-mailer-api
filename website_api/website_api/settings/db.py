from .base import *

def set_database(database =None, default=False):
    if database == 'POSTGRESQL' or default == True:
        DATABASES = {
        'default': {
            'ENGINE':'django.db.backends.postgresql',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': config('DB_HOST'),
            'PORT': config('DB_PORT'),
            'ATOMIC_REQUESTS': False
            
        }
    }


    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    return DATABASES