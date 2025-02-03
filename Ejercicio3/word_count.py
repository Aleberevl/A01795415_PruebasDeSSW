"""
Este módulo lee un archivo de texto, cuenta la frecuencia de cada palabra
y guarda los resultados en un archivo de salida llamado WordCountResults.txt.
"""

import sys
import time

def leer_palabras_desde_archivo(ruta_archivo):
    """
    Lee palabras desde un archivo y las almacena en una lista.
    Maneja posibles errores si el archivo no existe.
    """
    palabras = []
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                palabras.extend(linea.strip().split())
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_archivo}.")
        return []
    return palabras

def contar_frecuencia_palabras(palabras):
    """
    Cuenta la frecuencia de cada palabra en la lista dada.
    Convierte las palabras a minúsculas para un conteo uniforme.
    """
    frecuencias = {}
    for palabra in palabras:
        palabra = palabra.lower()
        if palabra not in frecuencias:
            frecuencias[palabra] = 1
        else:
            frecuencias[palabra] += 1
    return frecuencias

def main():
    """
    Función principal del programa.
    Lee el archivo, cuenta la frecuencia de las palabras
    y muestra los resultados en la pantalla y en un archivo de salida.
    """
    if len(sys.argv) != 2:
        print("Uso: python word_count.py archivo_con_datos.txt")
        return

    ruta_archivo = sys.argv[1]
    tiempo_inicio = time.time()

    palabras = leer_palabras_desde_archivo(ruta_archivo)
    if not palabras:
        print("No hay palabras válidas para procesar.")
        return

    frecuencias = contar_frecuencia_palabras(palabras)
    resultados = "Palabra\t\tFrecuencia\n"
    resultados += "-" * 30 + "\n"

    for palabra, frecuencia in frecuencias.items():
        resultados += f"{palabra}\t\t{frecuencia}\n"

    tiempo_transcurrido = time.time() - tiempo_inicio
    resultados += f"\nTiempo transcurrido: {tiempo_transcurrido:.5f} segundos"

    print(resultados)

    with open("WordCountResults.txt", "w", encoding='utf-8') as archivo_resultados:
        archivo_resultados.write(resultados)

if __name__ == "__main__":
    main()
