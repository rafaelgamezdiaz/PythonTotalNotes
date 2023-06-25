# Crea una función llamada devolver_distintos() que reciba 3
# integers como parámetros.
# Si la suma de los 3 numeros es mayor a 15, va a devolver el
# número mayor.
# Si la suma de los 3 numeros es menor a 10, va a devolver el
# número menor.
# Si la suma de los 3 números es un valor entre 10 y 15
# (incluidos) va a devolver el número de valorintermedio.


#######################3
# SOLUCION
def devolver_distintos(numero1, numero2, numero3):
    lista_temp = [numero1, numero2, numero3]

    if sum(lista_temp) > 15:
        return max(lista_temp)
    elif sum(lista_temp) < 10:
        return min(lista_temp)
    else:
        lista_nueva = [x for x in lista_temp if x != min(lista_temp) and x != max(lista_temp)]
        return lista_nueva[0]


print(devolver_distintos(3, 4, 8))
