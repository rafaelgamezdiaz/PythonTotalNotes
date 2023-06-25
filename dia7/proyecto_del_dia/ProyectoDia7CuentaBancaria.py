# Proyecto del Dia 7: CUENTA BANCARIA

from ProyectoCuentaBancaria.Cliente import Cliente
from ProyectoCuentaBancaria.Core import *
from os import system


def registro_cliente():
    """Registro del cliente"""

    divisor('Registro del Cliente')
    nombre = ''
    numero_cuenta = ''
    balance = ''

    while not nombre:
        nombre = input('Ingrese el nombre del cliente:? ')
    apellidos = input('Apellidos del cliente:? ')

    while not numero_cuenta and not balance.isdecimal():
        numero_cuenta = input('Numero de Cuenta:? ')
        balance = input('Balance actual:? ')

    return Cliente(nombre, apellidos, numero_cuenta, balance)


def inicio():
    """Inicio del Programa"""

    # Configuraciones iniciales de cuentas
    lista_opciones = ['Depositar', 'Retirar', 'Salir']
    indices_opciones = [str(indice + 1) for indice, _ in enumerate(lista_opciones)]

    presentacion()

    # Registro del Cliente
    cliente = registro_cliente()
    pausa()

    # Operaciones Bancarias
    system('cls')
    accion = None
    while accion != '3':  # '3' corresponde a la acción de Salir
        divisor('ACCIONES')
        for indice, valor in list(enumerate(lista_opciones)):
            print(f'[{indice + 1}] - {valor}')

        accion = input('Elija una opción:? ')
        while accion not in indices_opciones:
            system('cls')
            accion = input('Elija una opción:? ')

        system('cls')
        match accion:
            case '1':
                divisor('DEPOSITO')
                cliente.depositar()
            case '2':
                divisor('RETIRO')
                cliente.retirar()
            case '3':
                print('Chao ...')

        pausa()
        system('cls')


## INICIO DEL PROGRAMA
system('cls')
inicio()
