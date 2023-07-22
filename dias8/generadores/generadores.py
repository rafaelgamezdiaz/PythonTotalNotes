def mi_funcion():
    return 4


# def mi_generador():
#     for numero in range(1, 10):
#         yield numero**2
#
#
# print(mi_funcion())
# g = mi_generador()
#
# print(next(g))
# print(next(g))
# print(next(g))

# def generador_infinito():
#     inicio = 0
#     while True:
#         inicio += 1
#         yield inicio
#
#
# secuencia = generador_infinito()
# print(next(secuencia))
# print(next(secuencia))
# print(next(secuencia))


# def generador_multiplos_7():
#     inicio = 0
#     while True:
#         inicio += 7
#         yield inicio
#
#
# generador = generador_multiplos_7()
# print(next(generador))

def vidas_restantes():
    vidas = 4
    while True:
        vidas -= 1
        if vidas == 1:
            yield f"Te queda {vidas} vida"
        elif vidas < 1:
            yield "Game Over"
        else:
            yield f"Te quedan {vidas} vidas"


perder_vida = vidas_restantes()

print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
