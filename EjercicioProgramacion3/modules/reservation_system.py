#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo que define la clase ReservationSystem.
Contiene la lógica de negocio para crear y gestionar hoteles, clientes y reservas.
"""

import json
import os
from datetime import datetime
from modules.hotel import Hotel
from modules.customer import Customer
from modules.reservation import Reservation


class ReservationSystem:
    """Clase que gestiona el sistema de reservaciones, incluyendo hoteles, clientes y reservas."""

    def __init__(self,
                 hotels_file='hotels.json',
                 customers_file='customers.json',
                 reservations_file='reservations.json'):
        """
        Inicializa el sistema de reservaciones.

        Args:
            hotels_file (str): Ruta del archivo de hoteles.
            customers_file (str): Ruta del archivo de clientes.
            reservations_file (str): Ruta del archivo de reservaciones.
        """
        self.hotels_file = hotels_file
        self.customers_file = customers_file
        self.reservations_file = reservations_file

        self.hotels = {}
        self.customers = {}
        self.reservations = {}

        self.load_data()

    def load_data(self):
        """Carga los datos de hoteles, clientes y reservaciones desde los archivos JSON."""
        self.hotels = self._load_json(self.hotels_file, 'hotels')
        self.customers = self._load_json(self.customers_file, 'customers')
        self.reservations = self._load_json(self.reservations_file, 'reservations')

    def save_data(self):
        """Guarda los datos de hoteles, clientes y reservaciones en los archivos JSON."""
        self._save_json(self.hotels_file, self.hotels)
        self._save_json(self.customers_file, self.customers)
        self._save_json(self.reservations_file, self.reservations)

    def _load_json(self, file_path, data_type):
        """
        Carga datos de un archivo JSON y los convierte en objetos según el tipo.

        Args:
            file_path (str): Ruta del archivo.
            data_type (str): Tipo de datos ('hotels', 'customers' o 'reservations').

        Returns:
            dict: Diccionario de objetos cargados.
        """
        if not os.path.exists(file_path):
            return {}
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data_dict = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            data_dict = {}

        if data_type == 'hotels':
            return {int(k): Hotel.from_dict(v) for k, v in data_dict.items()}
        if data_type == 'customers':
            return {int(k): Customer.from_dict(v) for k, v in data_dict.items()}
        if data_type == 'reservations':
            return {int(k): Reservation.from_dict(v) for k, v in data_dict.items()}
        return {}

    def _save_json(self, file_path, data_dict):
        """
        Guarda un diccionario de objetos en un archivo JSON.

        Args:
            file_path (str): Ruta del archivo.
            data_dict (dict): Diccionario de objetos a guardar.
        """
        dict_to_save = {str(key): obj.to_dict() for key, obj in data_dict.items()}
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(dict_to_save, file, ensure_ascii=False, indent=4)

    def create_hotel(self):
        """Crea un nuevo hotel solicitando información al usuario."""
        if self.hotels:
            new_id = max(self.hotels.keys()) + 1
        else:
            new_id = 1
        nombre = input("Nombre del hotel: ")
        ubicacion = input("Ubicación del hotel: ")
        try:
            num_habitaciones = int(input("Número de habitaciones: "))
        except ValueError:
            print("Valor inválido, se asigna 0 habitaciones.")
            num_habitaciones = 0
        try:
            precio_por_noche = float(input("Precio por noche: "))
        except ValueError:
            print("Valor inválido, se asigna 0.0 como precio.")
            precio_por_noche = 0.0
        hotel = Hotel(new_id, nombre, ubicacion, num_habitaciones, precio_por_noche)
        self.hotels[new_id] = hotel
        self.save_data()
        print(f"Hotel '{nombre}' creado con ID {new_id}.\n")

    def display_hotels(self):
        """Muestra la lista de hoteles registrados."""
        if not self.hotels:
            print("No hay hoteles registrados.\n")
            return
        print("=== Lista de Hoteles ===")
        for hotel in self.hotels.values():
            print(f"ID: {hotel.hotel_id}")
            print(f"Nombre: {hotel.nombre}")
            print(f"Ubicación: {hotel.ubicacion}")
            print(f"Habitaciones: {hotel.num_habitaciones}")
            print(f"Precio/Noche: {hotel.precio_por_noche}")
            print("------------------------")
        print()

    def create_customer(self):
        """Crea un nuevo cliente solicitando información al usuario."""
        if self.customers:
            new_id = max(self.customers.keys()) + 1
        else:
            new_id = 1
        nombre = input("Nombre del cliente: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        customer = Customer(new_id, nombre, telefono, email)
        self.customers[new_id] = customer
        self.save_data()
        print(f"Cliente '{nombre}' creado con ID {new_id}.\n")

    def display_customers(self):
        """Muestra la lista de clientes registrados."""
        if not self.customers:
            print("No hay clientes registrados.\n")
            return
        print("=== Lista de Clientes ===")
        for customer in self.customers.values():
            print(f"ID: {customer.customer_id}")
            print(f"Nombre: {customer.nombre}")
            print(f"Teléfono: {customer.telefono}")
            print(f"Email: {customer.email}")
            print("------------------------")
        print()

    def create_reservation(self):
        """Crea una nueva reservación solicitando información al usuario."""
        if self.reservations:
            new_id = max(self.reservations.keys()) + 1
        else:
            new_id = 1
        try:
            customer_id = int(input("ID del cliente: "))
            if customer_id not in self.customers:
                print("Cliente no encontrado.")
                return
        except ValueError:
            print("ID de cliente inválido.")
            return
        try:
            hotel_id = int(input("ID del hotel: "))
            if hotel_id not in self.hotels:
                print("Hotel no encontrado.")
                return
        except ValueError:
            print("ID de hotel inválido.")
            return
        fecha_check_in = input("Fecha de check-in (YYYY-MM-DD): ")
        try:
            datetime.strptime(fecha_check_in, "%Y-%m-%d")
        except ValueError:
            print("Fecha inválida. Formato correcto: YYYY-MM-DD.")
            return
        try:
            noches_reserva = int(input("Cantidad de noches: "))
        except ValueError:
            print("Valor inválido, se asigna 1 noche por defecto.")
            noches_reserva = 1
        reservation = Reservation(new_id, customer_id, hotel_id, fecha_check_in, noches_reserva)
        self.reservations[new_id] = reservation
        self.save_data()
        print(f"Reserva creada con ID {new_id}.\n")

    def display_reservations(self):
        """Muestra la lista de reservaciones registradas."""
        if not self.reservations:
            print("No hay reservas registradas.\n")
            return
        print("=== Lista de Reservas ===")
        for reservation in self.reservations.values():
            print(f"Reserva ID: {reservation.reservation_id}")
            print(f"Cliente ID: {reservation.customer_id}")
            print(f"Hotel ID: {reservation.hotel_id}")
            print(f"Fecha Check-In: {reservation.fecha_check_in}")
            print(f"Noches: {reservation.noches_reserva}")
            print("------------------------")
        print()

    def modify_customer_info(self):
        """Modifica la información de un cliente registrado."""
        try:
            customer_id = int(input("Ingrese el ID del cliente a modificar: "))
        except ValueError:
            print("ID inválido.")
            return
        if customer_id not in self.customers:
            print("No existe un cliente con ese ID.\n")
            return
        customer = self.customers[customer_id]
        print(f"Modificando datos del cliente '{customer.nombre}' (ID: {customer_id})")
        nuevo_nombre = input(f"Nombre (actual: {customer.nombre}): ")
        nuevo_telefono = input(f"Teléfono (actual: {customer.telefono}): ")
        nuevo_email = input(f"Email (actual: {customer.email}): ")
        if nuevo_nombre.strip():
            customer.nombre = nuevo_nombre
        if nuevo_telefono.strip():
            customer.telefono = nuevo_telefono
        if nuevo_email.strip():
            customer.email = nuevo_email
        self.customers[customer_id] = customer
        self.save_data()
        print("Información del cliente actualizada.\n")

    def cancel_reservation(self):
        """Cancela una reservación registrada."""
        try:
            reservation_id = int(input("Ingrese el ID de la reserva a cancelar: "))
        except ValueError:
            print("ID inválido.")
            return
        if reservation_id not in self.reservations:
            print("No existe una reserva con ese ID.\n")
            return
        del self.reservations[reservation_id]
        self.save_data()
        print("Reserva cancelada exitosamente.\n")

    def retrieve_reservation(self):
        """Busca y muestra la información de una reservación por su ID."""
        try:
            reservation_id = int(input("Ingrese el ID de la reserva: "))
        except ValueError:
            print("ID inválido.")
            return
        if reservation_id not in self.reservations:
            print("No existe una reserva con ese ID.\n")
            return
        reservation = self.reservations[reservation_id]
        print("=== Reserva Encontrada ===")
        print(f"ID: {reservation.reservation_id}")
        print(f"Cliente ID: {reservation.customer_id}")
        print(f"Hotel ID: {reservation.hotel_id}")
        print(f"Fecha Check-In: {reservation.fecha_check_in}")
        print(f"Noches: {reservation.noches_reserva}")
        print("--------------------------\n")


def main_menu():
    """Muestra el menú interactivo del sistema de reservaciones."""
    system = ReservationSystem()
    while True:
        print("=== SISTEMA DE RESERVAS ===")
        print("1. Crear Hotel")
        print("2. Mostrar Hoteles")
        print("3. Crear Cliente")
        print("4. Mostrar Clientes")
        print("5. Crear Reserva")
        print("6. Mostrar Reservas")
        print("7. Modificar Cliente")
        print("8. Cancelar Reserva")
        print("9. Buscar Reserva por ID")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            system.create_hotel()
        elif opcion == '2':
            system.display_hotels()
        elif opcion == '3':
            system.create_customer()
        elif opcion == '4':
            system.display_customers()
        elif opcion == '5':
            system.create_reservation()
        elif opcion == '6':
            system.display_reservations()
        elif opcion == '7':
            system.modify_customer_info()
        elif opcion == '8':
            system.cancel_reservation()
        elif opcion == '9':
            system.retrieve_reservation()
        elif opcion == '0':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.\n")


if __name__ == "__main__":
    main_menu()
