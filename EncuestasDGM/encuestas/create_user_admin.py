# -*- coding: utf-8 -*-
"""
Script de creacion de usuario administrador
inicial de la aplicacion
"""
import os
import sys
import datetime
from django.core.wsgi import get_wsgi_application

CURRENT = os.path.dirname(__file__)
sys.path.insert(0, os.path.realpath(os.path.join(CURRENT, '../')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EncuestasDGM.settings")
application = get_wsgi_application()

from django.contrib.auth.models import User

if __name__ == "__main__":
    print "Creacion de administrador"
    admin = User.objects.create_user(username="adminEncuestas", password="pass{0}".format(datetime.datetime.now().strftime('%Y%m%d')))
    admin.is_staff = True
    print "Usuario: adminEncuestas"
    admin.save()
