
DEBUG = True

ALLOWED_HOSTS = []


STATIC_URL = '/static/'

STATICFILES_DIRS = [ 
    os.path.join(BASE_DIR, "static-storage") 
]

STATIC_ROOT = [
    os.path.join(os.path.dirname(BASE_DIR), "static-serve")
]
