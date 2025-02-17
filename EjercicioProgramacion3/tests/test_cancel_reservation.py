#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pruebas unitarias para el método cancel_reservation() de ReservationSystem.
Se agrega una reserva y se simula su cancelación.
"""

import os
import tempfile
import unittest
from unittest.mock import patch
from modules.reservation import Reservation
from modules.reservation_system import ReservationSystem


class TestCancelReservation(unittest.TestCase):
    """Pruebas unitarias para verificar la cancelación de una reserva."""

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
        # Agregar una reserva para la prueba
        reservation = Reservation(1, 1, 1, "2025-03-01", 3)
        self.system.reservations[1] = reservation

    def tearDown(self):
        """Limpia el entorno de prueba eliminando el directorio temporal."""
        self.temp_dir_obj.cleanup()

    @patch('builtins.input', side_effect=["1"])
    def test_cancel_reservation(self, _mock_input):
        """
        Verifica que al cancelar una reserva, ésta se elimine del sistema.
        """
        self.system.cancel_reservation()
        self.assertNotIn(1, self.system.reservations)


if __name__ == '__main__':
    unittest.main()
