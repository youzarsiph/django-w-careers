"""Job model"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel
from wagtail.api import APIField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.fields import RichTextField, StreamField
from wagtail.search import index

from careers.apps.jobs import JOB_SENIORITY_LEVELS, JOB_TYPES
from careers.cms.blocks import AllBlocks


# Create your models here.
class FormField(AbstractFormField):
    job = ParentalKey(
        "careers_jobs.Job",
        on_delete=models.CASCADE,
        related_name="form_fields",
    )


class AbstractJob(AbstractEmailForm):
    """Abstract class for extension"""

    type = models.CharField(
        max_length=16,
        choices=JOB_TYPES,
        verbose_name=_("type"),
        help_text=_("Job type"),
    )
    level = models.CharField(
        max_length=16,
        choices=JOB_SENIORITY_LEVELS,
        verbose_name=_("seniority level"),
        help_text=_("Job seniority level"),
    )
    link = models.URLField(
        null=True,
        blank=True,
        verbose_name=_("link"),
        help_text=_("Job apply link (if external)"),
    )
    is_remote = models.BooleanField(
        default=False,
        verbose_name=_("is remote"),
        help_text=_("Designates if job is remote"),
    )
    is_open = models.BooleanField(
        default=True,
        verbose_name=_("is remote"),
        help_text=_("Designates if job is open for applications"),
    )
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_("salary"),
        help_text=_("Job salary"),
    )
    country = CountryField(
        null=True,
        blank=True,
        verbose_name=_("country"),
        help_text=_("Country"),
    )
    description = models.CharField(
        max_length=256,
        verbose_name=_("description"),
        help_text=_("Job description"),
    )
    details = StreamField(
        AllBlocks(),
        verbose_name=_("details"),
        help_text=_("Job details"),
    )
    skills = ClusterTaggableManager(
        blank=True,
        through="careers_tags.JobTag",
        verbose_name=_("skills"),
        help_text=_("Required skills"),
    )
    message = RichTextField(
        verbose_name=_("message"),
        help_text=_("Message to display after applying for job"),
    )

    subpage_types = []
    context_object_name = "job"
    parent_page_types = ["careers_categories.JobCategory"]
    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel("type"),
        FieldPanel("level"),
        FieldPanel("link"),
        FieldPanel("is_remote"),
        FieldPanel("description"),
        FieldPanel("details"),
        FieldPanel("country"),
        FieldPanel("skills"),
        FieldPanel("message"),
        MultiFieldPanel(
            [
                FieldPanel("subject"),
                FieldRowPanel([FieldPanel("from_address"), FieldPanel("to_address")]),
            ],
            _("Email"),
        ),
        InlinePanel("form_fields"),
    ]
    search_fields = AbstractEmailForm.search_fields + [
        index.FilterField("is_open"),
        index.FilterField("is_remote"),
        index.FilterField("country"),
        index.SearchField("description"),
        index.SearchField("details"),
    ]
    api_fields = [
        APIField("is_remote"),
        APIField("country"),
        APIField("description"),
        APIField("details"),
        APIField("skills"),
    ]

    class Meta:
        """Meta data"""

        abstract = True


class Job(AbstractJob):
    """Jobs"""

    template = "careers/job.html"
