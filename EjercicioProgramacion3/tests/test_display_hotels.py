#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pruebas unitarias para el método display_hotels() de ReservationSystem.
Se captura la salida estándar para verificar la información mostrada.
"""

import os
import tempfile
import unittest
from io import StringIO
from unittest.mock import patch
from modules.hotel import Hotel
from modules.reservation_system import ReservationSystem


class TestDisplayHotels(unittest.TestCase):
    """Pruebas unitarias para verificar la función display_hotels."""

    def setUp(self):
        """Configura el entorno de prueba utilizando un directorio temporal."""
        self.temp_dir_obj = tempfile.TemporaryDirectory()  # pylint: disable=consider-using-with
        self.temp_dir = self.temp_dir_obj.name
        self.hotels_file = os.path.join(self.temp_dir, "hotels.json")
        self.customers_file = os.path.join(self.temp_dir, "customers.json")
        self.reservations_file = os.path.join(self.temp_dir, "reservations.json")
        self.system = ReservationSystem(
            hotels_file=self.hotels_file,
            customers_file=self.customers_file,
            reservations_file=self.reservations_file
        )
        # Agregar un hotel para mostrar
        self.system.hotels[1] = Hotel(1, "Test Hotel", "Test Location", 10, 100.0)

    def tearDown(self):
        """Limpia el entorno de prueba eliminando el directorio temporal."""
        self.temp_dir_obj.cleanup()

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_hotels(self, fake_out):
        """
        Verifica que la función display_hotels muestre correctamente la información del hotel.
        """
        self.system.display_hotels()
        output = fake_out.getvalue()
        self.assertIn("Test Hotel", output)
        self.assertIn("Test Location", output)


if __name__ == '__main__':
    unittest.main()
