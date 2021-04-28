import os

if os.getenv('DOCKER_CONTAINER'):
	POSTGRES_HOST = os.getenv('POSTGRES_HOST')
else:
	POSTGRES_HOST = '127.0.0.1'
SECRET_KEY = 'NJQCjO8KjS6NDqVpVpBqDPF5lCibttPnRPsGl34Js6A8R8ETX983CXTlD3AD50cr'
DEBUG = True
ALLOWED_HOSTS = ["10.100.0.30",]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nomnom_db',
        'USER': 'nomnom',
        'PASSWORD': '5bdd935678ebcbe342906ca8f328879f',
        'HOST': POSTGRES_HOST,
        'PORT': 5432,
    }
}
