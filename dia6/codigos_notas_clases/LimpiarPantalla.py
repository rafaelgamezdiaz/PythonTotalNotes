# from os import system
#
# nombre = input('Dime tu nombre? ')
# edad = input('Dime tu edad? ')
# system('cls')
# print(f'Tu nombre es {nombre} y tienes {edad} años')


########################################################
# Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro,
# y devuelva su contenido (read).

# def abrir_leer(nombre_archivo):
#     archivo = open(nombre_archivo)
#     contenido = archivo.read()
#     archivo.close()
#     return contenido


# print(abrir_leer('registro.txt'))

#####################################
# Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro,
# y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"
#
# def sobrescribir(archivo):
#     file = open(archivo, 'w')
#     file.write("contenido eliminado")
#     file.close()
#
#
# sobrescribir('texto.txt')

#################################33333

# Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro,
# y lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución".
# Finalmente, debe cerrar el archivo abierto.

# from pathlib import Path


# def registro_error(archivo):
#     file = open(archivo, 'a')
#     file.write('se ha registrado un error de ejecución')
#     file.close()
#
#
# registro_error('registro.txt')

from pathlib import Path

ruta = Path('C:\Developer\Python\PythonTotal\dia6') / 'Cuestionario Día 6' / 'Pregunta 1' / 'miarchivox.pdf'

print(ruta.stem)


