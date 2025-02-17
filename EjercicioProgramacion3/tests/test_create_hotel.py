#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pruebas unitarias para el método create_hotel() de ReservationSystem.
"""

import os
import tempfile
import unittest
from unittest.mock import patch
from modules.reservation_system import ReservationSystem


class TestCreateHotel(unittest.TestCase):
    """Pruebas unitarias para verificar la creación de un hotel en el sistema de reservaciones."""

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

    def tearDown(self):
        """Limpia el entorno de prueba eliminando el directorio temporal."""
        self.temp_dir_obj.cleanup()

    @patch('builtins.input', side_effect=["Hotel Test", "Test Location", "20", "200.0"])
    def test_create_hotel(self, _mock_input):
        """
        Verifica que al crear un hotel se agregue correctamente en el sistema.
        """
        self.system.create_hotel()
        self.assertIn(1, self.system.hotels)
        hotel = self.system.hotels[1]
        self.assertEqual(hotel.nombre, "Hotel Test")
        self.assertEqual(hotel.ubicacion, "Test Location")
        self.assertEqual(hotel.num_habitaciones, 20)
        self.assertEqual(hotel.precio_por_noche, 200.0)


if __name__ == '__main__':
    unittest.main()
