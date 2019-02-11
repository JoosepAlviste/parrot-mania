from django.apps import AppConfig
from django.core import checks

from tg_utils.checks import check_production_settings, check_sentry_config


class ParrotManiaConfig(AppConfig):
    name = 'parrot_mania'
    verbose_name = "Parrot mania"

    def ready(self):
        # Import and register the system checks
        checks.register(check_production_settings)
        checks.register(check_sentry_config)
