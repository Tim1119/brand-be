from pathlib import Path
import os
import logging.config
import logging
from django.utils.log import DEFAULT_LOGGING
import environ
from datetime import timedelta


# ---------------- BASE_PATH ------------------------
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# ----------------- SETTING ENVIROMENT PATH ---------------
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# --------------------SECURITY-OPTIONS--------------------------
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG').split(" ")
ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(" ")


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
    "drf_standardized_errors",
]

LOCAL_APPS = [

]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'brand.urls'

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

WSGI_APPLICATION = 'brand.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# ----------------------- LANGUAGES AND TIMEZONE -----------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Lagos'
USE_I18N = True
USE_TZ = True


# ----------------------- STATIC AND  MEDIA PATHS -----------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'staticfiles')]
MEDIA_URL = "/mediafiles/"
MEDIA_ROOT = BASE_DIR / "mediafiles"


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --------------------------------------------------------------LOGGERS --------------------------------------------------------
logger = logging.getLogger(__name__)

LOG_LEVEL = "INFO"

logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "console": {
                "format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
            },
            "file": {"format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"},
            "django.server": DEFAULT_LOGGING["formatters"]["django.server"],
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "console",
            },
            "file": {
                "level": "INFO",
                "class": "logging.FileHandler",
                "formatter": "file",
                "filename": "logs/brand.logs",
            },
            "django.server": DEFAULT_LOGGING["handlers"]["django.server"],
        },
        "loggers": {
            "": {"level": "INFO", "handlers": ["console", "file"], "propagate": False},
            "apps": {"level": "INFO", "handlers": ["console"], "propagate": False},
            "django.server": DEFAULT_LOGGING["loggers"]["django.server"],
        },
    }
)

# --------------------------------------DRF SETTINGS ----------------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    "EXCEPTION_HANDLER": "drf_standardized_errors.handler.exception_handler",
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        # 'project_utils.success_json_response.SuccessJsonResponse',
    ),
}

DRF_STANDARDIZED_ERRORS = {
    "ENABLE_IN_DEBUG_FOR_UNHANDLED_EXCEPTIONS": True,
    "EXCEPTION_FORMATTER_CLASS": "project_utils.exception_formatter.MyExceptionFormatter"
    }

# --------------------------------------SIMPLEJWT SETTINGS ---------------------------
SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": (
        "Bearer",
        "JWT",
    ),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=820),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "SIGNING_KEY": env("SIGNING_KEY"),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}

# --------------------------------------DJOSER SETTINGS ---------------------------

# DJOSER = {
#     "LOGIN_FIELD": "email",
#     "USER_CREATE_PASSWORD_RETYPE": True,
#     "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
#     "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
#     "SEND_CONFIRMATION_EMAIL": True,
#     "PASSWORD_RESET_CONFIRM_URL": "password/reset/confirm/{uid}/{token}",
#     "SET_PASSWORD_RETYPE": True,
#     "PASSWORD_RESET_CONFIRM_RETYPE": True,
#     "USERNAME_RESET_CONFIRM_URL": "email/reset/confirm/{uid}/{token}",
#     "ACTIVATION_URL": "activate/{uid}/{token}",
#     "SEND_ACTIVATION_EMAIL": True,
#     "SERIALIZERS": {
#         "user_create": "apps.accounts.serializers.CreateUserSerializer,",
#         "user": "apps.accounts.serializers.UserSerializer",
#         "current_user": "apps.accounts.serializers.UserSerializer",
#         "user_delete": "djoser.serializers.UserDeleteSerializer",
#     },
# }