import os
from website_api.settings.base import DEBUG

from django.core.asgi import get_asgi_application

if DEBUG:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website_api.settings.development')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website_api.settings.production')

application = get_asgi_application()
