from .base import *
from .db   import set_database

ALLOWED_HOSTS = []


 
set_database('POSTGRESQL', True)

# Redirect all non-HTTPS requests to HTTPS
SECURE_SSL_REDIRECT = True

# Ensure that the session cookie is only sent over HTTPS connections
SESSION_COOKIE_SECURE = True

# Ensure that the CSRF cookie is only sent over HTTPS connections
CSRF_COOKIE_SECURE = True

# Enable the browser's XSS protection filter
SECURE_BROWSER_XSS_FILTER = True

# Prevent browsers from interpreting files as a different MIME type
SECURE_CONTENT_TYPE_NOSNIFF = True

# Configure the X-Frame-Options header to prevent embedding in frames
X_FRAME_OPTIONS = 'DENY'

# Set the HTTP Strict Transport Security (HSTS) header
SECURE_HSTS_SECONDS = 31536000  # One year

SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_HSTS_PRELOAD = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')






SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'




CORS_ALLOW_ALL_ORIGINS = False

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "",
    # Add other allowed origins as needed
]
CSRF_TRUSTED_ORIGINS=['']