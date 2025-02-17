#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo que define la clase Reservation.
"""

class Reservation:
    """Clase que representa una reserva."""

    def __init__(self, reservation_id, customer_id, hotel_id, fecha_check_in, noches_reserva):  # pylint: disable=too-many-arguments, too-many-positional-arguments
        """
        Inicializa una nueva reserva.

        Args:
            reservation_id (int): Identificador único de la reserva.
            customer_id (int): Identificador del cliente.
            hotel_id (int): Identificador del hotel.
            fecha_check_in (str): Fecha de check-in en formato YYYY-MM-DD.
            noches_reserva (int): Número de noches de la reserva.
        """
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id
        self.fecha_check_in = fecha_check_in
        self.noches_reserva = noches_reserva

    def to_dict(self):
        """
        Convierte la instancia de Reservation en un diccionario.

        Returns:
            dict: Diccionario con los atributos de la reserva.
        """
        return {
            "reservation_id": self.reservation_id,
            "customer_id": self.customer_id,
            "hotel_id": self.hotel_id,
            "fecha_check_in": self.fecha_check_in,
            "noches_reserva": self.noches_reserva
        }

    @classmethod
    def from_dict(cls, data):
        """
        Crea una instancia de Reservation a partir de un diccionario.

        Args:
            data (dict): Diccionario que contiene los datos de la reserva.

        Returns:
            Reservation: Una nueva instancia de Reservation.
        """
        return cls(
            data["reservation_id"],
            data["customer_id"],
            data["hotel_id"],
            data["fecha_check_in"],
            data["noches_reserva"]
        )


if __name__ == "__main__":
    # Ejemplo de uso: crear una reserva y mostrar su representación en diccionario.
    reserva = Reservation(1, 100, 10, "2025-03-01", 3)
    print(reserva.to_dict())
