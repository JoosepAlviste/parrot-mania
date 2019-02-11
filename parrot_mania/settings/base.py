"""
Django settings for Parrot mania project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
import os
from datetime import timedelta

import environ


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# Build paths inside the project like this: os.path.join(SITE_ROOT, ...)
SITE_ROOT = os.path.dirname(os.path.dirname(__file__))
ROOT_DIR = environ.Path(SITE_ROOT)


# Load env to get settings
env = environ.Env()

READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=True)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    # By default use django.env file from project root directory
    env.read_env(str(ROOT_DIR.path('django.env')))

# Load env to get settings
ROOT_DIR = environ.Path(SITE_ROOT)
env = environ.Env()

READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=True)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    # By default use django.env file from project root directory
    env.read_env(str(ROOT_DIR.path('django.env')))


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', default=True)

ADMINS = (
    ('Admins', 'info@TODO.com'),
)
MANAGERS = ADMINS
EMAIL_SUBJECT_PREFIX = '[Parrot mania] '  # subject prefix for managers & admins

SESSION_COOKIE_NAME = 'parrot_mania_ssid'
SESSION_COOKIE_DOMAIN = env.str('DJANGO_SESSION_COOKIE_DOMAIN', default=None)

CSRF_COOKIE_DOMAIN = env.str('DJANGO_CSRF_COOKIE_DOMAIN', default=None)
CSRF_COOKIE_HTTPONLY = False


INSTALLED_APPS = [
    # Local apps
    'accounts',
    'parrot_mania',

    # Third-party apps
    'rest_framework',
    'django_filters',
    'tg_react',
    'crispy_forms',
    'corsheaders',

    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(SITE_ROOT, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': env.str('DJANGO_DATABASE_HOST', default='postgres'),
        'PORT': env.int('DJANGO_DATABASE_PORT', default=5432),
        'NAME': env.str('DJANGO_DATABASE_NAME', default='parrot_mania'),
        'USER': env.str('DJANGO_DATABASE_USER', default='parrot_mania'),
        'PASSWORD': env.str('DJANGO_DATABASE_PASSWORD', default='parrot_mania'),
    }
}


# Redis config (used for caching)
REDIS_URL = env.str('DJANGO_REDIS_URL', default='redis://redis:6379/1')
REDIS_CACHE_URL = env.str('DJANGO_REDIS_CACHE_URL', default=REDIS_URL)
REDIS_CELERY_URL = env.str('DJANGO_REDIS_CELERY_URL', default=REDIS_URL)


# Caching
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_CACHE_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}


# Internationalization
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'English'),
    ('et', 'Eesti keel'),
)
LOCALE_PATHS = (
    'locale',
)

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Media files (user uploaded/site generated)
MEDIA_ROOT = env.str('DJANGO_MEDIA_ROOT', default='/files/media')
MEDIA_URL = env.str('DJANGO_MEDIA_URL', default='/media/')
MEDIAFILES_LOCATION = env.str('DJANGO_MEDIAFILES_LOCATION', default='media')

# In staging/prod we use S3 for file storage engine
AWS_ACCESS_KEY_ID = '<unset>'
AWS_SECRET_ACCESS_KEY = '<unset>'
AWS_STORAGE_BUCKET_NAME = '<unset>'
AWS_DEFAULT_ACL = 'public-read'
AWS_IS_GZIPPED = True
AWS_S3_ENCRYPTION = True
AWS_S3_FILE_OVERWRITE = False
AWS_S3_REGION_NAME = 'eu-central-1'
AWS_S3_SIGNATURE_VERSION = 's3v4'

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=1209600',  # 2 weeks in seconds
}

# Static files (CSS, JavaScript, images)
STATIC_ROOT = '/files/assets'
STATIC_URL = env.str('DJANGO_STATIC_URL', default='/assets/')


STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('DJANGO_SECRET_KEY', default='dummy key')

AUTH_USER_MODEL = 'accounts.User'

# Static site url, used when we need absolute url but lack request object, e.g. in email sending.
SITE_URL = env.str('RAZZLE_SITE_URL', default='http://127.0.0.1:8000')
DJANGO_SITE_URL = env.str('RAZZLE_BACKEND_SITE_URL', default='http://127.0.0.1:3000')
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['django', 'localhost', '127.0.0.1'])
CSRF_TRUSTED_ORIGINS = env.list('DJANGO_CSRF_TRUSTED_ORIGINS', default=ALLOWED_HOSTS)
CORS_ORIGIN_WHITELIST = env.list('DJANGO_CORS_ORIGIN_WHITELIST', default=ALLOWED_HOSTS)

# Don't allow site's content to be included in frames/iframes.
X_FRAME_OPTIONS = 'DENY'


ROOT_URLCONF = 'parrot_mania.urls'

WSGI_APPLICATION = 'parrot_mania.wsgi.application'


LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = 'login'


# Crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'


# Email config
DEFAULT_FROM_EMAIL = "Parrot mania <info@TODO.com>"
SERVER_EMAIL = "Parrot mania server <server@TODO.com>"

# Show emails in the console, but don't send them.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# SMTP  --> This is only used in staging and production
EMAIL_HOST = env.str('DJANGO_EMAIL_HOST', default='smtp.sparkpostmail.com')
EMAIL_PORT = env.int('DJANGO_EMAIL_PORT', default=587)
EMAIL_HOST_USER = env.str('DJANGO_EMAIL_HOST_USER', default='SMTP_Injection')
EMAIL_HOST_PASSWORD = env.str('DJANGO_EMAIL_HOST_PASSWORD', default='')


# Base logging config. Logs INFO and higher-level messages to console. Production-specific additions are in
#  production.py.
#  Notably we modify existing Django loggers to propagate and delegate their logging to the root handler, so that we
#  only have to configure the root handler.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s [%(levelname)s] %(name)s:%(lineno)d %(funcName)s - %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'django': {'handlers': [], 'propagate': True},
        'django.request': {'handlers': [], 'propagate': True},
        'django.security': {'handlers': [], 'propagate': True},
    }
}

TEST_RUNNER = 'django.test.runner.DiscoverRunner'


# Disable a few system checks. Careful with these, only silence what your really really don't need.
# TODO: check if this is right for your project.
SILENCED_SYSTEM_CHECKS = [
    'security.W001',  # we don't use SecurityMiddleware since security is better applied in nginx config
]


# Rest framework configuration
REST_FRAMEWORK = {
    # Disable Basic auth
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    # Change default full-url media files to be only stored path, needs /media prepended in frontend
    'UPLOADED_FILES_USE_URL': False,
}

# Default values for sentry
RAVEN_BACKEND_DSN = env.str('DJANGO_RAVEN_BACKEND_DSN', default='https://TODO:TODO@sentry.thorgate.eu/TODO')
RAVEN_PUBLIC_DSN = env.str('DJANGO_RAVEN_PUBLIC_DSN', default='https://TODO@sentry.thorgate.eu/TODO')
RAVEN_CONFIG = {'dsn': RAVEN_BACKEND_DSN}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'pk',
    'USER_ID_CLAIM': 'user_id',
}


# CORS settings
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
