"""
Django settings for codellipse project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f3xz#8_@4t%n!(h0l-8+=$&pb_zifm6#i*(z8289gvm^dxgoth'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['codellipse.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'user.apps.UserConfig',
    'course.apps.CourseConfig',
    'django.contrib.humanize',
    'crispy_forms',
    'social_django',
    'ckeditor',
    'ckeditor_uploader',
]


CKEDITOR_UPLOAD_PATH = "uploads/"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'codellipse.urls'


# social authentications backends 

AUTHENTICATION_BACKENDS = [
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.twitter.TwitterOAuth',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'codellipse.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'codellipse_db.sqlite3'),
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'codellipse_db',
#         'USER' : 'root',
#         'PASSWORD' : '',
#         'HOST' : '127.0.0.1',
#         'PORT' : '3306',
#         'OPTIONS' : {
#             'sql_mode' : 'traditional',
#         }
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'codellipse',
#         'USER': 'postgres',
#         'PASSWORD': 'admin@123',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd6tcee5b7ee90s',
        'USER': 'trpbtvnkjdixar',
        'PASSWORD': '2a6240a45d7f75d9d1eaf21a8d9c72e07cdc9318ffeb0047f7b64db601f6d8d8',
        'HOST': 'ec2-54-225-116-36.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# Here instead of making the python interpreter to look for static folder in the packages
# we want it to be look for in container 

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

#On the server, run collectstatic to copy all the static files into STATIC_ROOT.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# to get the crispy form feature we need to configure the bootstrap 4
CRISPY_TEMPLATE_PACK = 'bootstrap4'


# Password reset Email connection
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'tak2prakash@gmail.com'
EMAIL_HOST_PASSWORD = 'ycovcxknzccagqdl'

# Media root will set a base directory for uploaded file in system no matter what OS
# we're working with
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# it will locate the media file when we fetch the picture.
MEDIA_URL = '/media/'


LOGIN_REDIRECT_URL = 'post_list'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '865845165849-oncqcl8bicke9dmq9m0jlam71lugn6tq.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH_SECRET = 'iP1CxqTdMaZs5jJITGZJ0K23'


SOCIAL_AUTH_TWITTER_KEY = 'y9COCBd3WIYyWzt9C2XubVeSu'
SOCIAL_AUTH_TWITTER_SECRET = 'KpSEn5LanLSzHKOCHyykqSQ1WUDjR2Dsp9t4Ymik8EJj3XeU3W'

SOCIAL_AUTH_GITHUB_KEY = '0b6bed4f2b42ab0a567d'
SOCIAL_AUTH_GITHUB_KEY = '50afd226e188e24a559a2d233868b1d71cd57aff'


