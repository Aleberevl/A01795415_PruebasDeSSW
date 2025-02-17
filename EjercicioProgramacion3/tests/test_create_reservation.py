#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pruebas unitarias para el método create_reservation() de ReservationSystem.
"""

import os
import tempfile
import unittest
from unittest.mock import patch
from modules.hotel import Hotel
from modules.customer import Customer
from modules.reservation_system import ReservationSystem


class TestCreateReservation(unittest.TestCase):
    """Pruebas unitarias para verificar la creación de una reserva."""

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
        # Pre-cargar un hotel y un cliente necesarios para la reserva
        self.system.hotels[1] = Hotel(1, "Test Hotel", "Location", 10, 100.0)
        self.system.customers[1] = Customer(1, "Test Customer", "3531258765", "usuario@gmail.com")

    def tearDown(self):
        """Limpia el entorno de prueba eliminando el directorio temporal."""
        self.temp_dir_obj.cleanup()

    @patch('builtins.input', side_effect=["1", "1", "2025-03-01", "2"])
    def test_create_reservation(self, _mock_input):
        """
        Verifica que al crear una reserva se agregue correctamente al sistema.
        """
        self.system.create_reservation()
        self.assertIn(1, self.system.reservations)
        reservation = self.system.reservations[1]
        self.assertEqual(reservation.customer_id, 1)
        self.assertEqual(reservation.hotel_id, 1)
        self.assertEqual(reservation.fecha_check_in, "2025-03-01")
        self.assertEqual(reservation.noches_reserva, 2)


if __name__ == '__main__':
    unittest.main()
