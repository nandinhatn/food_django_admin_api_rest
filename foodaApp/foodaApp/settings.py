"""
Django settings for foodaApp project.

Generated by 'django-admin startproject' using Django 4.1.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import pymysql
import logging
logger = logging.getLogger(__name__)
from django.utils.translation import gettext_lazy as _
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s5wj&sugddn80$9!2bbjup+rl&zu7v(m+%!&m16s5=e-q)^)%5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
MEDIA_URL = '/imagens/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
ALLOWED_HOSTS = ['*']
# CORS_ALLOWED_ORIGINS = [
#     "*",  # Origem do seu aplicativo React
    
# ]
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True


CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]
USE_I18N = True
LANGUAGES = (
  ('pt-br', _('Brazilian Portuguese')),
    ('en', _('English')),
)

ROOT_DIR = Path.cwd()
APPS_DIR = ROOT_DIR / "apps"
USE_L10N = True
# Application definition
CORS_ORIGIN_WHITELIST = (
  'http://localhost:3000',
)

INSTALLED_APPS = [

    'admin_interface',
    'corsheaders',
    'flat_responsive',
    'translation_manager',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',    
    'meususuarios',
     'rest_framework',
     'produtos',
     'categorias',
     'restaurante',
     'faixas',
     'pedidos',
]

ADMIN_INTERFACE_SETTINGS = {
    'theme': 'gerenciador',      # Escolha o tema desejado
    'title': 'My Admin Panel', # Título personalizado para o painel de administração
   
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
     "django.middleware.security.SecurityMiddleware", 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'foodaApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'foodaApp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'poppymidiacom_food',
#         'USER': 'poppymidiacom_fernanda',
#         'PASSWORD':'Fuvest@4050',
#         'HOST': '65.181.111.132',
#         'PORT': '3306',
#         'OPTIONS':{
#             'charset': 'utf8mb4'
#         }

#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'food2',  # Nome do seu banco de dados no MongoDB
#         'CLIENT': {
#             'host': 'localhost',  # Endereço do host do MongoDB
#             'port': 27017,        # Porta padrão do MongoDB
#             # Outras configurações do cliente MongoDB, se necessário
#         },
#     }
# }

AUTH_USER_MODEL = 'meususuarios.CustomUser'

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]
}