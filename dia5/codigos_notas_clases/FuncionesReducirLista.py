def reducir_lista(lista):
    '''Elimina duplicados y elimina el valor mas grande'''
    sin_duplicados = list(set(lista))
    ordenada = sorted(sin_duplicados)
    ordenada.pop()
    return ordenada


def promedio(lista):
    suma = 0
    for item in lista:
        suma += item

    return suma / len(lista)


lista_numeros = [1, 2, 15, 7, 2]
reducida = reducir_lista(lista_numeros)
respuesta2 = promedio(reducida)
print(respuesta2)