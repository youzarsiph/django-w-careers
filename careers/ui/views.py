"""Views for careers.ui"""

from typing import Any

from django.views import generic
from django_filters.views import FilterView
from wagtail.contrib.search_promotions.models import Query
from wagtail.models import Page

from careers.apps.jobs.models import Job


# Create your views here.
class JobListView(FilterView, generic.ListView):
    """Job List View"""

    model = Job
    paginate_by = 25
    template_name = "careers/job_list.html"
    filterset_fields = ["type", "level", "is_remote", "country", "salary"]
    queryset = (
        Job.objects.live()
        .public()
        .filter(is_open=True)
        .order_by("-latest_revision_created_at")
    )


class SearchView(generic.ListView):
    """Search View"""

    model = Page
    template_name = "careers/search.html"
    context_object_name = "search_results"
    queryset = Page.objects.live().public()

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        """Search and add to context"""

        return {
            **super().get_context_data(**kwargs),
            "search_query": self.request.GET.get("search", None),
            "search_results": self.get_search_results(),
        }

    def get_search_results(self):
        """Search and return results"""

        queryset = self.get_queryset()
        search_query = self.request.GET.get("search", None)

        search_results = queryset.none()

        if search_query:
            search_results = queryset.search(search_query)

            # Log the query so Wagtail can suggest promoted results
            Query.get(search_query).add_hit()

        return search_results
