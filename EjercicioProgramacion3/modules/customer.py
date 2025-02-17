#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo que define la clase Customer.
"""

class Customer:
    """Clase que representa un cliente."""

    def __init__(self, customer_id, nombre, telefono, email):
        """
        Inicializa una instancia de Customer.

        Args:
            customer_id (int): Identificador único del cliente.
            nombre (str): Nombre del cliente.
            telefono (str): Número de teléfono.
            email (str): Correo electrónico.
        """
        self.customer_id = customer_id
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def to_dict(self):
        """
        Convierte la instancia de Customer a un diccionario.

        Returns:
            dict: Diccionario con los datos del cliente.
        """
        return {
            "customer_id": self.customer_id,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, data):
        """
        Crea una instancia de Customer a partir de un diccionario.

        Args:
            data (dict): Diccionario con la información del cliente.

        Returns:
            Customer: Instancia de Customer creada a partir de data.
        """
        return cls(
            data["customer_id"],
            data["nombre"],
            data["telefono"],
            data["email"]
        )
