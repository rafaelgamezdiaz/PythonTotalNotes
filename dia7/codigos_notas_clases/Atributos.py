# class Casa:
#
#     def __init__(self, color, cantidad_pisos):
#         self.color = color
#         self.cantidad_pisos = cantidad_pisos
#
#
# casa_blanca = Casa('blanco', 4)
#
# print(casa_blanca.cantidad_pisos, casa_blanca.color)

class Cubo:

    caras = 6

    def __init__(self, color):
        self.color = color


cubo_rojo = Cubo('verde')

print(cubo_rojo.color)