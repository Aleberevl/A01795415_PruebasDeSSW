#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para crear una reserva.
"""

from modules.reservation_system import ReservationSystem

def main():
    """
    Función principal que crea una reserva utilizando el sistema de reservaciones.
    """
    system = ReservationSystem()
    system.create_reservation()

if __name__ == '__main__':
    main()
