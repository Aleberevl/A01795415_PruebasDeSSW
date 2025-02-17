#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para crear un cliente.
"""

from modules.reservation_system import ReservationSystem

def main():
    """
    Función principal que crea un cliente utilizando el sistema de reservaciones.
    """
    system = ReservationSystem()
    system.create_customer()

if __name__ == '__main__':
    main()
