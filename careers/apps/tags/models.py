"""Data Models for careers.apps.tags"""

from django.db import models
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase


# Create your models here.
class JobTag(TaggedItemBase):
    """Through model for defining m2m rel between Jobs and Tags"""

    content_object = ParentalKey(
        "careers_jobs.Job",
        related_name="tagged_items",
        on_delete=models.CASCADE,
    )
