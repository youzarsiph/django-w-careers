"""AppConf for careers.cms"""

from django.apps import AppConfig


# Create your config here.
class CMSConfig(AppConfig):
    """App configuration for careers.cms"""

    name = "careers.cms"
    label = "careers_cms"
    default_auto_field = "django.db.models.BigAutoField"
