# Django settings for yotweets project.
import os.path
from django.conf import global_settings

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DEBUG_PROPAGATE_EXCEPTIONS = False

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = os.path.join(PROJECT_ROOT, 'yotweets.db')  # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'site_media')
APP_MEDIA_ROOT = MEDIA_ROOT

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

SERVE_MEDIA = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = '4el$t$n7z9+wb=g8yfwv6^1w_o1=$5n)98sgl7+qkz%&nd!as*'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'yotweets.urls'

LOGIN_URL = '/twitter/login/'

TEMPLATE_DIRS = ( os.path.join(PROJECT_ROOT, 'templates').replace('\\','/'), )

TEST_RUNNER = "saaskit.tests.coverage_runner.run_tests"
COVERAGE_REPORT_PATH = os.path.join(PROJECT_ROOT, 'coverage_report')

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',

    # 3rd party
    'django_extensions',
    'compress',
    'paypal.standard.ipn',
    'perfect404',
    'south',
    'templatesadmin',
    'app_media',
    'uni_form',

    # local
    'simple_adsense',
	'tasks',
	'prepaid',
	'shorturls',
	'twitter_app',
)
# Settings for templates editing via django admin

TEMPLATESADMIN_HIDE_READONLY = True
TEMPLATESADMIN_GROUP = 'Editors'
TEMPLATESADMIN_VALID_FILE_EXTENSIONS = (
        'html',
        'css',
        'txt',
        'backup',
   )

TEMPLATESADMIN_EDITHOOKS = (
        'templatesadmin.edithooks.dotbackupfiles.DotBackupFilesHook',
#        'templatesadmin.edithooks.gitcommit.GitCommitHook',
   )

TEMPLATESADMIN_TEMPLATE_DIRS = (
      ( os.path.join(PROJECT_ROOT, 'templates'), )
   )

COMPRESS = False
COMPRESS_VERSION = False

_default_css_files = (
	'tasks/css/reset.css',
	'uni_form/uni_form/uni-form-generic.css',
	'uni_form/uni_form/uni-form.css',
	'tasks/css/styles.css',
	'tasks/css/ui.datepicker.css',
	'tasks/css/jquery-ui-1.7.2.custom.css',
)
_default_js_files = (
	'uni_form/uni_form/uni-form.jquery.js',
	'tasks/js/jquery-1.3.2.min.js',
	'tasks/js/jquery-ui-1.7.2.custom.min.js',
	'tasks/js/jquery.form.js',
)

COMPRESS_CSS = {  
    'all' : {
        'name' : 'Default theme',
        'source_filenames' : _default_css_files,
        'output_filename' : 'style.css'},
    }
COMPRESS_JS = {
    'all' : {
        'source_filenames' : _default_js_files,
        'output_filename' : 'scripts.js'},
    }

PAYPAL_PRO = False

#Dummy paypal settings
PAYPAL_TEST = True
PAYPAL_RECEIVER_EMAIL='example@example.com'
SUBSCRIPTION_PAYPAL_SETTINGS = {
    'business' : PAYPAL_RECEIVER_EMAIL,
    }

# Website payments Pro settings
PAYPAL_WPP_USER = ""
PAYPAL_WPP_PASSWORD = ""
PAYPAL_WPP_SIGNATURE = ""

if PAYPAL_PRO:

    INSTALLED_APPS += ('paypal.standard', 'paypal.pro')
	
	
# shorurls settings
ROOT_URL = 'http://localhost:8000'
SHORT_BASE_URL = 'http://localhost:8000'
SHORTEN_FULL_BASE_URL = ROOT_URL + '/'
SHORTEN_MODELS = {
	't': 'tasks.task',
	'a': 'tasks.advertisement',
}


# Local settings for development / production
try:
     from local_settings import *
except ImportError:
     pass

