"""Generdores"""


def decorar_respuesta(funcion):
    def aplicar_decorador(tipo):
        print("Tu Turno es:")
        funcion(tipo)
        print("Aguarde y será atendido.")

    return aplicar_decorador


def generador(tipo):
    """Genera un nuevo turno de farmacia"""

    match tipo:
        case 'farmacia':
            turno_farmacia = 0
            while True:
                turno_farmacia += 1
                yield f"F-{turno_farmacia}"

        case 'perfumeria':
            turno_perfumeria = 0
            while True:
                turno_perfumeria += 1
                yield f"P-{turno_perfumeria}"

        case 'cosmeticos':
            turno_cosmeticos = 0
            while True:
                turno_cosmeticos += 1
                yield f"C-{turno_cosmeticos}"
