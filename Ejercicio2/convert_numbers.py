"""
Este programa convierte números enteros desde un archivo a sus representaciones
en binario y hexadecimal. Los resultados se muestran en pantalla y se guardan
en un archivo llamado ConversionResults.txt.
"""

import sys
import time


def leer_numeros_desde_archivo(ruta_archivo):
    """
    Lee números desde un archivo y los almacena en una lista.
    Ignora líneas con datos inválidos y muestra advertencias.

    :param ruta_archivo: Ruta del archivo de entrada.
    :return: Lista de números válidos.
    """
    numeros = []
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        for numero_linea, linea in enumerate(archivo, start=1):
            try:
                numero = int(linea.strip())
                numeros.append(numero)
            except ValueError:
                print(
                    f"Dato inválido en la línea {numero_linea}: "
                    f"'{linea.strip()}' (ignorado)"
                )
    return numeros


def convertir_binario(numero):
    """
    Convierte un número a su representación en binario.

    :param numero: Número entero a convertir.
    :return: Representación en binario como cadena.
    """
    return bin(numero)[2:]


def convertir_hexadecimal(numero):
    """
    Convierte un número a su representación en hexadecimal.

    :param numero: Número entero a convertir.
    :return: Representación en hexadecimal como cadena.
    """
    return hex(numero)[2:]


def main():
    """
    Función principal del programa.
    Lee números desde un archivo, los convierte a binario y hexadecimal,
    mide el tiempo de ejecución y guarda los resultados.
    """
    if len(sys.argv) != 2:
        print("Uso: python convert_numbers.py archivoConDatos.txt")
        return

    ruta_archivo = sys.argv[1]
    tiempo_inicio = time.time()

    numeros = leer_numeros_desde_archivo(ruta_archivo)
    if not numeros:
        print("No hay números válidos para procesar.")
        return

    resultados = "Número Decimal\tBinario\t\tHexadecimal\n" + "-" * 50 + "\n"

    for numero in numeros:
        binario = convertir_binario(numero)
        hexadecimal = convertir_hexadecimal(numero)
        resultados += f"{numero}\t\t{binario}\t\t{hexadecimal}\n"

    tiempo_transcurrido = time.time() - tiempo_inicio
    resultados += f"\nTiempo transcurrido: {tiempo_transcurrido:.5f} segundos"

    print(resultados)

    with open("ConversionResults.txt", "w", encoding="utf-8") as archivo_resultados:
        archivo_resultados.write(resultados)


if __name__ == "__main__":
    main()
