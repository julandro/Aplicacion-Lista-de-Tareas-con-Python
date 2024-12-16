import streamlit as st
import pandas as pd
import json
import datetime
import copy
from func.sesiones import recargar, cargarJSON, guardarAlJSON


st.set_page_config(layout="wide")

if 'estados' not in st.session_state:
    st.session_state['estados'] = 0

if 'sesion' not in st.session_state:
    st.session_state['sesion'] = 'Sesion Actual'

if 'datosTabla' not in st.session_state:
    st.session_state['datosTabla'] = []

if 'sesionActual' not in st.session_state:
    st.session_state['sesionActual'] = []

st.title("Aplicación de Gestión de Tareas 📒")

st.columns(3)[1].subheader(f'Interactuando en {st.session_state["sesion"]}')
left, center, right = st.columns(3, border=True, gap='medium')

with left:
    st.columns(3)[1].subheader("Vistas")
    
    if st.button("Ver Sesión Actual", use_container_width=True):
        st.session_state['datosTabla'] = copy.deepcopy(st.session_state['sesionActual'])
        st.session_state['sesion'] = 'Sesion Actual'
        st.info('Cambiando a la Sesion Actual...')
        recargar()
        
    if st.button('Ver JSON', use_container_width=True):
        st.session_state['datosTabla'] = cargarJSON()
        st.session_state['sesion'] = 'JSON'
        st.info('Motrando y cambiando al JSON...')
        recargar()
        
    if st.button('Ver DataBase', use_container_width=True):
        st.warning('Falta Codearlo :P')

with center:
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
                "realizado": estado
            }
            
            
            if st.session_state['sesion']=='JSON':
                st.session_state['estados'] = guardarAlJSON(tarea)
                recargar()
            if st.session_state['sesion']=='Sesion Actual':
                st.session_state['datosTabla'].append(tarea)
                st.session_state['sesionActual'].append(tarea)
                st.success('Tarea agregada a la Sesion Actual Exitosamente ! 🎉')
                recargar()
            
            recargar()

with right:
    st.columns(3)[1].subheader("Opciones")

    if st.button('Descargar el JSON', use_container_width=True):
        st.warning('Falta codearlo 😝')

    
st.header('Tareas:')
df = pd.DataFrame(st.session_state['datosTabla'])
st.dataframe(df, width=800, use_container_width=True)
