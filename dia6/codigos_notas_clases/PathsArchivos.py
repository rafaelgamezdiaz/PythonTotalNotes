# import os
# import shutil


# ruta = os.getcwd()

# os.chdir('C:\\Users\\rafae\\OneDrive\\Escritorio\\pyfiles')

#
# def remove_folder(carpeta):
#     if os.path.exists(carpeta):
#         if os.path.isdir(carpeta):
#             if os.listdir(carpeta):
#                 shutil.rmtree(carpeta)
#             else:
#                 os.rmdir(carpeta)
#         else:
#             print('No es un directorio valido')
#     else:
#         print('El directorio no existe')
#
#
# ruta = 'C:\\Users\\rafae\\OneDrive\\Escritorio\\pyfiles\\nueva'
# # if os.path.dirname(path):
# #     os.rmdir(path)
# #
# # os.mkdir(path)
# # os.chdir(path)
# # archivo = open('otro_archivo.txt', 'w')
# # archivo.write('Nuevo archivo en nueva carpeta')
# # archivo.close()
# # print(archivo.read())
#
#
# # path = 'C:\\Users\\rafae\\OneDrive\\Escritorio\\pyfiles\\nueva\mifile.txt'
# # filename = os.path.basename(path)
# # dirname = os.path.dirname(path)
# # ruta, nombre = os.path.split(path)
# # print(ruta, '\n', nombre)
#
# # os.rmdir(ruta)
#
# #os.path.exists(ruta)
#
# remove_folder(ruta)


##########################################


from pathlib import Path

carpeta = Path('C:/Users/rafae/OneDrive/Escritorio/pyfiles/nueva')
archivo = carpeta / 'otroarchivo.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())