"""AppConf for careers.apps.categories"""

from django.apps import AppConfig


# Create your config here.
class CategoriesConfig(AppConfig):
    """App configuration for careers.apps.categories"""

    label = "careers_categories"
    name = "careers.apps.categories"
    default_auto_field = "django.db.models.BigAutoField"

    def ready(self) -> None:
        """Register signal receivers"""

        from careers.apps.signals import register_category_signal_receivers

        register_category_signal_receivers()
