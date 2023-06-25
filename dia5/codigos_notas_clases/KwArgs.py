# def suma(**kwargs):
#
#     total = 0
#
#     for clave, valor in kwargs.items():
#         print(f'{clave} = {valor}' )
#         total += valor
#
#     return total
#
# print(suma(x=3, y=5, z=2))


# def cantidad_atributos (**kwargs):
#     return len(kwargs)
#
#
# print(cantidad_atributos(x = 1, y = 2, z = 3, r = 12, rt = 432))


# Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados
# en forma de palabras clave (keywords). La función debe preveer recibir cualquier cantidad de argumentos de este tipo.

# def lista_atributos(**kwargs):
#     return list(kwargs.values())
#
#
# print(lista_atributos(x=3, w=3, d=5, q=4, y=34, fg=21))

#################################################################################3
# Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad indetermida
# de argumentos. Esta función deberá mostrar en pantalla:

def describir_persona(nombre, **kwargs):
    print(f'Características de {nombre}:')
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')



describir_persona("María", color_ojos="azules", color_pelo="rubio")
# Características de {nombre}:
# {nombre_argumento}: {valor_argumento}
# {nombre_argumento}: {valor_argumento}
# etc...
# Por ejemplo:
#
# describir_persona("María", color_ojos="azules", color_pelo="rubio")
#
# Mostrará en pantalla:
#
# Características de María:
# color_ojos: azules
# color_pelo: rubio
