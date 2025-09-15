"""Data Models for careers.apps.categories"""

from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.search import index

from careers.apps.mixins import ChildPaginatorMixin


# Create your models here.
class AbstractJobCategory(ChildPaginatorMixin, Page):
    """Abstract class for extension"""

    description = RichTextField(
        null=True,
        blank=True,
        verbose_name=_("description"),
        help_text=_("Category description"),
    )

    show_in_menus = True
    context_object_name = "category"
    subpage_types = ["careers_jobs.Job"]
    parent_page_types = ["careers_indexes.CareersIndex"]
    content_panels = Page.content_panels + [FieldPanel("description")]
    api_fields = [APIField("description", serializer=RichTextField())]
    search_fields = Page.search_fields + [index.SearchField("description")]

    class Meta(Page.Meta):
        """Meta data"""

        abstract = True

    def get_ordered_children(self):
        return super().get_ordered_children().order_by("-latest_revision_created_at")


class JobCategory(AbstractJobCategory):
    """Job Categories"""

    template = "careers/category.html"
