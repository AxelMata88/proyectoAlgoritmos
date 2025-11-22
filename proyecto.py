#Reyes Ortega Brayan
#Calderon Almanza Marvin Daniel
#Mata Centeno Axel Jesus

import string
import re
from collections import Counter

referencias = {
    "Inglés": "en_largo.txt",
    "Francés": "fr_largo.txt",
    "Italiano": "it_largo.txt"
}

misteriosos = {
    "Texto 1": "texto1.txt",
    "Texto 2": "texto2.txt"
}

LETTERS = string.ascii_lowercase 
histograma20 = 20 

#funcion para limpiar texto y dejar solo las letras y tambien en minusculas

def limpiar_letras(texto):
  
    texto = texto.lower()
    solo = []
    for ch in texto:
        if ch in LETTERS:
            solo.append(ch)
    return "".join(solo)

#funcion para calcular el histograma de los archivos

def frecuencias_letras_desde_archivo(ruta_archivo):
   
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        texto = f.read()

    texto_limpio = limpiar_letras(texto)
    contador = Counter(texto_limpio)
    total = sum(contador.values())

    frequencia = {}
    for letra in LETTERS:
        if total > 0:
            frequencia[letra] = contador.get(letra, 0) / total
        else:
            frequencia[letra] = 0.0
    return frequencia

def distancia_frecuencias(freq1, freq2):
    
    dist = 0.0
    for letra in LETTERS:
        dist += abs(freq1.get(letra, 0.0) - freq2.get(letra, 0.0))
    return dist

#funcion para imprimir el histograma ordenado de mayor a menor frecuencia

def imprimir_histograma_ordenado(nombre, freqs):
    
    print(f"\nHistograma odenado {nombre} ")
    ordenadas = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
    for letra, freq in ordenadas:
        print(f"{letra}: {freq:.6f}")
    return ordenadas

def limpiartxt(texto):
    
    texto = texto.lower()
    texto = re.sub(r"[^a-záéíóúüñ]", " ", texto)
    palabras = texto.split()
    return palabras

#funcion para crear el diccionario desde los archivos

def diccionario_palabras_desde_archivo(ruta_archivo):
   
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        texto = f.read()

    palabras = limpiartxt(texto)
    contador = Counter(palabras)
    return contador

def imprimir_diccionario(nombre, contador):
    
    total = sum(contador.values())
    distintas = len(contador)
    print(f"\n=== Diccionario de {nombre} ===")
    print(f"Total de palabras      : {total}")
    print(f"Palabras distintas     : {distintas}")
    print(f"Top {histograma20} palabras más frecuentes:")
    for palabra, freq in contador.most_common(histograma20):
        print(f"{palabra:15s} -> {freq}")


# Programa principal para calcular y comparar los histogramas

def main():
    freqs_ref = {}
    print("Calcular histogramas")
    for idioma, ruta in referencias.items():
        print(f"{idioma}: {ruta}")
        freqs_ref[idioma] = frecuencias_letras_desde_archivo(ruta)

    for nombre_texto, ruta_texto in misteriosos.items():
        print("--------------------------")
        print(f"Carga {nombre_texto}: {ruta_texto}")
        print("--------------------------")

        freqs_m = frecuencias_letras_desde_archivo(ruta_texto)
        imprimir_histograma_ordenado(nombre_texto, freqs_m)
        

        dicc_m = diccionario_palabras_desde_archivo(ruta_texto)
        imprimir_diccionario(nombre_texto, dicc_m)

        print(f"\n Comparación de {nombre_texto} con los idiomas")
        distancias = {}
        for idioma, freqs_idioma in freqs_ref.items():
            d = distancia_frecuencias(freqs_m, freqs_idioma)
            distancias[idioma] = d
            print(f"{idioma:10s} -> distancia = {d:.6f}")

        idioma_mas_probable = min(distancias, key=distancias.get)
        print(f"\nIdioma más probable {nombre_texto}: {idioma_mas_probable}")

if __name__ == "__main__":
    main()
