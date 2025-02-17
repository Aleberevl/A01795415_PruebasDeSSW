#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pruebas unitarias para el método display_customers() de ReservationSystem.
Se captura la salida para verificar que se muestren los datos del cliente.
"""

import os
import tempfile
import unittest
from io import StringIO
from unittest.mock import patch
from modules.customer import Customer
from modules.reservation_system import ReservationSystem


class TestDisplayCustomers(unittest.TestCase):
    """Pruebas unitarias para verificar la funcionalidad de display_customers."""

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
        # Agregar un cliente para la prueba
        self.system.customers[1] = Customer(1, "John Doe", "123456789", "john@example.com")

    def tearDown(self):
        """Limpia el entorno de prueba eliminando el directorio temporal."""
        self.temp_dir_obj.cleanup()

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_customers(self, fake_out):
        """
        Verifica que la función display_customers muestre correctamente los datos del cliente.
        """
        self.system.display_customers()
        output = fake_out.getvalue()
        self.assertIn("John Doe", output)
        self.assertIn("123456789", output)


if __name__ == '__main__':
    unittest.main()
