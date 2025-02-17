#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para buscar y mostrar una reserva por ID.
"""

from modules.reservation_system import ReservationSystem

def main():
    """
    Función principal que busca y muestra una reserva.
    """
    system = ReservationSystem()
    system.retrieve_reservation()

if __name__ == '__main__':
    main()
