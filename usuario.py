from operacion.py import Operacion
from app import get_user_by_number
from datetime import datetime

class Usuario:
    def __init__(self, numero, nombre, saldo, contactos):
        self.numero = numero
        self.nombre = nombre
        self.saldo = saldo
        self.contactos = contactos
        self.operaciones = []

    def historia(self):
        historial = f"Saldo de {self.nombre}: {self.saldo}\nOperaciones de {self.nombre}\n"
        for operacion in self.operaciones:
            fecha = operacion.fecha.strftime('%d/%m/%Y')
            historial += f"{operacion.tipo}: {operacion.valor} {'a' if operacion.tipo == 'pago_recibido' else 'de'} {operacion.numero_origen} el {fecha}\n"
        return historial

    def pagar(self, destino, valor):
        if destino in self.contactos and self.saldo >= valor:
            self.saldo -= valor
            operacion = Operacion(self.numero, destino, datetime.now(), valor, 'pago_realizado')
            destino_usuario = get_user_by_number(destino)
            destino_usuario.operaciones.append(operacion)
            return True
        else:
            return False