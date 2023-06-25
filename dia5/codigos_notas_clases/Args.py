# def suma(*args):
#     resultado = 0
#     for argumento in args:
#         resultado += argumento
#     return resultado


# def suma(*args):
#     return sum(args)
#
#
# print(sum([3, 4, 5]))
# print(suma(2, 3, 5, 4, 3, 2, 1, 34))


# def suma_cuadrados(*args):
#     return sum([x ** 2 for x in args])
#
#
# print(suma_cuadrados(2,3,5,-7))
# # suma_cuadrados(1,2,3)


# Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión,
# y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume,
# o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).
def numeros_persona(nombre, *args):
    return f"{nombre}, la suma de tus números es {sum(args)}"


print(numeros_persona('Rafael', 2,4,5,6))
# def suma_absolutos(*args):
#     return sum([abs(x) for x in args])
#
#
# print(suma_absolutos(-1, 23,-10))


# Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.

# La función debe devolver el siguiente mensaje: "{nombre}, la suma de tus números es {suma_numeros}"

