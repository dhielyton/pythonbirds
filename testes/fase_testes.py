# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from unittest.case import TestCase
from atores import Obstaculo, Porco
from fase import Fase


class FaseTestes(TestCase):
    def teste_adicionar_obstaculo(self):
        fase = Fase()
        self.assertListEqual([], fase._obstaculos)
        obstaculo = Obstaculo()
        fase.adicionar_obstaculo(obstaculo)
        self.assertListEqual([obstaculo], fase._obstaculos)

        obstaculo1, obstaculo2 = Obstaculo(), Obstaculo()
        fase.adicionar_obstaculo(obstaculo1, obstaculo2)
        self.assertListEqual([obstaculo, obstaculo1, obstaculo2], fase._obstaculos)
        
    def teste_adicionar_porco(self):
        fase = Fase()
        self.assertListEqual([], fase._porcos)
        porco = Porco()
        fase.adicionar_porco(porco)
        self.assertListEqual([porco], fase._porcos)

        porco1, porco2 = Porco(), Porco()
        fase.adicionar_porco(porco1, porco2)
        self.assertListEqual([porco, porco1, porco2], fase._porcos)

