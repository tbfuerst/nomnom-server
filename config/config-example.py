
SECRET_KEY = 'abc'
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1",]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nomnom_db',
        'USER': 'nomnom',
        'PASSWORD': 'unsafe-password',
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }
}