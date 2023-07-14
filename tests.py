import unittest
from flask import Flask
from datetime import datetime
import app.py

app = Flask(__name__)

class UnitTests(unittest.TestCase):

    def test_contactos_exito(self):
        # Caso de prueba: Obtener los contactos exitosamente
        response = self.app.get('/billetera/contactos?minumero=21345')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), "123: Luisa\n456: Andrea\n")

    def test_pagar_exito(self):
        # Caso de prueba: Pago exitoso dentro del límite diario
        response = self.app.post('/billetera/pagar?minumero=123&numerodestino=456&valor=50')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Pago exitoso realizado en", response.data.decode('utf-8'))

    def test_pagar_error_destino_no_encontrado(self):
        # Caso de prueba: Error - Destino no encontrado
        response = self.app.post('/billetera/pagar?minumero=123&numerodestino=789&valor=50')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), "El destinatario no fue localizado")

    def test_pagar_error_saldo_insuficiente(self):
        # Caso de prueba: Error - Saldo insuficiente para la transferencia
        response = self.app.post('/billetera/pagar?minumero=123&numerodestino=456&valor=500')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), "Usted no tiene el saldo suficiente para realizar esta operación")

    def test_historial_exito(self):
        # Caso de prueba: Obtener historial exitosamente
        response = self.app.get('/billetera/historial?minumero=123')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Saldo de Luisaus", response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
