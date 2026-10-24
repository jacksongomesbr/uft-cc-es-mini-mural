"""Ponto de entrada ASGI do Mini Mural.

O servidor de produção que vai usá-lo é decidido no capítulo 14 (A-11).
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_asgi_application()
