from corsheaders.defaults import default_headers

from settings.base import *


DEBUG = False

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['office.parrot-mania.test.TODO.com', 'parrot-mania.test.TODO.com'])

# Static site url, used when we need absolute url but lack request object, e.g. in email sending.
SITE_URL = env.str('RAZZLE_SITE_URL', default='https://parrot-mania.test.TODO.com')
DJANGO_SITE_URL = env.str('RAZZLE_BACKEND_SITE_URL', default='https://office.parrot-mania.test.TODO.com')

CSRF_COOKIE_DOMAIN = env.str('DJANGO_CSRF_COOKIE_DOMAIN', default='.parrot-mania.test.TODO.com')

# Static site url, used when we need absolute url but lack request object, e.g. in email sending.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

EMAIL_HOST_PASSWORD = env.str('DJANGO_EMAIL_HOST_PASSWORD', default='TODO (api key)')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

STATIC_URL = env.str('DJANGO_STATIC_URL', default='/assets/')

# Production logging - all INFO and higher messages go to info.log file. ERROR and higher messages additionally go to
#  error.log file plus to Sentry.
LOGGING['handlers'] = {
    'sentry': {
        'level': 'ERROR',
        'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
    },
}
LOGGING['loggers'][''] = {
    'handlers': ['console', 'sentry'],
    'level': 'INFO',
    'filters': ['require_debug_false'],
}

if env.str('DJANGO_DISABLE_FILE_LOGGING', default='n') != 'y':
    # Add file handlers as addition to sentry
    LOGGING['handlers'].update({
        'info_log': {
            'level': 'INFO',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': '/var/log/parrot_mania/info.log',
            'formatter': 'default',
        },
        'error_log': {
            'level': 'ERROR',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': '/var/log/parrot_mania/error.log',
            'formatter': 'default',
        },
    })
    LOGGING['loggers']['']['handlers'] = ['info_log', 'error_log', 'sentry']

# Sentry error logging
INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
)
RAVEN_BACKEND_DSN = env.str('DJANGO_RAVEN_BACKEND_DSN', default='https://TODO:TODO@sentry.thorgate.eu/TODO')
RAVEN_PUBLIC_DSN = env.str('DJANGO_RAVEN_PUBLIC_DSN', default='https://TODO@sentry.thorgate.eu/TODO')
RAVEN_CONFIG['dsn'] = RAVEN_BACKEND_DSN

# CORS overrides
CORS_ORIGIN_ALLOW_ALL = False
CORS_EXPOSE_HEADERS = default_headers
CORS_ORIGIN_WHITELIST = env.list('DJANGO_CORS_ORIGIN_WHITELIST', default=ALLOWED_HOSTS)
CSRF_TRUSTED_ORIGINS = env.list('DJANGO_CSRF_TRUSTED_ORIGINS', default=ALLOWED_HOSTS)

# Enable S3 storage
DEFAULT_FILE_STORAGE = 'parrot_mania.storages.MediaStorage'
MEDIA_ROOT = env.str('DJANGO_MEDIA_ROOT', default='')
AWS_STORAGE_BUCKET_NAME = env.str('DJANGO_AWS_STORAGE_BUCKET_NAME', default='parrot_mania-staging')
AWS_ACCESS_KEY_ID = env.str('DJANGO_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env.str('DJANGO_AWS_SECRET_ACCESS_KEY')
