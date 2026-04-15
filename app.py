"""
app.py - Punto de entrada de la aplicacion Flask.
"""

from flask import Flask
from config import SECRET_KEY

# Crear la aplicacion Flask
app = Flask(__name__)

# La clave secreta es necesaria para los mensajes flash (alertas)
app.secret_key = SECRET_KEY

# Los Blueprints se registran aqui (los crearemos en las siguientes partes)
# from routes.home import bp as home_bp
# app.register_blueprint(home_bp)

if __name__ == '__main__':
    # Puerto 5100 para no chocar con la API (puerto 5034)
    # debug=True recarga automaticamente al guardar cambios
    app.run(debug=True, port=5100)