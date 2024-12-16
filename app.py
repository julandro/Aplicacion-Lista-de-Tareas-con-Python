import streamlit as st
import pandas as pd
import json
import datetime
import copy
from functions.functions import recargar, cargarJSON, guardarAlJSON, descargarJSON, reemplazarJSON


st.set_page_config(layout="wide")

if 'estados' not in st.session_state:
    st.session_state['estados'] = None

if 'estadoBtn' not in st.session_state:
    st.session_state['estadoBtn'] = False

if 'sesion' not in st.session_state:
    st.session_state['sesion'] = 'Sesion Actual'

if 'datosTabla' not in st.session_state:
    st.session_state['datosTabla'] = []

if 'sesionActual' not in st.session_state:
    st.session_state['sesionActual'] = []

st.title("Aplicación de Gestión de Tareas 📒")

left, center, right = st.columns(3, border=True, gap='medium')

with left:
    st.columns(3)[1].subheader("Vistas")
    
    if st.button("Ver Sesión Actual", use_container_width=True):
        st.session_state['datosTabla'] = copy.deepcopy(st.session_state['sesionActual'])
        st.session_state['sesion'] = 'Sesion Actual'
        st.session_state['estadoBtn'] = False
        
        st.info('Cambiando a la Sesion Actual...')
        recargar()
        
    if st.button('Ver JSON', use_container_width=True):
        st.session_state['datosTabla'] = cargarJSON()
        st.session_state['sesion'] = 'JSON'
        st.session_state['estadoBtn'] = False
        
        st.info('Motrando y cambiando al JSON...')
        recargar()
        
    if st.button('Ver DataBase', use_container_width=True):
        st.warning('Falta Codearlo :P')

with right:
    st.columns(3)[1].subheader("Opciones")
    
    #st.session_state['estados'] = descargarJSON()
    
    st.download_button(
        label="Descargar el JSON",
        data=descargarJSON(),
        file_name="data.json",
        use_container_width=True
    )
    
    archivo = st.file_uploader('Importar JSON',type=['json'], help='Solo archivos JSON')
    
    if archivo is not None:
        if archivo.name.endswith('.json'):
            try:
                datos = json.load(archivo)
                st.session_state['datosTabla'] = datos
                st.session_state['estadoBtn'] = True

                st.session_state['sesion'] = f'Archivo {archivo.name}'
                st.success(f'Visualizando {archivo.name}')
                if st.button('Guardar al JSON', use_container_width=True):
                    st.session_state['estados']= reemplazarJSON(datos)
                
            except json.JSONDecodeError as e:
                st.error('Error al leer el archivo JSON')

with center:
    with st.form("my_form"):
        st.subheader('Agregar Tareas')
        nombreTarea = st.text_input('Nombre', placeholder='Ingrese el nombre de la tarea...')
        descripcionTarea = st.text_input('Descripcion', placeholder='Ingrese la descripción de la tarea...')
        realizado = st.checkbox('Finalizada?')

        submitted = st.form_submit_button("Agregar", use_container_width=True, disabled=st.session_state['estadoBtn'])
        if submitted:
            tarea = {
                "nombre": nombreTarea,
                "descripcion": descripcionTarea,
                "fecha_creacion": datetime.date.today(),
                "realizado": realizado
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

    
st.header('Tareas:')

st.info(f'Interactuando en {st.session_state["sesion"]}')
df = pd.DataFrame(st.session_state['datosTabla'])
st.dataframe(df, width=800, use_container_width=True)
