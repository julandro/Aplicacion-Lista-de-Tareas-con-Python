import streamlit as st
import json

def cargarJSON():
    try:
        with open('datos.json', 'r') as archivo:
            contenido = archivo.read()
            if contenido.strip() == "":
                return []  # Si el archivo está vacío, devolvemos una lista vacía
            return json.loads(contenido)
    except FileNotFoundError:
        return []  # Si el archivo no existe, devolvemos una lista vacía
    except json.JSONDecodeError:
        return []  # Si el archivo tiene errores, devolvemos una lista vacía
