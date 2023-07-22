def suma(num1, num2):
    try:
        if num1 is None or num2 is None:
            raise ValueError("Ambos sumandos deben estar definidos")

        suma = num1 + num2

    except ValueError as error:
        print("Error: ", error)
    except:
        print("Error inesperado")
    else:
        print(suma)


def cociente(num1, num2):
    try:
        division = num1 / num2
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")
    else:
        print(division)


def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")


suma(2, 3)
suma(3, None)
suma("123", 234)
cociente(18, 3)
cociente("18", 3)
cociente(18, 0)
