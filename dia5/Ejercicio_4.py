# Escribe una función llamada contar_primos() que requiera un
# solo argumento numérico.
# Esta función va a mostrar en pantalla todos los números
# primos existentes en el rango que va desde cero hasta ese
# número incluido, y va a devolver la cantidad de números
# primos que encontró.
# Aclaración, por convención el 0 y el 1 no se consideran primos

def es_primo(numero):
    divisores = [2, 3, 5, 7]
    if numero in divisores:
        return True

    check_primo = True
    for divisor in divisores:
        if numero % divisor != 0:
            continue
        check_primo = False

    return check_primo


def contar_primos(numero):
    lista_numeros = list(range(2, numero + 1, 1))
    cantidad_primos = 0
    primos = []
    for valor in lista_numeros:
        if es_primo(valor):
            primos.append(valor)
            cantidad_primos += 1

    print(primos)
    return cantidad_primos


print(contar_primos(50))
