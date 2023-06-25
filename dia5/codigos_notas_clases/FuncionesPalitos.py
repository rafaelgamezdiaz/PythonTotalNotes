#######################################################
from random import shuffle

# Lista inicial
palitos = ['-', '--', '---', '----']


# Mexclar Palitos
def mezclar(lista):
    shuffle(lista)
    return lista


# Pedir Intento
def probar_suerte():
    intento = ''

    while intento not in ['1', '2', '3', '4']:
        intento = input('Elige un número del 1 al 4: ')

    return int(intento)


# Comprobar respuesta de intento
def chequear_intento(intento, lista):
    lista = mezclar(lista)
    if lista[intento - 1] == '-':
        print(f'A lavar los platos')
    else:
        print(f'Te salvaste')

    print(f'Elegiste {lista[intento - 1]}')


chequear_intento(probar_suerte(), palitos)