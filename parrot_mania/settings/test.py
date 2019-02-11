from settings.local import *


SEND_EMAILS = False

DATABASES['default']['TEST'] = {
    'NAME': 'parrot_mania_test',
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
