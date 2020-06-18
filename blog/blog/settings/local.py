
DEBUG = True

ALLOWED_HOSTS = []


STATIC_URL = '/static/'

STATICFILES_DIRS = [ 
    os.path.join(BASE_DIR, "static-storage") 
]

STATIC_ROOT = [
    os.path.join(os.path.dirname(BASE_DIR), "static-serve")
]

EMAIL_HOST = smtp.gmail.com
EMAIL_PORT = 587
EMAIL_HOST_USER = vikusingh210@gmail.com
EMAIL_HOST_PASSWORD = frontmissionevolved
EMAIL_USE_TLS = True
# EMAIL_USE_SSL : Whether to use an implicit TLS secure connection

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
