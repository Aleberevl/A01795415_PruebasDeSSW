#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo que define la clase Hotel.
"""



class Hotel:
    """Clase que representa un hotel con sus atributos básicos."""

    def __init__(self, hotel_id, nombre, ubicacion, num_habitaciones, precio_por_noche):  # pylint: disable=too-many-arguments, too-many-positional-arguments
        """
        Inicializa una nueva instancia de Hotel.

        Args:
            hotel_id (int): Identificador único del hotel.
            nombre (str): Nombre del hotel.
            ubicacion (str): Ubicación del hotel.
            num_habitaciones (int): Número de habitaciones.
            precio_por_noche (float): Precio por noche.
        """
        self.hotel_id = hotel_id
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.num_habitaciones = num_habitaciones
        self.precio_por_noche = precio_por_noche

    def to_dict(self):
        """
        Convierte la instancia de Hotel a un diccionario.

        Returns:
            dict: Diccionario con los atributos del hotel.
        """
        return {
            "hotel_id": self.hotel_id,
            "nombre": self.nombre,
            "ubicacion": self.ubicacion,
            "num_habitaciones": self.num_habitaciones,
            "precio_por_noche": self.precio_por_noche
        }

    @classmethod
    def from_dict(cls, data):
        """
        Crea una instancia de Hotel a partir de un diccionario.

        Args:
            data (dict): Diccionario que contiene los datos del hotel.

        Returns:
            Hotel: Una nueva instancia de Hotel.
        """
        return cls(
            data["hotel_id"],
            data["nombre"],
            data["ubicacion"],
            data["num_habitaciones"],
            data["precio_por_noche"]
        )


if __name__ == "__main__":
    # Ejemplo de uso: crear una instancia y mostrar el diccionario
    hotel = Hotel(1, "Hotel Ejemplo", "Ciudad Ejemplo", 50, 120.0)
    print(hotel.to_dict())
