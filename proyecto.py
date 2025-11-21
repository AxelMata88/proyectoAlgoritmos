import string
import re
from collections import Counter
import matplotlib.pyplot as plt

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
TOP_N_PALABRAS = 20 

def limpiar_letras(texto):
    """
    Deja solo letras a-z en minúsculas (sin acentos).
    Sirve para comparar histogramas entre idiomas.
    """
    texto = texto.lower()
    solo = []
    for ch in texto:
        if ch in LETTERS:
            solo.append(ch)
    return "".join(solo)

def frecuencias_letras_desde_archivo(ruta_archivo):
    """
    Regresa un dict letra -> frecuencia relativa (0 a 1)
    para un archivo dado.
    """
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        texto = f.read()

    texto_limpio = limpiar_letras(texto)
    contador = Counter(texto_limpio)
    total = sum(contador.values())

    freqs = {}
    for letra in LETTERS:
        if total > 0:
            freqs[letra] = contador.get(letra, 0) / total
        else:
            freqs[letra] = 0.0
    return freqs

def distancia_frecuencias(freq1, freq2):
    """
    Distancia entre dos histogramas de letras.
    Usamos suma de diferencias absolutas.
    """
    dist = 0.0
    for letra in LETTERS:
        dist += abs(freq1.get(letra, 0.0) - freq2.get(letra, 0.0))
    return dist

def imprimir_histograma_ordenado(nombre, freqs):
    """
    Imprime el histograma ordenado (letra de mayor a menor frecuencia).
    """
    print(f"\n=== Histograma (letras ordenadas) - {nombre} ===")
    ordenadas = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
    for letra, freq in ordenadas:
        print(f"{letra}: {freq:.6f}")
    return ordenadas

def limpiar_y_tokenizar(texto):
    """
    Convierte a minúsculas y separa en palabras.
    Conserva áéíóúüñ, quita números y signos.
    """
    texto = texto.lower()
    texto = re.sub(r"[^a-záéíóúüñ]", " ", texto)
    palabras = texto.split()
    return palabras

def diccionario_palabras_desde_archivo(ruta_archivo):
    """
    Regresa Counter (palabra -> frecuencia)
    para un archivo dado.
    """
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        texto = f.read()

    palabras = limpiar_y_tokenizar(texto)
    contador = Counter(palabras)
    return contador

def imprimir_diccionario(nombre, contador):
    """
    Imprime resumen del diccionario de palabras.
    """
    total = sum(contador.values())
    distintas = len(contador)
    print(f"\n=== Diccionario de {nombre} ===")
    print(f"Total de palabras      : {total}")
    print(f"Palabras distintas     : {distintas}")
    print(f"Top {TOP_N_PALABRAS} palabras más frecuentes:")
    for palabra, freq in contador.most_common(TOP_N_PALABRAS):
        print(f"{palabra:15s} -> {freq}")

def graficar_histograma(nombre, freqs):
    """
    Grafica el histograma ordenado de un texto (solo).
    """
    ordenadas = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
    letras = [l for l, _ in ordenadas]
    valores = [v for _, v in ordenadas]

    plt.figure()
    plt.bar(letras, valores)
    plt.title(f"Histograma de letras - {nombre}")
    plt.xlabel("Letras")
    plt.ylabel("Frecuencia relativa")
    plt.tight_layout()
    plt.show()


def main():
    freqs_ref = {}
    print("=== Calculando histogramas de referencia ===")
    for idioma, ruta in referencias.items():
        print(f"{idioma}: {ruta}")
        freqs_ref[idioma] = frecuencias_letras_desde_archivo(ruta)

    for nombre_texto, ruta_texto in misteriosos.items():
        print("\n" + "=" * 50)
        print(f"Procesando {nombre_texto}: {ruta_texto}")
        print("=" * 50)

        freqs_m = frecuencias_letras_desde_archivo(ruta_texto)
        imprimir_histograma_ordenado(nombre_texto, freqs_m)
        graficar_histograma(nombre_texto, freqs_m)

        dicc_m = diccionario_palabras_desde_archivo(ruta_texto)
        imprimir_diccionario(nombre_texto, dicc_m)

        print(f"\n--- Comparación de {nombre_texto} con los idiomas ---")
        distancias = {}
        for idioma, freqs_idioma in freqs_ref.items():
            d = distancia_frecuencias(freqs_m, freqs_idioma)
            distancias[idioma] = d
            print(f"{idioma:10s} -> distancia = {d:.6f}")

        idioma_mas_probable = min(distancias, key=distancias.get)
        print(f"\n>>> Idioma más probable para {nombre_texto}: {idioma_mas_probable} <<<")

if __name__ == "__main__":
    main()
