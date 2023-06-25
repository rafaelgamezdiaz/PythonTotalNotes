from ProyectoCuentaBancaria.Persona import Persona
from os import system


class Cliente(Persona):

    def __init__(self, nombre, apellidos, numero_cuenta, balance):
        super().__init__(nombre, apellidos)
        self.numero_cuenta = numero_cuenta
        self.balance = float(balance)

    def __str__(self):
        data_cliente = f'Nombre y apellidos del cliente: {self.nombre} {self.apellidos}\n'
        data_cliente += f'Numero de cuenta: {self.numero_cuenta}\n'
        data_cliente += f'Balance: {self.balance}\n'
        return data_cliente

    def operacion_deposito_retiro(self, operacion):
        monto = ''
        while not monto.replace('.', '').isdigit():
            monto = input(f'Ingrese el monto para {operacion}:? ')

        if operacion == 'deposito':
            self.balance += float(monto)
        else:
            if float(monto) > self.balance:
                print('No tiene fondos suficientes para el retiro solicitado')
                return

            self.balance -= float(monto)

        # Redondeo a dos cifras
        self.balance = round(self.balance, 2)
        print(f'Balance actual: {self.balance}')

    def depositar(self):
        self.operacion_deposito_retiro('deposito')

    def retirar(self):
        self.operacion_deposito_retiro('retiro')
