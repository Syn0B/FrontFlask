"""
config.py - Configuracion centralizada de la aplicacion Flask.
"""

# URL base de la API REST que consume este frontend.
# La API generica en C# corre en el puerto 5034.
API_BASE_URL = "http://localhost:5034"

# Clave secreta para el manejo de sesiones y mensajes flash.
# Flask la necesita para firmar las cookies de sesion.
SECRET_KEY = "clave-secreta-flask-frontend-2024"