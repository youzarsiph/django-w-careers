"""careers Index page"""

from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.search import index

from careers.apps.jobs.models import Job
from careers.cms.blocks import MediaBlock


# Create your models here.
class AbstractCareersIndex(Page):
    """Abstract model for extension"""

    content = StreamField(
        MediaBlock(),
        verbose_name=_("content"),
        help_text=_("Page content"),
    )

    context_object_name = "index"
    parent_page_types = ["home.Home"]
    subpage_types = ["careers_categories.JobCategory"]

    api_fields = [APIField("content")]
    content_panels = Page.content_panels + [FieldPanel("content")]
    search_fields = Page.search_fields + [index.SearchField("content")]

    class Meta(Page.Meta):
        """Meta data"""

        abstract = True

    def get_context(self, request, *args, **kwargs):
        """Add latest jobs to context"""

        context = super().get_context(request, *args, **kwargs)

        return {
            **context,
            "jobs": self.get_descendants()
            .type(Job)
            .live()
            .order_by("-latest_revision_created_at")
            .specific(),
        }


class CareersIndex(AbstractCareersIndex):
    """careers index pages"""

    template = "careers/index.html"
