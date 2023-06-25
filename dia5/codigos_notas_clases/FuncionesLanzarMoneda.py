from random import choice


def lanzar_moneda():
    return choice(['Cara', 'Cruz']);


# Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero,
# debe ser el resultado del lanzamiento de la moneda.
# El segundo argumento, será una lista de números cualquiera
# (debes crear una lista con valores y llamarla lista_numeros).


def probar_suerte(intento, lista_numeros):
    if intento == 'Cara':
        print("La lista se autodestruirá")
        lista_numeros.clear()
    else:
        print("La lista fue salvada")

    return lista_numeros

#   Si se le proporciona una "Cara", debe mostrar el mensaje al usuario:
#   "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).

#   Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.


intento = lanzar_moneda()
lista_numeros = [1, 2, 3, 4, 5, 6]
print(intento)
suerte = probar_suerte(intento, lista_numeros)
print(suerte)
