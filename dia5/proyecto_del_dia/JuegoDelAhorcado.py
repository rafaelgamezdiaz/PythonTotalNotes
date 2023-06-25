from random import choice

lista_palabras = ['ahorcado', 'murcielago', 'ventilador', 'escaparate', 'enrollado', 'biblioteca', 'natacion',
                  'repercutir', 'salvacion']
numero_vidas = 6
volver_a_jugar = 'S'

def seleccionar_palabra(lista):
    return choice(lista)


def pedir_letra():
    validas = 'abcdefghijklmnñopqrstuvwxyz'
    letra = '1'
    while letra not in validas:
        letra = input('Ingrese una letra: ')

    return letra


def checkear_letra(letra, palabra):
    if letra in palabra:
        return True
    return False


def posiciones_letra(letra, palabra):
    posiciones = []
    for posicion, caracter in enumerate(palabra):
        if caracter == letra:
            posiciones.append(posicion)

    return posiciones


def reemplazar_encontradas(letra, posiciones, palabra):
    lista_letras = enumerate(palabra)

    l_palabra_reemplazada = []
    for pos, le in lista_letras:
        if pos in posiciones:
            l_palabra_reemplazada.append(letra)
        else:
            l_palabra_reemplazada.append(le)

    return ''.join(l_palabra_reemplazada)


def juego(listapalabras, vidas):
    palabra = seleccionar_palabra(listapalabras)
    adivinadas = ''.join(['_' for letra in palabra])
    has_acertado = False
    lista_incorrectas = []
    print('Ha iniciado el Juego del ahorcado. Tienes seis intentos para adivinar la palabra. En cada intento me diras una letra')
    print(f'???: {adivinadas}')
    while vidas > 0:
        letra = pedir_letra()
        chequear_letra = checkear_letra(letra, palabra)
        if chequear_letra:
            posiciones_de_la_letra = posiciones_letra(letra, palabra)
            adivinadas = reemplazar_encontradas(letra, posiciones_de_la_letra, adivinadas)
        else:
            lista_incorrectas.append(letra)
            vidas -= 1

        if vidas > 0:
            print(f'Te quedan {vidas} oportunidades')
            print(f'???: {adivinadas}')
            print(f'Letras incorrectas: {lista_incorrectas}')
        if '_' not in adivinadas:
            has_acertado = True
            print(f'Felicitaciones!! Has adivinado la palabra: {adivinadas}')
            break

    if not has_acertado:
        print(f'Lo sentimos :( no has podido adivinar la palabra: {palabra}')


while volver_a_jugar.upper() == 'S':
    juego(lista_palabras, numero_vidas)
    volver_a_jugar = input('Desea volver a jugar (S/N)')
