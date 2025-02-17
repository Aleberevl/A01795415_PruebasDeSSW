#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para cancelar una reserva.
"""

from modules.reservation_system import ReservationSystem

def main():
    """
    Función principal que cancela una reserva utilizando el sistema de reservaciones.
    """
    system = ReservationSystem()
    system.cancel_reservation()

if __name__ == '__main__':
    main()
