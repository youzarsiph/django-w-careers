"""AppConf for careers.apps.indexes"""

from django.apps import AppConfig


# Create your AppConf here.
class CareersIndexConfig(AppConfig):
    """App Configuration for careers.apps.indexes"""

    label = "careers_indexes"
    name = "careers.apps.indexes"
    default_auto_field = "django.db.models.BigAutoField"
