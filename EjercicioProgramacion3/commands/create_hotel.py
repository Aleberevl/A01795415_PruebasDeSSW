#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para crear un hotel.
"""

from modules.reservation_system import ReservationSystem

def main():
    """
    Función principal que crea un hotel utilizando el sistema de reservaciones.
    """
    system = ReservationSystem()
    system.create_hotel()

if __name__ == '__main__':
    main()
