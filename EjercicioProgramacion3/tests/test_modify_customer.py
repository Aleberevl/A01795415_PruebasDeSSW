#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pruebas unitarias para el método modify_customer_info() de ReservationSystem.
Se simula la entrada para modificar un cliente existente.
"""

import os
import tempfile
import unittest
from unittest.mock import patch
from modules.customer import Customer
from modules.reservation_system import ReservationSystem


class TestModifyCustomer(unittest.TestCase):
    """Pruebas unitarias para verificar la modificación de un cliente en el
    sistema de reservaciones.
    """

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
        # Agregar un cliente para la prueba (se divide en varias líneas)
        self.system.customers[1] = Customer(
            1, "John Doe", "123456789", "john@example.com"
        )

    def tearDown(self):
        """Limpia el entorno de prueba eliminando el directorio temporal."""
        self.temp_dir_obj.cleanup()

    @patch('builtins.input', side_effect=[
        "1",
        "Jane Doe",
        "987654321",
        "jane@example.com"
    ])
    def test_modify_customer_info(self, _mock_input):
        """
        Verifica que al modificar la información de un cliente,
        se actualicen correctamente sus datos.
        """
        self.system.modify_customer_info()
        customer = self.system.customers[1]
        self.assertEqual(customer.nombre, "Jane Doe")
        self.assertEqual(customer.telefono, "987654321")
        self.assertEqual(customer.email, "jane@example.com")


if __name__ == '__main__':
    unittest.main()
