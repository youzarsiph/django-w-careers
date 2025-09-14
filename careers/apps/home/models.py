"""Home page"""

from wagtail.models import Page


# Create your models here.
class Home(Page):
    """Home page"""

    context_object_name = "home"
    template = "careers/base.html"
    parent_page_types = ["wagtailcore.Page"]
