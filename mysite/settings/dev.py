from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g(qu+x0j2wop48*ty=jr8rgun@$z#q!2m!=kwh@au)4g@3#nt%'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ['127.0.0.1']
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
