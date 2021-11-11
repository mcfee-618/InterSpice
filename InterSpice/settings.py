"""
Django settings for InterSpice project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*c(vqpu7+v=fug7$r*m3i5(-1vbecvil_0i0h=)8u+(0=%25&='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions',
    'django.contrib.messages', 'django.contrib.staticfiles', 'album.apps.AlbumConfig',
    'article.apps.ArticleConfig', 'ckeditor', 'ckeditor_uploader', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'InterSpice.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'InterSpice.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/setting/s/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'interspice',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': 'root'
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR + "/static",
]

CKEDITOR_UPLOAD_PATH = ""

CKEDITOR_FILENAME_GENERATOR = 'utils.get_filename'

CUSTOM_TOOLBAR = [
    {
        "name": "document",
        "items": [
            "Styles",
            "Format",
            "Bold",
            "Italic",
            "Underline",
            "Strike",
            "-",
            "TextColor",
            "BGColor",
            "-",
            "JustifyLeft",
            "JustifyCenter",
            "JustifyRight",
            "JustifyBlock",
        ],
    },
    {
        "name": "widgets",
        "items": [
            "Undo",
            "Redo",
            "-",
            "NumberedList",
            "BulletedList",
            "-",
            "Outdent",
            "Indent",
            "-",
            "Link",
            "Unlink",
            "-",
            "Image",
            "CodeSnippet",
            "Table",
            "HorizontalRule",
            "Smiley",
            "SpecialChar",
            "-",
            "Blockquote",
            "-",
            "ShowBlocks",
            "Maximize",
        ],
    },
]

CKEDITOR_CONFIGS = {
    "default":  {
    "skin": "moono-lisa",
    "toolbar_Basic": [["Source", "-", "Bold", "Italic"]],
    "toolbar_Full": [
        [
            "Styles",
            "Format",
            "Bold",
            "Italic",
            "Underline",
            "Strike",
            "SpellChecker",
            "Undo",
            "Redo",
        ],
        ["Link", "Unlink", "Anchor"],
        ["Image", "Flash", "Table", "HorizontalRule"],
        ["TextColor", "BGColor"],
        ["Smiley", "SpecialChar"],
        ["Source"],
    ],
    "toolbar": "Full",
    "height": 291,
    "width": 835,
    "filebrowserWindowWidth": 940,
    "filebrowserWindowHeight": 725,
},
    "my-custom-toolbar": {
        "skin": "moono-lisa",
        "toolbar": CUSTOM_TOOLBAR,
        "toolbarGroups": None,
        "extraPlugins": ",".join(["image2", "codesnippet"]),
        "removePlugins": ",".join(["image"]),
        "codeSnippet_theme": "xcode",
    },
}


CKEDITOR_RESTRICT_BY_DATE = False