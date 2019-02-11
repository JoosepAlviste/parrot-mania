from settings.staging import *


# Allowed hosts for the site
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['office.TODO.com', 'TODO.com'])

# Static site url, used when we need absolute url but lack request object, e.g. in email sending.
SITE_URL = env.str('RAZZLE_SITE_URL', default='https://TODO.com')
DJANGO_SITE_URL = env.str('RAZZLE_BACKEND_SITE_URL', default='https://office.TODO.com')

CSRF_COOKIE_DOMAIN = env.str('DJANGO_CSRF_COOKIE_DOMAIN', default='.TODO.com')

EMAIL_HOST_PASSWORD = env.str('DJANGO_EMAIL_HOST_PASSWORD', default='TODO')

RAVEN_BACKEND_DSN = env.str('DJANGO_RAVEN_BACKEND_DSN', default='https://TODO:TODO@sentry.thorgate.eu/TODO')
RAVEN_PUBLIC_DSN = env.str('DJANGO_RAVEN_PUBLIC_DSN', default='https://TODO@sentry.thorgate.eu/TODO')
RAVEN_CONFIG['dsn'] = RAVEN_BACKEND_DSN

# CORS overrides
CORS_ORIGIN_WHITELIST = env.list('DJANGO_CORS_ORIGIN_WHITELIST', default=ALLOWED_HOSTS)
CSRF_TRUSTED_ORIGINS = env.list('DJANGO_CSRF_TRUSTED_ORIGINS', default=ALLOWED_HOSTS)

# Enable S3 storage
DEFAULT_FILE_STORAGE = 'parrot_mania.storages.MediaStorage'
MEDIA_ROOT = env.str('DJANGO_MEDIA_ROOT', default='')
AWS_STORAGE_BUCKET_NAME = env.str('DJANGO_AWS_STORAGE_BUCKET_NAME', default='parrot_mania-production')
AWS_ACCESS_KEY_ID = env.str('DJANGO_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env.str('DJANGO_AWS_SECRET_ACCESS_KEY')
