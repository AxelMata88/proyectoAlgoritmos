import string
from collections import Counter
import textwrap

# Es el texto cifrado
ciphertext = """Rlm vywpdlat uybrm ryvgm quulrlm ebpdbmmlm udlmlvkm mad rq klkl oa rqubv, vykqwwlvk mad rq rledl mauldbladl lk rq uqdkbl qvkldbladl ol rq hyal, wqbm lgqrlwlvk qa-olmmam olm slat lk oqvm rq dlgbyv klwuydqrl, yvk av dyrl lmmlvkblr oqvm rq uldilukbyv oa kyaixld. Rl rqubv iywwav lmk av qvbwqr vyikadvl lk idluamiarqbdl. Br iywwavbzal qeli mlm iyvglvldlm udbvibuqrlwlvk uqd rlm yoladm, zab uldwlkklvk o'bolvkbcbld rl mltl lk r'qgl, wqbm qammb rl mkqkak myibqr. Zaqvo rl rqubv ol gqdlvvl mlvk av oqvgld, br udleblvk mlm iyvglvldlm lv kquqvk ol rq uqkkl qddbldl, il zab udyeyzal av pdabk mli, vlk lk pblv qaobprl q gdqvol obmkqvil. Rydmza'br qkkqzal, rl rqubv iyaixl mlm ydlbrrlm lv qddbldl lk uybvkl myv vlj eldm r'lvvlwb, iywwl m'br ixldixqbk q rab oyvvld olm iyaum ol wamlqa. Ilkkl qkkbkaol qgdlmmbel lmk dqdl ixlj rl rqubv lv iqukbebkl."""

# Son las funciones utilizadas
def frecuencias(texto):
    texto = texto.lower()
    solo_letras = [c for c in texto if c in string.ascii_lowercase]
    total = len(solo_letras)
    c = Counter(solo_letras)
    freqs = {letra: c[letra]/total for letra in c}
    return dict(sorted(freqs.items(), key=lambda x: x[1], reverse=True))

def aplicar_mapa(texto, mapa):
    resultado = []
    for ch in texto:
        c = ch.lower()
        if c in mapa and c in string.ascii_lowercase:
            nuevo = mapa[c]
            if ch.isupper():
                nuevo = nuevo.upper()
            resultado.append(nuevo)
        else:
            resultado.append(ch)
    return "".join(resultado)

# Es el mapa inicial de letras, en pocas palabras, la letra 'l' se reemplaza por la 'e', la letra 'v' se reemplaza por la 's'....asi sucesivamente
mapa = {
    'l': 'e', 'v': 's', 'q': 'i', 'm': 'n', 'k': 't', 'b': 'a', 'd': 'l',
    'r': 'r', 'a': 'u', 'y': 'o', 'u': 'd', 'i': 'c', 'o': 'p', 'w': 'm',
    'g': 'v', 'e': 'g', 'z': 'q', 'p': 'f', 'x': 'h', 't': 'b', 'j': 'x',
    'h': 'y', 's': 'j', 'c': 'w'
}

# Es el contador de intentos
intento = 1

def mostrar_intento(mapa, intento):
    print("\n=== MAPA ACTUAL ===")
    for k in sorted(mapa.keys()):
        print(f"{k} -> {mapa[k]}")
    print(f"\n=== TEXTO CIFRADO ===")
    print(textwrap.fill(ciphertext, width=80))
    print(f"\n=== TEXTO DESCIFRADO - INTENTO {intento} ===")
    texto_descifrado = aplicar_mapa(ciphertext, mapa)
    print(textwrap.fill(texto_descifrado, width=80))
    print("\n==============================================================================================")

   

# Muestra las frecuencias de las letras
print("=== FRECUENCIAS DEL TEXTO CIFRADO ===")
freqs = frecuencias(ciphertext)
for letra, f in freqs.items():
    print(f"{letra}: {f:.4f}")

# Es el numero de intentos, cada que se agrega un cambio en el mapa inicial tambien se agrega un intento nuevo para ver la evolucion de como va cambiando el texto cifrado
mostrar_intento(mapa, intento)

intento += 1
mapa['r'] = 'l'
mostrar_intento(mapa, intento)

intento += 1
mapa['m'] = 's'
mostrar_intento(mapa, intento)

intento += 1
mapa['q'] = 'a'
mostrar_intento(mapa, intento)

intento += 1
mapa['b'] = 'i'
mostrar_intento(mapa, intento)

intento += 1
mapa['v'] = 'n'
mostrar_intento(mapa, intento)

intento += 1
mapa['d'] = 'r'
mostrar_intento(mapa, intento)

intento += 1
mapa['u'] = 'p'
mostrar_intento(mapa, intento)

intento += 1
mapa['o'] = 'd'
mostrar_intento(mapa, intento)

intento += 1
mapa['g'] = 'g'
mostrar_intento(mapa, intento)

intento += 1
mapa['e'] = 'v'
mostrar_intento(mapa, intento)

intento += 1
mapa['j'] = 'z'
mostrar_intento(mapa, intento)

intento += 1
mapa['p'] = 'b'
mostrar_intento(mapa, intento)

intento += 1
mapa['t'] = 'x'
mostrar_intento(mapa, intento)

intento += 1
mapa['h'] = 'j'
mostrar_intento(mapa, intento)

intento += 1
mapa['c'] = 'f'
mostrar_intento(mapa, intento)

intento += 1
mapa['s'] = 'y'
mostrar_intento(mapa, intento)

traduccion = """Los numerosos pelos largos llamados vibrisas presentes en la cabeza del conejo, 
principalmente en el labio superior y la parte anterior de la mejilla, pero también por 
encima de los ojos y en la región temporal, tienen un papel esencial en la percepción del 
tacto. El conejo común es un animal nocturno y crepuscular. Se comunica con sus congéneres 
principalmente a través de los olores, lo que permite identificar el sexo y la edad, así como 
también el estatus social. Cuando el conejo de campo siente un peligro, advierte a sus 
congéneres golpeando con la pata trasera, lo que provoca un ruido seco, claro y bien audible 
a gran distancia. Cuando ataca, el conejo pone sus orejas hacia atrás y apunta su nariz hacia 
el enemigo, como si intentara darle golpes con el hocico. Esta actitud agresiva es rara en 
el conejo en cautiverio."""

wrapped = textwrap.fill(traduccion, width=80)

print("\n=== TEXTO TRADUCIDO ===")
print(wrapped)











