from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^6r4n+hf)%pm3iqfa0erkfzozn3q1=gi)x)p&sl^2ewv*ptzvq'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


INSTALLED_APPS = INSTALLED_APPS + [
		"debug_toolbar",
		"django_extensions", # kvůli API
		"wagtail.contrib.styleguide", # backend style - ikony, ...
	]

MIDDLEWARE = MIDDLEWARE + [
		"debug_toolbar.middleware.DebugToolbarMiddleware",
	]

INTERNAL_IPS = ("127.0.0.1", "172.17.0.1")


		# CACHES
CACHES = {
	"default": {
		"BACKEND":  "django.core.cache.backends.filebased.FileBasedCache",
		"LOCATION": "/Users/kilimetr/Desktop/python/webscrapping/Slevy/WEB/WEB/cache",
	},
}


try:
    from .local import *
except ImportError:
    pass
