#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pruebas unitarias para el método create_customer() de ReservationSystem.
"""

import os
import tempfile
import unittest
from unittest.mock import patch
from modules.reservation_system import ReservationSystem


class TestCreateCustomer(unittest.TestCase):
    """Pruebas unitarias para verificar la creación de un cliente en el sistema de reservaciones."""

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

    @patch('builtins.input', side_effect=["John Doe", "123456789", "john@example.com"])
    def test_create_customer(self, _mock_input):
        """
        Verifica que al crear un cliente se agregue correctamente en el sistema.
        """
        self.system.create_customer()
        self.assertIn(1, self.system.customers)
        customer = self.system.customers[1]
        self.assertEqual(customer.nombre, "John Doe")
        self.assertEqual(customer.telefono, "123456789")
        self.assertEqual(customer.email, "john@example.com")


if __name__ == '__main__':
    unittest.main()
