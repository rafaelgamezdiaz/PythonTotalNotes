# class Animal:
#
#     def __init__(self, color, especie):
#         self.color = color
#         self.especie = especie
#
#     def emitir_sonido(self):
#         print('El animal ha emitido un sonido')
#
#     @classmethod
#     def desplazar(cls, distancia):
#         print(f'Se desplazó {distancia} metros')
#
#     @staticmethod
#     def mirar(objeto_mirado):
#         print(f'El animal ha mirado el/la {objeto_mirado}')
#
#
# class Ave(Animal):
#
#     def __init__(self, color, especie, altura_vuelo):
#         super().__init__(color, especie)
#         self.altura_vuelo = altura_vuelo
#
#     def volar(self, metros):
#         print(f'Voló {metros} metros.')
#
#
# sinsontillo = Ave('verde', 'ss')
# print(sinsontillo.color)

# mi_pajaro = Pajaro('azul', 'sinsonte')
# mi_pajaro.piar()
# mi_pajaro.volar(15)
# mi_pajaro.alas = False
# mip2 = Pajaro('Rosado', 'Samuro')
# print(mip2.alas)
# Pajaro.poner_huevos(3)

# Pajaro.mirar('al gusanito')


# Pajaro.

# class Perro:
#
#     def ladrar(self):
#         print('Guau!')

# class Alarma:
#
#     def postergar(self, cantidad_minutos):
#         print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")
#
#
# alarma = Alarma()
# alarma.postergar(10)


# class Padre:
#
#     def trabajar(self):
#         print("Trabajando en el Hospital")
#
#     def reir(self):
#         print("Ja ja ja!")
#
#
# class Madre:
#     def trabajar(self):
#         print("Trabajando en la Fiscalía")
#
#
# class Hija(Madre, Padre):
#     pass
#
#
# la_hija = Hija()
#
#
# la_hija.trabajar()
# la_hija.reir()


# Crea una clase Ornitorrinco que herede de otras clases: Vertebrado, Pez,
# Reptil, Ave y Mamifero, tal que
# "construyas" un animal que tiene los siguientes métodos y atributos:
# - poner_huevos()
# - tiene_pico = True
# - vertebrado = True
# - venenoso = True
# - nadar()
# - caminar()
# - amamantar()
#
# class Vertebrado:
#     vertebrado = True
#
# class Ave(Vertebrado):
#     tiene_pico = True
#     def poner_huevos(self):
#         print("Poniendo huevos")
#
# class Reptil(Vertebrado):
#     venenoso = True
#
# class Pez(Vertebrado):
#     def nadar(self):
#         print("Nadando")
#     def poner_huevos(self):
#         print("Poniendo huevos")

# class Mamifero(Vertebrado):
#     def caminar(self):
#         print("Caminando")
#     def amamantar(self):
#         print("Amamantando crías")
#
#
# class Ornitorrinco(Ave, Reptil, Pez, Mamifero):
#     pass

#
# miorni = Ornitorrinco()
#
# print(miorni.venenoso)
# print(miorni.vertebrado)
# print(miorni.venenoso)
# miorni.poner_huevos()
# miorni.nadar()
# miorni.caminar()
# miorni.amamantar()


# palabra = "polimorfismo"
# lista = ["Clases", "POO", "Polimorfismo"]
# tupla = (1, 2, 3, 80)
#
# for elemento in [palabra, lista, tupla]:
#     print(len(elemento))


# class Mago():
#     def atacar(self):
#         print("Ataque mágico")
#
#
# class Arquero():
#     def atacar(self):
#         print("Lanzamiento de flecha")
#
#
# class Samurai():
#     def atacar(self):
#         print("Ataque con katana")
#
#
# guerrero_mago = Mago()
# guerrero_arquero = Arquero()
# guerrero_samurai = Samurai()
#
# personajes = [guerrero_samurai, guerrero_arquero, guerrero_mago]
#
# for personaje in personajes:
#     personaje.atacar()


# class Mago():
#     def defender(self):
#         print("Escudo mágico")
#
#
# class Arquero():
#     def defender(self):
#         print("Esconderse")


# class Samurai:
#     def defender(self):
#         return "Bloqueo"
#
#     def __str__(self):
#         return self.defender()
#
#     def __del__(self):
#         print("Se ha eliminado la instancia")
#
#
# # def personaje_defender(personaje):
# #     personaje.defender()
#
#
# guerrero_samurai = Samurai()
#
# del guerrero_samurai
#
# print(guerrero_samurai.defender())

# guerrero_mago = Mago()
# guerrero_arquero = Arquero()
# guerrero_samurai = Samurai()
#
#
# personaje_defender(guerrero_mago)
