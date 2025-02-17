#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para modificar la información de un cliente.
"""

from modules.reservation_system import ReservationSystem

def main():
    """
    Función principal que modifica la información de un cliente.
    """
    system = ReservationSystem()
    system.modify_customer_info()

if __name__ == '__main__':
    main()
