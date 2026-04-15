"""
api_service.py - Servicio generico que consume la API REST.
"""

import requests
from config import API_BASE_URL


class ApiService:
    """
    Servicio generico para consumir la API REST.

    Metodos:
        listar(tabla, limite)           → lista de diccionarios
        crear(tabla, datos, ...)        → (bool, str)
        actualizar(tabla, clave, ...)   → (bool, str)
        eliminar(tabla, clave, valor)   → (bool, str)
    """

    def __init__(self):
        self.base_url = API_BASE_URL

    # ──────────────────────────────────────────────
    # LISTAR: GET /api/{tabla}
    # ──────────────────────────────────────────────
    def listar(self, tabla, limite=None):
        try:
            url = f"{self.base_url}/api/{tabla}"
            params = {}
            if limite:
                params['limite'] = limite

            respuesta = requests.get(url, params=params)
            datos_json = respuesta.json()
            return datos_json.get("datos", [])

        except requests.RequestException as ex:
            print(f"Error al listar {tabla}: {ex}")
            return []

    # ──────────────────────────────────────────────
    # CREAR: POST /api/{tabla}
    # ──────────────────────────────────────────────
    def crear(self, tabla, datos, campos_encriptar=None):
        try:
            url = f"{self.base_url}/api/{tabla}"
            params = {}
            if campos_encriptar:
                params['camposEncriptar'] = campos_encriptar

            respuesta = requests.post(url, json=datos, params=params)
            contenido = respuesta.json()
            mensaje = contenido.get("mensaje", "Operacion completada.")
            return (respuesta.ok, mensaje)

        except requests.RequestException as ex:
            return (False, f"Error de conexion: {ex}")

    # ──────────────────────────────────────────────
    # ACTUALIZAR: PUT /api/{tabla}/{nombre_clave}/{valor_clave}
    # ──────────────────────────────────────────────
    def actualizar(self, tabla, nombre_clave, valor_clave, datos, campos_encriptar=None):
        try:
            url = f"{self.base_url}/api/{tabla}/{nombre_clave}/{valor_clave}"
            params = {}
            if campos_encriptar:
                params['camposEncriptar'] = campos_encriptar

            respuesta = requests.put(url, json=datos, params=params)
            contenido = respuesta.json()
            mensaje = contenido.get("mensaje", "Operacion completada.")
            return (respuesta.ok, mensaje)

        except requests.RequestException as ex:
            return (False, f"Error de conexion: {ex}")

    # ──────────────────────────────────────────────
    # ELIMINAR: DELETE /api/{tabla}/{nombre_clave}/{valor_clave}
    # ──────────────────────────────────────────────
    def eliminar(self, tabla, nombre_clave, valor_clave):
        try:
            url = f"{self.base_url}/api/{tabla}/{nombre_clave}/{valor_clave}"
            respuesta = requests.delete(url)
            contenido = respuesta.json()
            mensaje = contenido.get("mensaje", "Operacion completada.")
            return (respuesta.ok, mensaje)

        except requests.RequestException as ex:
            return (False, f"Error de conexion: {ex}")