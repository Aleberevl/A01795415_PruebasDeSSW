#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para mostrar la lista de reservas.
"""

from modules.reservation_system import ReservationSystem

def main():
    """
    Función principal que muestra la lista de reservas utilizando el sistema de reservaciones.
    """
    system = ReservationSystem()
    system.display_reservations()

if __name__ == '__main__':
    main()
