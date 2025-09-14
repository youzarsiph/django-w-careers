"""URLConf for careers.ui"""

from django.urls import path

from careers.ui import views

# Create your URLConf here.
app_name = "careers"

urlpatterns = [
    path("jobs/", views.JobListView.as_view(), name="jobs"),
    path("search/", views.SearchView.as_view(), name="search"),
]
