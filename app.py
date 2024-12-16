import streamlit as st
import pandas as pd
import json
import datetime
from func.sesiones import cargarJSON

if 'sesionActual' not in st.session_state:
    st.session_state['sesionActual'] = []

st.title("Aplicación de Gestión de Tareas 📒")


st.header('Tareas:')
df = pd.DataFrame(st.session_state['sesionActual'])
st.dataframe(df, width=800)


with st.form("my_form"):
    st.subheader('Agregar Tareas')
    nombreTarea = st.text_input('Nombre', placeholder='Ingrese el nombre de la tarea...')
    descripcionTarea = st.text_input('Descripcion', placeholder='Ingrese la descripción de la tarea...')
    estado = st.checkbox('Finalizada?')

    submitted = st.form_submit_button("Agregar", use_container_width=True)
    if submitted:
        tarea = {
            "nombre": nombreTarea,
            "descripcion": descripcionTarea,
            "fecha_creacion": datetime.date.today(),
            "estado": estado
        }
        st.success(f'Tarea {nombreTarea} agregada exitosamente!')
        st.session_state['sesionActual'].append(tarea)
        st.rerun()
st.write("Outside the form")

if st.button('Ver JSON'):
    st.session_state['sesionActual'] = cargarJSON()
    st.rerun()
    