"""Jobs"""

from django.utils.translation import gettext_lazy as _


# Constants
JOB_TYPES = [
    ("full-time", _("Full-time")),
    ("part-time", _("Part-time")),
    ("contract", _("Contract")),
    ("internship", _("Internship")),
    ("temporary", _("Temporary")),
]

JOB_SENIORITY_LEVELS = [
    ("junior", _("Junior")),
    ("mid", _("Mid")),
    ("senior", _("Senior")),
    ("lead", _("Lead")),
    ("manager", _("Manager")),
]
