"""AppConf for careers.ui"""

from django.apps import AppConfig


# Create your config here.
class TheCertainNewUIConfig(AppConfig):
    """App configuration for careers.ui"""

    name = "careers.ui"
    label = "careers_ui"
    default_auto_field = "django.db.models.BigAutoField"
