# Escribe una función que requiera una cantidad indefinida de
# argumentos. Lo que hará esta función es devolver True si en
# algún momento se ha ingresado al numero cero repetido dos
# veces consecutivas.

# Por ejemplo:
# (5,6,1,0,0,9,3,5) >>> True
# (6,0,5,1,0,3,0,1) >>> False

def detector_ceros_repetidos(*args):
    anterior = 1
    for numero in args:
        if anterior == 0 and numero == 0:
            return True
        anterior = numero
    return False


print(detector_ceros_repetidos(0,5,6,1,0,9,3,5, 0))
print(detector_ceros_repetidos(6,0,5,1,0,3,0,1))
