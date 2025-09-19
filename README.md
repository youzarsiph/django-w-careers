# django-w-careers

[![CI](https://github.com/youzarsiph/django-w-careers/actions/workflows/ci.yml/badge.svg)](https://github.com/youzarsiph/django-w-careers/actions/workflows/ci.yml)
[![CD](https://github.com/youzarsiph/django-w-careers/actions/workflows/cd.yml/badge.svg)](https://github.com/youzarsiph/django-w-careers/actions/workflows/cd.yml)
[![Code Style: Black](https://github.com/youzarsiph/django-w-careers/actions/workflows/black.yml/badge.svg)](https://github.com/youzarsiph/django-w-careers/actions/workflows/black.yml)
[![Code Linting: Ruff](https://github.com/youzarsiph/django-w-careers/actions/workflows/ruff.yml/badge.svg)](https://github.com/youzarsiph/django-w-careers/actions/workflows/ruff.yml)
[![Docker Image](https://github.com/youzarsiph/django-w-careers/actions/workflows/docker-image.yml/badge.svg)](https://github.com/youzarsiph/django-w-careers/actions/workflows/docker-image.yml)
[![Docker Publish](https://github.com/youzarsiph/django-w-careers/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/youzarsiph/django-w-careers/actions/workflows/docker-publish.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/django-w-careers?logo=pypi&logoColor=white)](https://pypi.org/project/django-w-careers/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-w-careers?logo=python&logoColor=white)](https://pypi.org/project/django-w-careers/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/django-w-careers?logo=pypi&logoColor=white)](https://pypi.org/project/django-w-careers/)
[![PyPI - License](https://img.shields.io/pypi/l/django-w-careers?logo=pypi&logoColor=white)](https://pypi.org/project/django-w-careers/)

## Overview

A reusable, production-ready job posting application (One employer) built with Python, Django, Django REST Framework, and Wagtail CMS, styled with Tailwind CSS and daisyUI. It provides modern theming, optional APIs, and sensible defaults so you can deploy quickly and grow with confidence.

---

## Key features

- **Full CMS:** Wagtail-powered editorial interface with pages, media management, search, and governance.  
- **Modern UI:** Utility-first styling with Tailwind CSS and responsive layouts.  
- **Theming:** Out-of-the-box daisyUI themes plus support for custom themes.  
- **API ready:** Optional REST endpoints for headless use and integrations.  
- **CI/CD:** GitHub Actions workflows for automated testing, linting, and deployment.  
- **Dependencies:** Managed by Poetry for reproducible installs.  
- **Formatting:** Black for consistent, automatic code styling.  
- **Linting:** Ruff for fast, comprehensive code quality checks.  
- **Testing:** Django test runner for unit and integration suites.  
- **Boilerplate included:** `.gitignore`, `pyproject.toml`, and other config files to jump-start your project.

---

## Installation

```bash
pip install django-w-careers
```

---

## Configuration

### Add installed apps

```python
# project/settings.py

INSTALLED_APPS = [
    "careers",
    "careers.api",            # Optional: REST API
    "careers.apps.categories",
    "careers.apps.home",      # Optional: If you have a Home model ('home.Home')
    "careers.apps.indexes",
    "careers.apps.jobs",
    "careers.apps.tags",
    "careers.cms",
    "careers.ui",

    # Dependencies
    "rest_wind",              # Optional: REST API
    "rest_framework",         # Optional: REST API
    "wagtail_blocks",
    "django_countries",
    "django_filters",
    "wagtail.contrib.search_promotions",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    # ...
]
```

### Run migrations

```bash
python manage.py migrate
```

### Update URL configuration

```python
# project/urls.py

from django.urls import include, path
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path("", include("careers.ui.urls")),
    path("api/", include("careers.api.urls")),       # Optional: REST API
    path("api/", include("rest_framework.urls")),    # Optional: REST API
    # ...
    path("documents/", include(wagtaildocs_urls)),
    path("dashboard/", include(wagtailadmin_urls)),
    path("", include(wagtail_urls)),                 # Always last
]
```

---

## Theming and templates

All templates in django-w-careers extend `careers/base.html`. Create and customize this base template to match your brand.

### Create the template directory

```bash
mkdir -p your_app/templates/careers
```

### Create the base template

```bash
touch your_app/templates/careers/base.html
```

You can extend or override any provided template for full control.

### Available blocks and context

- **`careers/base.html`**  
  - Blocks: `theme`, `toggle_theme`, `head`, `title`, `styles`, `navbar`, `branding`, `navbar_center`, `navbar_end`, `content`, `footer`, `drawer_branding`, `drawer_content`  
  - Context: `home` (site root page)

- **`careers/index.html`**  
  - Blocks: all from `careers/base.html`  
  - Context: `index` (jobs index page), `jobs` (latest postings)

- **`careers/category_index.html`**  
  - Blocks: all from `careers/base.html`  
  - Context: `category` (Category instance)

- **`careers/category.html`**  
  - Blocks: all from `careers/base.html`  
  - Context: `category` (CategoryIndex instance)

- **`careers/job.html`**  
  - Blocks: all from `careers/base.html`  
  - Context: `job` (Job instance), `form` (application form)

- **`careers/job_landing.html`**  
  - Blocks: all from `careers/job.html`  
  - Context: `job` (Job instance)

- **`careers/job_list.html`**  
  - Blocks: all from `careers/base.html`  
  - Context: `job_list` (Job queryset), `filter` (Filter object)

- **`careers/search.html`**  
  - Blocks: all from `careers/base.html`  
  - Context: `search_results` (`PageQuerySet` results)

---

## Contributing

We welcome contributions from the community. Please review our [CONTRIBUTING](CONTRIBUTING.md) guide for setup, coding conventions, and workflow. Opening an issue before major changes helps align on scope.

---

## Support

For questions, bug reports, or feature requests, open an issue or start a thread in [GitHub Discussions](https://github.com/youzarsiph/django-w-careers/discussions).

---

## License

This project is released under the MIT License. See the [LICENSE](LICENSE) file for details.
