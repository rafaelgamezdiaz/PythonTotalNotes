from pathlib import Path
from os import system

def info_recetas():
    ruta_recetario = path_recetas()
    total = 0
    for _ in ruta_recetario.glob('**/*.txt'):
        total += 1

    print(f'** INFORMACION DEL RECETARIO **')
    print(f'      - Actualmente hay registradas {total} recetas.')
    print(f'      - Todas las recetas se encuentran en la carpeta: {ruta_recetario}')


def pausa():
    input('\nPresione una tecla para continuar ...')
    system('cls')


def path_recetas():
    return Path(Path.cwd(), 'Recetas')


def lista_carpetas(directorio):
    """Retorna una lista de los directorio contenidos en un directorio dado. No se consideran los subdirectorios"""
    return [carpeta.name for carpeta in directorio.iterdir() if carpeta.is_dir()]


def divisor():
    system('cls')
    print('*' * 50)


def seleccionar_opcion():
    opcion = -1
    while opcion not in ['1', '2', '3', '4', '5', '6']:
        divisor()
        print(f'** SELECCIONA UNA OPCIÓN **')
        print('[1] - leer receta')
        print('[2] - crear receta')
        print('[3] - crear categoría')
        print('[4] - eliminar receta')
        print('[5] - eliminar categoría')
        print('[6] - finalizar programa')
        opcion = input('opcion: ')

    return int(opcion)


def mostrar_listado(listados, tipolistado):
    print(f'Selecciona una {tipolistado}')
    for indice, listado in listados:
        print(f'[{indice + 1}] - {listado}')


def elegir_categoria():
    lista_categorias = categorias()
    opciones_validas = [indice for indice, _ in enumerate(lista_categorias)]
    opcion_seleccionada = -1
    while opcion_seleccionada not in opciones_validas:
        divisor()
        print(f'** CATEGORIAs **')
        mostrar_listado(lista_categorias, 'categoría')
        opcion_seleccionada = input('categoría?: ')
        if not opcion_seleccionada.isdigit():
            continue
        opcion_seleccionada = int(opcion_seleccionada) - 1

    return opcion_seleccionada


def seleccionar_receta(indice_categoria):
    lista_categorias = categorias()
    nombre_categoria = lista_categorias[indice_categoria][1]
    ruta = path_recetas()
    ruta_categoria = Path(Path(ruta) / nombre_categoria)

    recetas_pathname = list(
        enumerate([receta_listada for receta_listada in ruta_categoria.glob('**/*.txt')]))

    recetas = list(
        enumerate([receta_listada.name.removesuffix('.txt') for _, receta_listada in recetas_pathname]))

    if len(recetas) > 0:
        opciones_validas = [indice for indice, _ in enumerate(recetas)]
        opcion_seleccionada = -1
        while opcion_seleccionada not in opciones_validas:
            divisor()
            print(nombre_categoria.upper())
            mostrar_listado(recetas, 'receta')
            opcion_seleccionada = input('receta:? ')
            if not opcion_seleccionada.isdigit():
                continue
            opcion_seleccionada = int(opcion_seleccionada) - 1

        return recetas_pathname[opcion_seleccionada]

    print('No se han guardado recetas en esta categoría.')
    pausa()
    return []


def leer_archivo(archivo):
    print('Contenido de la receta: \n')
    print(archivo.read_text())
    pausa()


def eliminar_archivo(archivo):
    archivo.unlink()


def nuevo_archivo(archivo, subcarpeta):
    nombre_receta = input('Ingrese el nombre de la receta: ')
    texto_receta = input('Ingrese el contenido de la receta: ')
    nombre_receta = nombre_receta + '.txt'
    archivo = Path(archivo) / subcarpeta / nombre_receta
    archivo = Path(archivo)
    archivo.write_text(texto_receta)


def nueva_categoria():
    divisor()
    print(f'** CREAR CATEGORIA **')
    nombre_nueva_categoria = input('Nombre para la nueva categoría?: ')
    ruta_actual = path_recetas()
    if not ruta_actual or not nombre_nueva_categoria:
        print('No se puede crear la carpeta correspondiente a la categoria.')
        return 0

    ruta_nueva = Path(ruta_actual, nombre_nueva_categoria)
    if ruta_nueva.exists():
        print('Lo siento, ya existe esa categoría.')
        pausa()
        return 0

    ruta_nueva.mkdir()
    print('Se ha creado la nueva categoría.')
    pausa()


def eliminar_carpeta(categoria):
    lista_categorias = categorias()
    carpeta = lista_categorias[categoria][1]
    ruta = path_recetas()
    ruta_a_eliminar = Path(Path(ruta) / carpeta)
    ruta_a_eliminar.rmdir()


def ejecutar():
    opcion = -1
    while opcion != 6:
        opcion = seleccionar_opcion()
        match opcion:
            case 1:
                '''Leer Receta'''
                categoria = elegir_categoria()
                receta = seleccionar_receta(categoria)
                if len(receta) > 0:
                    leer_archivo(receta[1])
            case 2:
                '''Crear Receta'''
                categoria = elegir_categoria()
                nuevo_archivo(ruta_recetario, categorias[categoria][1])
            case 3:
                '''Crear categoria'''
                nueva_categoria()
            case 4:
                '''Eliminar receta'''
                categoria = elegir_categoria()
                receta = seleccionar_receta(categoria)
                if len(receta) > 0:
                    eliminar_archivo(receta[1])
            case 5:
                '''Eliminar categoria'''
                categoria = elegir_categoria()
                eliminar_carpeta(categoria)
                pausa()


def categorias():
    ruta_recetario = path_recetas()
    return list(enumerate(lista_carpetas(ruta_recetario)))


# PRINCIPAL
# Dar la Bienvenida al Usuario
system('cls')
print('*' * 50)
print('Bienvenido a la App Recetario. Aqui podras leer las recetas existentes, crear nuevas o eliminar recetas.')
print('*' * 50)

# Informar la ruta de acceso donde se encuentra la carpeta
info_recetas()
pausa()
ejecutar()
print('El Programa Recetario ha Finalizado!')

