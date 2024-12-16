import streamlit as st
import json
import time


def recargar():
    time.sleep(0.7)
    st.rerun()

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
    
def guardarAlJSON(data):
    datos = cargarJSON()
    datos.append(data)
    with open('datos.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4, default=str)
    st.success('Tarea agregada en el JSON Exitosamente ! 🎉')
    
    
def descargarJSON():
    datos = cargarJSON()
    return json.dumps(datos)

def reemplazarJSON(datos):
    with open('datos.json', 'w') as archivo:
        jason = json.dumps(datos, indent=4)
        archivo.write(jason)
    st.success('JSON reemplazado!')