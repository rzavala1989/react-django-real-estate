from .base import *

# EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
# EMAIL_HOST = env("EMAIL_HOST")
# EMAIL_USE_TLS = True
# EMAIL_PORT = env("EMAIL_PORT")
# EMAIL_HOST_USER = env("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
# DEFAULT_FROM_EMAIL = "info@real-estate.com"
# DOMAIN = env("DOMAIN")
# SITE_NAME = "Real Estate"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "estate",
        "USER": "postgres",
        "PASSWORD": "Marcel2018!",
        "HOST": "localhost",
        "PORT": 5432,
    }
}


# CELERY_BROKER_URL = env("CELERY_BROKER")
# CELERY_RESULT_BACKEND = env("CELERY_BACKEND")
# CELERY_TIMEZONE = "America/Los_Angeles"