"""Configuração do Mini Mural.

Os valores vêm de variáveis de ambiente (A-10, no ARQUITETURA.md). Quando a
variável falta, vale o valor de desenvolvimento. A chave secreta de
desenvolvimento não pode ir para a hospedagem; o tratamento de segredos é do
capítulo 13.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def ambiente(nome, padrao=""):
    """Lê uma variável de ambiente, com o valor de desenvolvimento como padrão."""
    return os.environ.get(nome, padrao)


SECRET_KEY = ambiente("MURAL_SECRET_KEY", "somente-desenvolvimento-nao-use-na-hospedagem")
DEBUG = ambiente("MURAL_DEBUG", "1") == "1"
ALLOWED_HOSTS = ambiente("MURAL_HOSTS", "localhost,127.0.0.1").split(",")

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    # A-05: avisos depende de contas, nunca o contrário.
    "contas",
    "avisos",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": ambiente("MURAL_DB_NAME", "mini_mural_es"),
        "USER": ambiente("MURAL_DB_USER"),
        "PASSWORD": ambiente("MURAL_DB_PASSWORD"),
        "HOST": ambiente("MURAL_DB_HOST"),
        "PORT": ambiente("MURAL_DB_PORT"),
    }
}

# A-04: a conta é um modelo próprio, só com os campos do PROJETO.md.
AUTH_USER_MODEL = "contas.Conta"

# CA-01.3: pelo menos 8 caracteres, e não só números. Nenhuma outra regra.
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {"min_length": 8},
    },
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LOGIN_URL = "/entrar/"

LANGUAGE_CODE = "pt-br"

# DP-06: o banco guarda o instante com fuso, e a página mostra no horário de
# Palmas (CA-04.3).
TIME_ZONE = "America/Araguaina"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
