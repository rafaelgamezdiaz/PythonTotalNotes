"""
    ** TURNERO PARA UNA FARMACIA **
        Proyecto del dia 8
        - La Farmacia tiene tres áreas: Perfumeria, Farmacia, Cosméticos
        - Se pide al cliente que eloja un area en la que desea tomar un turno
        - Se asigna un numero de turno segun el área que se selecciona
        - El numero tendra el formato C-53 (C de Cosméticos), o F-11 (Farmacia), o P-31 (Perfumería)
        - El mensaje debe tener un mensaje antes de dar el numero, ejemplo "Tu Turno es:", y después: "Aguarde y será atendido"
        - Se pregunta si desea sacar otro turno (para atender a un nuevo cliente)
        - Crear un modulo llamado numeros.py donde vamos a colocar los generadores y el decorador
        - Y el modulo actual Principal.py donde tendremos la llamada a numeros.py
"""
from numeros import generador, decorar_respuesta


def mostrar_opciones():
    secciones = ["1 - Farmacia", "2 - Perfumería", "3 - Cosméticos"]
    for seccion in secciones:
        print(f"{seccion}")


@decorar_respuesta
def imprimir_seleccion(tipo):
    print(next(tipo))


def select_turns(turno_farmacia, turno_perfumeria, turno_cosmeticos):
    opcion = 0
    while opcion not in ["1", "2", "3"]:
        mostrar_opciones()
        opcion = input("Seleccione una sección en la que desee reservar un turno: \n")

    match opcion:
        case "1":
            imprimir_seleccion(turno_farmacia)
        case "2":
            imprimir_seleccion(turno_perfumeria)
        case "3":
            imprimir_seleccion(turno_cosmeticos)


def init_program():
    """Inicio del Programa"""
    print("// *****************************************")
    print("// Iniciando Turnero")
    print("// *****************************************")
    turno_farmacia = generador("farmacia")
    turno_perfumeria = generador("perfumeria")
    turno_cosmeticos = generador("cosmeticos")

    repetir = 'S'
    while repetir == 'S':
        repetir = input("Desea seleccionar un turno (S/N)? ").upper()
        if repetir == 'S':
            select_turns(turno_farmacia, turno_perfumeria, turno_cosmeticos)

    print("// *****************************************")
    print("// FIN Turnero")
    print("// *****************************************")


init_program()
