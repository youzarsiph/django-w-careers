"""AppConf for careers.api"""

from django.apps import AppConfig


# Create your AppConf here.
class APIConfig(AppConfig):
    """App Configuration for careers.api"""

    name = "careers.api"
    label = "careers_api"
    default_auto_field = "django.db.models.BigAutoField"
