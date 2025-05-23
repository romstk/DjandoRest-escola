"""
Django settings for setup project.

Generated by 'django-admin startproject' using Django 5.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e#%n0z2lew+)9oam3dc@_r&p#++cy%n64_(t!^p#4iteev=7vd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'escola',
    'rest_framework',
    'django_filters',
    'drf_yasg',
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

ROOT_URLCONF = 'setup.urls'

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

WSGI_APPLICATION = 'setup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Configuração do REST_FRAMEWORK para autencicação
# Definindo a autenticação como BasicAuthentication e a permissão como IsAuthenticated  
REST_FRAMEWORK = {
    # Nesta aplicação definimos que todos os acessos deverão ser fetios por usuário autenticado, então definimos direto aqui no settings.py, caso queira personalizar posso criar permissões dentro da cada view. 
    # Configuração de autenticação
    # Isso significa que a autenticação será feita usando o BasicAuthentication e a SessionAuthentication.
    # BasicAuthentication é um método de autenticação simples que usa o nome de usuário e a senha do usuário.
    # SessionAuthentication é um método de autenticação que usa a sessão do usuário para autenticar o usuário.
    # Isso significa que o usuário deve estar autenticado para acessar a API.
   
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    # Configuração de permissão
    # Isso significa que apenas usuários autenticados podem acessar a API.
    # Se você quiser permitir que usuários anônimos acessem a API, você pode usar a permissão IsAuthenticatedOrReadOnly.
    # Isso significa que usuários anônimos podem acessar a API, mas apenas para métodos de leitura (GET, HEAD, OPTIONS).
    # Para métodos de escrita (POST, PUT, PATCH, DELETE), eles precisam estar autenticados.
    # Vamos definir as permissões de usuário para que as permissões sejam as concedidas no Django Admin para cada usuário
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissions',
    ],
    # Configuração de paginação
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.QueryParameterVersioning',

    # Configurando o throttle, limites de requisições  
    # Isso é útil para evitar que um usuário faça muitas requisições em um curto período de tempo. 
    # Por exemplo, se você quiser limitar um usuário a 100 requisições por dia, você pode usar o seguinte código:    
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    # Definindo os limites de requisições por usuários logados e anônimos    
    'DEFAULT_THROTTLE_RATES': {
        'anon': '20/day',
        'user': '50/day'
    }
}