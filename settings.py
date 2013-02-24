# -*- coding: utf-8 -*-
__author__ = 'Kirill S. Yakovenko'
__email__ = 'kirill.yakovenko@gmail.com'

# Django settings for geometrical_community project.

import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

ADMINS = (
     ('Kirill Yakovenko', 'kirill.yakovenko@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_ROOT,'database.db'),
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Omsk'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-RU'

LANGUAGES = [
    ('ru', 'Russian'),#'Русский'),
    ('en', 'English')
]

DEFAULT_LANGUAGE = 0

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'static/media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'a7swblf5!tfqh)1u1!@20&^pz4f8y5%9(=q$t5^m=$n@x5c1$!'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cmsplugin_blog.middleware.MultilingualBlogEntriesMiddleware',

)

ROOT_URLCONF = 'geometrical_community.urls'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.csrf',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)

CMS_TEMPLATES = (
    ('example.html', 'Example Template'),
    ('bootstrap.html', 'HTML5 bootstrap')
)

CMS_PAGE_MEDIA_PATH = os.path.join(MEDIA_ROOT, 'pages')

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # 'django.contrib.comments',
    # external packages
    'cms',
    'mptt',
    'menus',
    'filer',
    'tagging',
    'sekizai',
    'missing',
    'tinymce',
    'easy_thumbnails',
    'simple_translation',
    # cms plugins
    'cms.plugins.flash',
    'cms.plugins.googlemap',
    'cms.plugins.link',
    'cms.plugins.snippet',
    'cms.plugins.text',
    'cms.plugins.twitter',
    'cmsplugin_filer_file',
    'cmsplugin_filer_link',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',
    'cmsplugin_blog',
    'djangocms_utils',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Settings for plugins

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

TEXT_SAVE_IMAGE_FUNCTION='cmsplugin_filer_image.integrations.ckeditor.create_image_plugin'

JQUERY_JS = 'https://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js'
JQUERY_UI_JS = 'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/jquery-ui.min.js'
JQUERY_UI_CSS = 'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/themes/smoothness/jquery-ui.css'

CMS_USE_TINYMCE = True

TINYMCE_SPELLCHECKER = False
TINYMCE_PLUGINS = [
    'autolink',
    'lists',
    'pagebreak',
    'style',
    'layer',
    'table',
    'save',
    'advhr',
    'advimage',
    'advlink',
    'emotions',
    'iespell',
    'inlinepopups',
    'insertdatetime',
    'preview',
    'media',
    'searchreplace',
    'print',
    'contextmenu',
    'paste',
    'directionality',
    'fullscreen',
    'noneditable',
    'visualchars',
    'nonbreaking',
    'xhtmlxtras',
    'template',
    'wordcount',
    'advlist',
    'autosave',
    ]

CMS_PLUGIN_TEXT_TINYMCE_CONFIG={
    'mode': "textareas",
    'theme': "advanced",
    'plugins': ",".join(TINYMCE_PLUGINS), # django-cms
    'language': 'en',
    'theme_advanced_buttons1': "save,newdocument,|,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,styleselect,formatselect,fontselect,fontsizeselect",
    'theme_advanced_buttons2': "cut,copy,paste,pastetext,pasteword,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,help,code,|,insertdate,inserttime,preview,|,forecolor,backcolor",
    'theme_advanced_buttons3': "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr,|,print,|,ltr,rtl,|,fullscreen",
    'theme_advanced_buttons4': "insertlayer,moveforward,movebackward,absolute,|,styleprops,|,cite,abbr,acronym,del,ins,attribs,|,visualchars,nonbreaking,template,pagebreak,restoredraft,visualblocks",

    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'theme_advanced_statusbar_location': "bottom",
    'theme_advanced_resizing': True,
    'table_default_cellpadding': 2,
    'table_default_cellspacing': 2,
    'cleanup_on_startup': False,
    'cleanup': False,
    'paste_auto_cleanup_on_paste': False,
    'paste_block_drop': False,
    'paste_remove_spans': False,
    'paste_strip_class_attributes': False,
    'paste_retain_style_properties': "",
    'forced_root_block': False,
    'force_br_newlines': False,
    'force_p_newlines': False,
    'remove_linebreaks': False,
    'convert_newlines_to_brs': False,
    'inline_styles': False,
    'relative_urls': False,
    #    'content_css' : "css/content.css",
    'style_formats': [
        {'title': 'Bold text', 'inline': 'strong'},
        {'title': 'Italic text', 'inline': 'em'},
        {'title': 'Big text', 'inline': 'span', 'classes': 'big-text'},
        {'title': 'Medium text', 'inline': 'span', 'classes': 'medium-text'},
        {'title': 'Small text', 'inline': 'span', 'classes': 'small-text'},
        {'title': 'Micro text', 'inline': 'span', 'classes': 'micro-text'},
        {'title': 'Colors'},
        {'title': 'Gray text', 'inline': 'span', 'classes': 'gray-text'},
        {'title': 'Pink text', 'inline': 'span', 'classes': 'pink-text'},
        {'title': 'White text', 'inline': 'span', 'classes': 'white-text'},
        {'title': 'Button styles'},
        {'title': 'Primary button', 'selector': 'a', 'classes': 'primaryButton'},
        {'title': 'Secondary button', 'selector': 'a', 'classes': 'secondaryButton'},
        #        {'title': 'Table styles'},
        #        {'title': 'Table row 1', 'selector': 'tr', 'classes': 'tablerow1'},
    ],
    }
