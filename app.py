from flask import Flask, request
from datetime import datetime
from usuario.py import Usuario
from operacion.py import Operacion
app = Flask(__name__)

BD = []
BD.append(Usuario("21345", "Arnaldo", 200, ["123", "456"]))
BD.append(Usuario("123", "Luisa", 400, ["456"]))
BD.append(Usuario("456", "Andrea", 300, ["21345"]))

def get_user_by_number(numero):
    for usuario in BD:
        if usuario.numero == numero:
            return usuario
    return None

@app.route('/billetera/contactos', methods=['GET'])
def contactos():
    numero = request.args.get('minumero')
    usuario = get_user_by_number(numero)
    if usuario:
        response = ""
        for contacto in usuario.contactos:
            contacto_usuario = get_user_by_number(contacto)
            if contacto_usuario:
                response += f"{contacto_usuario.numero}: {contacto_usuario.nombre}\n"
        return response
    else:
        return "Usuario no encontrado"

@app.route('/billetera/pagar', methods=['POST'])
def pagar():
    numero_origen = request.args.get('minumero')
    numero_destino = request.args.get('numerodestino')
    valor = float(request.args.get('valor'))
    usuario_origen = get_user_by_number(numero_origen)
    if usuario_origen:
        if usuario_origen.pagar(numero_destino, valor):
            return f"Realizado en {datetime.now().strftime('%d/%m/%Y')}"
        else:
            return "Usted no tiene el saldo suficiente para realizar esta operación. El destinatario no fue localizado"
    else:
        return "No se pudo encontrar el usuario de origen de petición"

@app.route('/billetera/historial', methods=['GET'])
def historial():
    numero = request.args.get('minumero')
    usuario = get_user_by_number(numero)
    if usuario:
        return usuario.historia()
    else:
        return "No se pudo encontrar el usuario"

if __name__ == '__main__':
    app.run()
