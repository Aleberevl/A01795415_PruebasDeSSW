#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pruebas unitarias para el método retrieve_reservation() de ReservationSystem.
Se captura la salida para verificar que se muestre la información de la reserva.
"""

import os
import tempfile
import unittest
from io import StringIO
from unittest.mock import patch
from modules.reservation import Reservation
from modules.reservation_system import ReservationSystem


class TestRetrieveReservation(unittest.TestCase):
    """Pruebas unitarias para verificar la función retrieve_reservation."""

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
    @patch('sys.stdout', new_callable=StringIO)
    def test_retrieve_reservation(self, fake_out, _mock_input):
        """
        Verifica que al buscar una reserva, se muestre correctamente la información.
        """
        self.system.retrieve_reservation()
        output = fake_out.getvalue()
        self.assertIn("Reserva Encontrada", output)
        self.assertIn("2025-03-01", output)


if __name__ == '__main__':
    unittest.main()
