"""AppConf for careers.apps.tags"""

from django.apps import AppConfig


# Create your config here.
class TagsConfig(AppConfig):
    """App configuration for careers.apps.tags"""

    label = "careers_tags"
    name = "careers.apps.tags"
    default_auto_field = "django.db.models.BigAutoField"
