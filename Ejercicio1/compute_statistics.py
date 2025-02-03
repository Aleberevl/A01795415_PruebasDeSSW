"""
Módulo: compute_statistics.py
Descripción: Este programa calcula estadísticas descriptivas básicas 
(media, mediana, moda, varianza y desviación estándar) a partir de un archivo de números.
Los resultados se muestran en la consola y se guardan en un archivo de resultados.
"""

import sys
import time

def leer_numeros_desde_archivo(ruta_archivo):
    """
    Lee números desde un archivo y los almacena en una lista.
    Ignora líneas con datos inválidos y muestra advertencias.
    """
    numeros = []
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        for numero_linea, linea in enumerate(archivo, start=1):
            try:
                numero = float(linea.strip())
                numeros.append(numero)
            except ValueError:
                print(f"Dato inválido en la línea {numero_linea}: '{linea.strip()}' (ignorado)")
    return numeros

def calcular_media(numeros):
    """Calcula y devuelve la media de una lista de números."""
    return sum(numeros) / len(numeros)

def calcular_mediana(numeros):
    """Calcula y devuelve la mediana de una lista de números."""
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    mitad = n // 2
    if n % 2 == 0:
        return (numeros_ordenados[mitad - 1] + numeros_ordenados[mitad]) / 2
    return numeros_ordenados[mitad]

def calcular_moda(numeros):
    """
    Calcula y devuelve la moda de una lista de números.
    Devuelve una lista si hay múltiples modas.
    """
    frecuencia = {}
    for numero in numeros:
        frecuencia[numero] = frecuencia.get(numero, 0) + 1
    max_frecuencia = max(frecuencia.values())
    modas = [clave for clave, valor in frecuencia.items() if valor == max_frecuencia]
    return modas if len(modas) > 1 else modas[0]

def calcular_varianza(numeros, media):
    """Calcula y devuelve la varianza de una lista de números."""
    return sum((x - media) ** 2 for x in numeros) / len(numeros)

def calcular_desviacion_estandar(varianza):
    """Calcula y devuelve la desviación estándar a partir de la varianza."""
    return varianza ** 0.5

def main():
    """
    Función principal del programa.
    Lee números desde el archivo especificado, calcula estadísticas descriptivas,
    mide el tiempo de ejecución y guarda los resultados.
    """
    if len(sys.argv) != 2:
        print("Uso: python compute_statistics.py archivoConDatos.txt")
        return
    
    ruta_archivo = sys.argv[1]
    tiempo_inicio = time.time()

    numeros = leer_numeros_desde_archivo(ruta_archivo)
    if not numeros:
        print("No hay números válidos para procesar.")
        return

    media = calcular_media(numeros)
    mediana = calcular_mediana(numeros)
    moda = calcular_moda(numeros)
    varianza = calcular_varianza(numeros, media)
    desviacion_estandar = calcular_desviacion_estandar(varianza)

    tiempo_transcurrido = time.time() - tiempo_inicio

    resultados = (
        f"Media: {media}\n"
        f"Mediana: {mediana}\n"
        f"Moda: {moda}\n"
        f"Varianza: {varianza}\n"
        f"Desviación estándar: {desviacion_estandar}\n"
        f"Tiempo transcurrido: {tiempo_transcurrido:.5f} segundos"
    )

    print(resultados)

    with open("ResultadosEstadisticas.txt", "w", encoding="utf-8") as archivo_resultados:
        archivo_resultados.write(resultados)

if __name__ == "__main__":
    main()
