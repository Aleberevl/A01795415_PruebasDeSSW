import json
import sys
import time


def cargar_archivo_json(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta_archivo}'.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Falló la decodificación del JSON en '{ruta_archivo}'.")
        sys.exit(1)


def calcular_ventas_totales(catalogo_precios, registro_ventas):
    ventas_totales = 0.0
    errores = []

    for venta in registro_ventas:
        try:
            if not all(key in venta for key in ["Product", "Quantity"]):
                errores.append(
                    f"Error: Falta clave en el registro de venta: {venta}"
                )
                continue

            producto = venta["Product"]
            cantidad = venta["Quantity"]

            if not isinstance(producto, str) or not isinstance(
                cantidad, (int, float)
            ):
                errores.append(
                    f"Error: Datos inválidos en el registro de venta: {venta}"
                )
                continue

            if cantidad < 0:
                errores.append(
                    f"Error: Cantidad no puede ser negativa en venta:{venta}"
                )
                continue

            if producto not in catalogo_precios:
                errores.append(
                    f"Error: '{producto}' no se encuentra en el catálogo"
                )
                continue

            precio_por_unidad = catalogo_precios[producto]
            ventas_totales += precio_por_unidad * cantidad

        except KeyError as e:
            errores.append(
                f"Error: Falta la clave {str(e)} en venta: {venta}"
            )
        except TypeError as e:
            errores.append(
                f"Error: Dato inválido en ventas {venta}: {str(e)}"
            )

    return ventas_totales, errores


def escribir_r_en_archivo(ventas_totales, errores, tiempo_transcurrido):
    with open("ResultadosVentas.txt", 'w') as archivo:
        archivo.write(f"Ventas Totales: ${ventas_totales:.2f}\n")
        archivo.write(
            f"Tiempo de Ejecución: {tiempo_transcurrido:.2f} segundos\n"
        )
        if errores:
            archivo.write("\nErrores:\n")
            for error in errores:
                archivo.write(f"- {error}\n")


def main():
    if len(sys.argv) != 3:
        print("computeSales.py catalogoPrecios.json registroVentas.json")
        sys.exit(1)

    archivo_catalogo_precios = sys.argv[1]
    archivo_registro_ventas = sys.argv[2]

    catalogo_precios_data = cargar_archivo_json(archivo_catalogo_precios)
    registro_ventas = cargar_archivo_json(archivo_registro_ventas)

    catalogo_precios = {
        item["title"]: item["price"] for item in catalogo_precios_data
    }

    tiempo_inicio = time.time()

    ventas_totales, errores = calcular_ventas_totales(
        catalogo_precios, registro_ventas
    )

    tiempo_transcurrido = time.time() - tiempo_inicio

    print(f"Ventas Totales: ${ventas_totales:.2f}")
    print(f"Tiempo de Ejecución: {tiempo_transcurrido:.2f} segundos")
    if errores:
        print("\nErrores:")
        for error in errores:
            print(f"- {error}")

    escribir_r_en_archivo(ventas_totales, errores, tiempo_transcurrido)


if __name__ == "__main__":
    main()
