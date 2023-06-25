# def saludo(nombre):
#     """Funcion que saluda
#     otra linea"""
#     print(f'Hola {nombre}')
#
#
# saludo('Rafael')
# saludo('Rocio')
import numpy as np

# def invertir_palabra(palabra):
#     return palabra[::-1].upper()
#
#
# palabra = 'Python'
#
# print(invertir_palabra(palabra))

# def chequear_3_cifras(numero):
#     return 100 < numero < 1000
#
#
# respuesta = chequear_3_cifras(1112)
#
# print(respuesta)


# Crea una función (todos_positivos) que reciba una lista de números como parámetro, y devuelva True si todos
# los valores de una lista son positivos, y False si al menos uno de los valores es negativo.
# Crea una lista llamada lista_numeros con valores positivos y negativos.
#
# No invoques la función, solo es necesario definirla.

# def todos_positivos(lista_numeros):
#     for numero in lista_numeros:
#         if numero < 0:
#             return False
#
#     return True
#
#
# lista_numeros = [3, 12, -5, 234, -4, 123]
# print(todos_positivos(lista_numeros))


# Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0
# y menores a 1000, y devuelva el resultado de dicha suma.

# def suma_menores(lista):
#     acumulado = 0
#     for numero in lista:
#         if 0 < numero < 1000:
#             acumulado += numero
#
#     return acumulado
#
#
# def suma_menores2(lista):
#     l2 = [numero for numero in lista if 0 < numero < 1000]
#     return np.sum(l2)
#
#
# lista_numeros = [1, -3, 4, 123124, 6]
#
# print(suma_menores(lista_numeros))
# print(suma_menores2(lista_numeros))


# Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta.

# def cantidad_pares(lista_numeros):
#     return len([numero for numero in lista_numeros if numero % 2 == 0])
#
#
# lista_numeros = [3, 54, 12, 676, 9, 1, 23]
# print(cantidad_pares(lista_numeros))


# precios_cafe = [('capuchino', 1.5), ('Expreso', 1.2), ('Moka', 1.9)]
#
#
# def cafe_mas_caro(lista_precios):
#     respuesta = [elemento for elemento in lista_precios if elemento[1] > 1.6]
#     return respuesta
#
#
# print(cafe_mas_caro(precios_cafe))

########################################################
# from random import shuffle
#
# # Lista inicial
# palitos = ['-', '--', '---', '----']
#
#
# # Mexclar Palitos
# def mezclar(lista):
#     shuffle(lista)
#     return lista
#
#
# # Pedir Intento
# def probar_suerte():
#     intento = ''
#
#     while intento not in ['1', '2', '3', '4']:
#         intento = input('Elige un número del 1 al 4: ')
#
#     return int(intento)
#
#
# # Comprobar respuesta de intento
# def chequear_intento(intento, lista):
#     lista = mezclar(lista)
#     if lista[intento - 1] == '-':
#         print(f'A lavar los platos')
#     else:
#         print(f'Te salvaste')
#
#     print(f'Elegiste {lista[intento - 1]}')
#
#
# chequear_intento(probar_suerte(), palitos)


##########################################
# from random import choice
#
#
# def lanzar_dados():
#     lista_dado = ['1', '2', '3', '4', '5', '6']
#     return int(choice(lista_dado)), int(choice(lista_dado))


# def evaluar_jugada(valor1, valor2):
#     suma_dados = valor1 + valor2
#     if suma_dados <= 6:
#         return f"La suma de tus dados es {suma_dados}. Lamentable"
#     if 6 < suma_dados < 10:
#         return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
#     if suma_dados >= 10:
#         return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"


# resultado1, resultado2 = lanzar_dados()
# respuesta = evaluar_jugada(resultado1, resultado2)
#
# print(respuesta)


# def reducir_lista(lista):
#     '''Elimina duplicados y elimina el valor mas grande'''
#     sin_duplicados = list(set(lista))
#     ordenada = sorted(sin_duplicados)
#     ordenada.pop()
#     return ordenada
#
#
# def promedio(lista):
#     suma = 0
#     for item in lista:
#         suma += item
#
#     return suma / len(lista)
#
#
# lista_numeros = [1, 2, 15, 7, 2]
# reducida = reducir_lista(lista_numeros)
# respuesta2 = promedio(reducida)
# print(respuesta2)