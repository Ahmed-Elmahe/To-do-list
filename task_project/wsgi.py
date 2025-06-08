"""
WSGI config for task_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_project.settings')

base_application = get_wsgi_application()

application = WhiteNoise(
    base_application,
    root=settings.STATIC_ROOT,
    prefix=settings.STATIC_URL,
    index_file=True
)

