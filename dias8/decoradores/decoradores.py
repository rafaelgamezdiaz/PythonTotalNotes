"""Decoradores"""


# def cambiar_letras(tipo):
#     def mayusculas(texto):
#         """Mayusculas"""
#         print(texto.upper())
#
#     def minusculas(texto):
#         """Minusculas"""
#         print(texto.lower())
#
#     if tipo == 'may':
#         return mayusculas
#     elif tipo == "min":
#         return minusculas
#
#
# operacion = cambiar_letras("may")

# operacion("pAlAbra")
#
#
# def una_funcion(funcion):
#     """Funcion como argumento"""
#     return funcion


def decorar_saludo(funcion):

    def aplicar(palabra):
        print("Hola")
        funcion(palabra)
        print("Adios")

    return aplicar


@decorar_saludo
def mayusculas(texto):
    print(texto.upper())


def minusculas(texto):
    print(texto.lower())



mayusculas("la casa")


mayusculas_decorada = decorar_saludo(mayusculas)