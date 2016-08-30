# -*- coding: utf-8 -*-
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestPublicarEncuestas(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.FireFox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_publicar_encuesta_historia_1(self):
        """
        Como parte del equipo de DGM, quiero publicar
        una encuesta dentro del blog de datos.gob.mx
        para conocer que datos son prioritarios para los usuarios.
        """
        self.browser.get('http://0.0.0.0:8000/encuestas/administrador/')
        pass

    def test_encuestas_opciones_historia2(self):
        """"
        Quiero ser capaz de incluir votaciones entre
        conjuntos de datos (máximo 4 elementos) para
        que los usuarios del sistema voten por el que
        les interesa más, Así como incluir preguntas
        abiertas donde el usuario podrá escribir libremente su opinión.
        """
        pass

    def test_encuestas_introduccion_historia3(self):
        """
        Quiero poder incluir un texto introductorio
        para explicar el propósito de la encuesta
        u otros temas que puedan interesarle
        al usuario.
        """
        pass
