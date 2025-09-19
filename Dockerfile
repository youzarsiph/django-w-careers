# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Create new Django project and configure the settings
RUN django-admin startproject core
RUN cp -r careers core

# Configure settings
RUN echo "AUTH_USER_MODEL = 'users.User'" >> core/settings.py
RUN echo "INSTALLED_APPS += [" >> core/settings.py
RUN echo "    'careers'," >> core/settings.py
RUN echo "    'careers.apps.categories'," >> core/settings.py
RUN echo "    'careers.apps.home'," >> core/settings.py
RUN echo "    'careers.apps.indexes'," >> core/settings.py
RUN echo "    'careers.apps.jobs'," >> core/settings.py
RUN echo "    'careers.apps.tags'," >> core/settings.py
RUN echo "    'careers.cms'," >> core/settings.py
RUN echo "    'careers.ui'," >> core/settings.py
RUN echo "    'wagtail_blocks'," >> core/settings.py
RUN echo "    'django_countries'," >> core/settings.py
RUN echo "    'django_filters'," >> core/settings.py
RUN echo "    'rest_wind'," >> core/settings.py
RUN echo "    'rest_framework'," >> core/settings.py
RUN echo "    'wagtail.contrib.search_promotions'," >> core/settings.py
RUN echo "    'wagtail.contrib.forms'," >> core/settings.py
RUN echo "    'wagtail.contrib.redirects'," >> core/settings.py
RUN echo "    'wagtail.embeds'," >> core/settings.py
RUN echo "    'wagtail.sites'," >> core/settings.py
RUN echo "    'wagtail.users'," >> core/settings.py
RUN echo "    'wagtail.snippets'," >> core/settings.py
RUN echo "    'wagtail.documents'," >> core/settings.py
RUN echo "    'wagtail.images'," >> core/settings.py
RUN echo "    'wagtail.search'," >> core/settings.py
RUN echo "    'wagtail.admin'," >> core/settings.py
RUN echo "    'wagtail'," >> core/settings.py
RUN echo "    'modelcluster'," >> core/settings.py
RUN echo "    'taggit'," >> core/settings.py
RUN echo "]" >> core/settings.py
RUN echo "MIDDLEWARE += ['wagtail.contrib.redirects.middleware.RedirectMiddleware']" >> core/settings.py

# Setup URLConf
RUN echo "from django.urls import include" >> core/urls.py
RUN echo "from wagtail import urls as wagtail_urls" >> core/urls.py
RUN echo "from wagtail.admin import urls as wagtailadmin_urls" >> core/urls.py
RUN echo "from wagtail.documents import urls as wagtaildocs_urls" >> core/urls.py
RUN echo "urlpatterns += [" >> core/urls.py
RUN echo "    path('', include('careers.ui.urls', namespace='careers'))," >> core/urls.py
RUN echo "    path('api/', include('careers.api.urls'))," >> core/urls.py
RUN echo "    path('api/', include('rest_framework.urls'))," >> core/urls.py
RUN echo "    path('documents/', include(wagtaildocs_urls))," >> core/urls.py
RUN echo "    path('dashboard/', include(wagtailadmin_urls))," >> core/urls.py
RUN echo "    path('', include(wagtail_urls))," >> core/urls.py
RUN echo "]" >> core/urls.py

# Run migrations
RUN cd core && python manage.py migrate


WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi"]
