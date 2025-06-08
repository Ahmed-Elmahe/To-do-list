"""
WSGI config for task_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from django.conf import settings  # Import settings module

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

# Get the base WSGI application
base_application = get_wsgi_application()

# Wrap with WhiteNoise for static files
application = WhiteNoise(
    base_application,
    root=settings.STATIC_ROOT,  # Uses STATIC_ROOT from settings
    prefix=settings.STATIC_URL,  # Uses STATIC_URL from settings
    index_file=True  # Serve index.html files for directories
)

