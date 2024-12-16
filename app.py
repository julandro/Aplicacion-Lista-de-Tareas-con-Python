import streamlit as st
import pandas as pd
import json
import datetime
import copy
from functions.functions import recargar, cargarJSON, guardarAlJSON, descargarJSON, reemplazarJSON
from db.db import crearTareaDB, mostrarTareasDB, reemplazarTareasDB, eliminarTareaDB

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
        st.session_state['datosTabla'] = mostrarTareasDB()
        st.session_state['sesion'] = 'Database'
        st.session_state['estadoBtn'] = False

        st.info('Motrando y cambiando a la Database...')
        recargar()
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
                    st.success('JSON reemplazado correctamente')
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
                "fecha_creacion": datetime.datetime.today(),
                "realizado": realizado
            }
            
            
            if st.session_state['sesion']=='JSON':
                st.session_state['estados'] = guardarAlJSON(tarea)
                st.toast('La vista de la tabla del JSON no se actualiza automaticamente')
                
            if st.session_state['sesion']=='Sesion Actual':
                st.session_state['datosTabla'].append(tarea)
                st.session_state['sesionActual'].append(tarea)
                st.success('Tarea agregada a la Sesion Actual Exitosamente ! 🎉')
                recargar()
            if st.session_state['sesion']=='Database':
                st.session_state['estados'] = crearTareaDB(tarea['nombre'], tarea['descripcion'], tarea['realizado'])
                recargar()
                
            
    
st.header('Tareas:')

st.info(f'Interactuando en {st.session_state["sesion"]}')

df = pd.DataFrame(st.session_state['datosTabla'])

dtf = st.data_editor(
    df,
    column_config={
        "realizado": st.column_config.CheckboxColumn(
            "realizado",
            default=False,
            disabled=False,
        ),
    },
    disabled=['nombre', 'descripcion', 'fecha_creacion'],
    use_container_width=True
)

if dtf is not st.empty:
    for indice, columna in dtf.iterrows():
        if columna['realizado'] != df.loc[indice, 'realizado']:
            
            df.loc[indice, 'realizado'] = columna['realizado']
            
            
            st.balloons()
            if st.session_state['sesion']=='Sesion Actual':
                st.session_state['sesionActual'][indice]['realizado'] = columna['realizado']
                recargar()
                
            elif st.session_state['sesion'] == 'JSON':
                datosJson = cargarJSON()
                datosJson[indice]['realizado'] = columna['realizado']
                reemplazarJSON(datosJson)
            
            elif st.session_state['sesion'] == 'Database':
                tareas = mostrarTareasDB()
                tareas[indice]['realizado'] = columna['realizado']
                reemplazarTareasDB(tareas[indice]['id'], tareas[indice])
                st.success('Cambios en la Database!')
                if tareas[indice]['realizado'] == True:
                    st.error(f'Tarea {tareas[indice]["nombre"]} Eliminada :D')
                    eliminarTareaDB(tareas[indice]['id'])
                