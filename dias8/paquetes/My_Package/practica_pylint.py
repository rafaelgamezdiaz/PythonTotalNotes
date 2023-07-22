"""
 Practica Pylint
"""


def sumar(numero1, numero2):
    """Esta funcion suma"""
    return numero1 + numero2


try:
    valor1 = input("valor1: ")
    valor2 = input("valor2: ")
    resultado = sumar(valor2, valor1)
except TypeError:
    print("Error")
else:
    print(resultado)
