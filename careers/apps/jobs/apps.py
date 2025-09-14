"""AppConf for careers.apps.jobs"""

from django.apps import AppConfig


# Create your AppConf here.
class JobsConfig(AppConfig):
    """App Configuration for careers.apps.jobs"""

    label = "careers_jobs"
    name = "careers.apps.jobs"
    default_auto_field = "django.db.models.BigAutoField"
