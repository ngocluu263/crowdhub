# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'crowdhub',
        'USER': 'crowdhubuser',
        'PASSWORD': 'crowdhubpass1!',
        'HOST': 'localhost',
        'PORT': '',
    },
}


# Setup mongo connection
MONGO_DATABASE_NAME = 'crowdhub_data'
from mongoengine import connect
DEFAULT_CONNECTION_NAME = connect(MONGO_DATABASE_NAME)

