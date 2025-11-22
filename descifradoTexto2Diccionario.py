def descifra_sustitucion(cadena, llave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    cifrado = ''
    cadena = cadena.lower()    
    for letra in cadena:
        if letra in alfabeto:
            pos = llave.lower().index(letra)
            cifrado += alfabeto[pos]
        else:
            cifrado += letra        
    return cifrado

def carga_dic(nombre):
    arch = open(nombre, 'r')
    texto = arch.read()
    arch.close()
    return texto.split()



alfabeto = 'abcdefghijklmnopqrstuvwxyz'
cifrado ='Yjwwsk pjoes psuswngsp pvcdoz kms Dkjwdjo Csojdlljoes, yshncs sunwudoz do Hcjoes jop Cvlldj dokn j enoesck pjoes xsjok hnc gvywde gschncxjoes. Kmdl dl do kms hncx nh j yjwwsk, do imdem kms pjoes dl emncsnzcjgmsp idkm ewjlldejw xvlde. Yjwwsk gcnpvekdnol ujca yskisso vldoz swjyncjks enlkvxsl jop lkjzdoz jop vldoz xdodxjw enlkvxsl jop yjcs lkjzdoz.Yjwwsk dl oni j idpslgcsjp, mdzmwa ksemodejw hncx nh pjoes idkm xjoa lvyzsocsl doewvpdoz ewjlldejw, cnxjokde, osnewjlldejw jop enoksxgncjca. Idkm ldq encs csenzodfsp xskmnpl: kms Eseemskkd xskmnp, kms Ynvconudwws xskmnp, kms Ujzjonuj xskmnp, kms Hcsoem Lemnnw, kms Cnajw Jejpsxa nh Pjoes xskmnp jop kms Yjwjoemdos xskmnp, yjwwsk dl lkvpdsp gcnhslldnojwwa jk kng pjoes lemnnwl jww nusc kms incwp.'
llave = 'jyepshzmdbrwxongtclkvuiqaf'
dic1 = carga_dic('words.txt')

posA = 'j'
posB = 'y'
posC = 'e'
posD = 'p'
posE = 's'
posF = 'h'
posG = 'z'
posH = 'm'
posI = 'd'
posJ = 'b'
posK = 'r'
posL = 'w'
posM = 'x'
posN = 'o'
posO = 'n'
posP = 'g'
posQ = 't'
posR = 'c'
posS = 'l'
posT = 'k'
posU = 'v'
posV = 'u'
posW = 'i'
posX = 'q'
posY = 'a'
posZ = 'f'

#probando con Yjwwsk
#                                    
c = 0
prueba = ''
for p in dic1:
    if len(p) == 6 and len(set(p))==5:
        if p[0] in posY and p[1] in posJ and p[2]==p[3] in posW and p[4] in posS and p[5] in posK:
            
        
            print(p)
            if not(p[0] in prueba):
                prueba += p[0]
            c = c + 1
print('cumplen:', c)
print(prueba)

print('------------------')
print(cifrado)
print('------------------')
print(descifra_sustitucion(cifrado, llave))
print('------------------')