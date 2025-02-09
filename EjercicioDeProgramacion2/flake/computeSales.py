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
            nombre_producto = venta["producto"]
            cantidad = venta["cantidad"]

            if nombre_producto not in catalogo_precios:
                errores.append(f"Error: El producto '{nombre_producto}' no se encuentra en el catálogo de precios.")
                continue

            precio_por_unidad = catalogo_precios[nombre_producto]
            ventas_totales += precio_por_unidad * cantidad

        except KeyError as e:
            errores.append(f"Error: Falta la clave {str(e)} en el registro de ventas: {venta}")
        except TypeError as e:
            errores.append(f"Error: Tipo de dato inválido en el registro de ventas {venta}: {str(e)}")

    return ventas_totales, errores


def escribir_resultados_en_archivo(ventas_totales, errores, tiempo_transcurrido):
    with open("ResultadosVentas.txt", 'w') as archivo:
        archivo.write(f"Ventas Totales: ${ventas_totales:.2f}\n")
        archivo.write(f"Tiempo de Ejecución: {tiempo_transcurrido:.2f} segundos\n")
        if errores:
            archivo.write("\nErrores:\n")
            for error in errores:
                archivo.write(f"- {error}\n")


def main():
    if len(sys.argv) != 3:
        print("Uso: python computeSales.py catalogoPrecios.json registroVentas.json")
        sys.exit(1)

    archivo_catalogo_precios = sys.argv[1]
    archivo_registro_ventas = sys.argv[2]

    # Cargar archivos de entrada
    catalogo_precios = cargar_archivo_json(archivo_catalogo_precios)
    registro_ventas = cargar_archivo_json(archivo_registro_ventas)

    # Iniciar medición del tiempo de ejecución
    tiempo_inicio = time.time()

    # Calcular ventas totales y recopilar errores
    ventas_totales, errores = calcular_ventas_totales(catalogo_precios, registro_ventas)

    # Calcular tiempo transcurrido
    tiempo_transcurrido = time.time() - tiempo_inicio

    # Mostrar y guardar resultados
    print(f"Ventas Totales: ${ventas_totales:.2f}")
    print(f"Tiempo de Ejecución: {tiempo_transcurrido:.2f} segundos")
    if errores:
        print("\nErrores:")
        for error in errores:
            print(f"- {error}")

    escribir_resultados_en_archivo(ventas_totales, errores, tiempo_transcurrido)


if __name__ == "__main__":
    main()
