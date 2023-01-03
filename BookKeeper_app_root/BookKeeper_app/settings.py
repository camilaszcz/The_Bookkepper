"""
Django settings for BookKeeper_app project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""


from django.core.management.utils import get_random_secret_key
from pathlib import Path
import os
import sys
import dj_database_url


BASE_DIR = Path(__file__).resolve().parent.parent

# # Initialise environment variables

# env = environ.Env(
#     # set casting, default value
#     DEBUG=(bool, False)
# )

# # Take environment variables from .env file
# environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# False if not in os.environ because of casting above
# DEBUG = env('DEBUG')
DEBUG = os.getenv("DEBUG", "False") == "True"



# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())


# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "whitenoise.runserver_nostatic",
    "my_library",
    "loans",
    "pages",
    "currently_reading",
    "accounts",
    "next_in_line",
     "storages",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
   
]

ROOT_URLCONF = "BookKeeper_app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "BookKeeper_app.wsgi.application"

DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"


if DEVELOPMENT_MODE is True:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
elif len(sys.argv) > 0 and sys.argv[1] != 'collectstatic':
    if os.getenv("DATABASE_URL", None) is None:
        raise Exception("DATABASE_URL environment variable not defined")
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
    }
    
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME':env('DATABASE_NAME'),
#         'USER':env('DATABASE_USER'),
#         'PASSWORD':env('DATABASE_PASSWORD'),
#         'HOST':env('DATABASE_HOST'),
#         'PORT':env('DATABASE_PORT'),
#     }
# }

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Jerusalem"
USE_I18N = True
USE_TZ = True
USE_L10N = True





# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/




# AWS_ACCESS_KEY_ID = 'key_id'
# AWS_SECRET_ACCESS_KEY = 'access_key'
# AWS_STORAGE_BUCKET_NAME = 'bucket_name'
# AWS_DEFAULT_ACL = 'public-read' 
# AWS_S3_ENDPOINT_URL = 'https://thebookkeeper.fra1.digitaloceanspaces.com' # Make sure nyc3 is correct
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400'
# }

# AWS_STATIC_LOCATION = 'static'
# STATIC_URL = '%s/%s' % (AWS_S3_ENDPOINT_URL, AWS_STATIC_LOCATION)
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = "static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'BookKeeper_app/static')
]
# # Default primary key field type
# # https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_DIRS = [
    os.path.join(BASE_DIR, 'BookKeeper_app/media')
]



from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',

}