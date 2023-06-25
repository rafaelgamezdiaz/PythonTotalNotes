from random import choice


def lanzar_dados():
    lista_dado = ['1', '2', '3', '4', '5', '6']
    return int(choice(lista_dado)), int(choice(lista_dado))


def evaluar_jugada(valor1, valor2):
    suma_dados = valor1 + valor2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    if 6 < suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    if suma_dados >= 10:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"


resultado1, resultado2 = lanzar_dados()
respuesta = evaluar_jugada(resultado1, resultado2)

print(respuesta)