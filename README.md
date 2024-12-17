# Aplicación de Gestión de Tareas 📒

## Descripción

Este proyecto esta basado en un aplicativo de Gestión de Tareas, que nos puede servir para organizarnos con los pendientes que tengamos


---

## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso](#uso)
- [Características](#características)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Créditos](#créditos)
- [Recursos y Enlaces Adicionales](#recursos-y-enlaces-adicionales)

---

## Instalación

Sigue los pasos a continuación para configurar el proyecto en tu entorno local:

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/julandro/Aplicacion-Lista-de-Tareas-con-Python.git
   ```
2. **Navega al directorio del proyecto:**
   ```bash
   cd proyecto
   ```
3. **Crea y Activa un entorno virtual:**
   - Con `python` en la termina:

     ```bash
     python -m venv venv
     ```
   - Luego `Activalo`:
   
     ```bash
     venv/Scripts/activate
     ```

3. **Instala las dependencias o modulos del proyecto:**
   - Con `pip`:
     ```bash
     pip install -r requeriments.txt
     ```
   
---

## Uso

Una vez configurado y listo todo puedes ejecutar el proyecto:

- **Ejecución:**
  ```bash
  streamlit run ./app.py
  ```


## Características

#### Modos de uso
- [Sesion Actual]: Esta es un sesión que nos permite agregar y marcar tareas por un periodo de tiempo limitado. Y se perderan sus datos si recargas la página
- [JSON]: En este modo podemos interactuar directamente con un archivo JSON, por lo cual los datos perduraran por un periodo de tiempo ilimitado, tambien podremos ver las tareas agregadas al JSON, agregar tareas, marcarlas como realizadas y descargar el archivo 
- [Database]: En este modo interactuamos directamente con una base de datos sqlite en modo local, por lo cual los datos también perduraran por un periodo de tiempo ilimitado, podemos ver las tareas agregadas a la db, agregar tareas, marcarlas como realizadas y al hacerlo quedan eliminadas de la base de datos.

#### Manejo de Archivos
- [Descarga de JSON]: Con esta funcionalidad podremos descargar el json con el que estemos trabajando.
- [Importar JSON]: Esta funcionalidad nos permite visualizar un archivo JSON externo en la tabla.
- [Guardar el JSON]: Esta funcionalidad se nos muestra despues de ingresar un archivo JSON y nos permite reemplazar el archivo JSON externo por el actual 


---

### Tecnologías Utilizadas

- **Python en su totalidad**
- **Frontend:** [Streamlit]
- **Librerias/Modulos:** [Streamlit, Pandas, SQLalchemy]
- **Base de Datos:** [SQLite]

---



## Créditos

- **Autor:** Julian Alejandro Camacho Mendoza
- **Contacto:** julandro.mza@gmail
 Cel: 323 2304966


---

## Recursos y Enlaces Adicionales

- [Streamlit Documentacion](https://docs.streamlit.io/)
- [SQLAlchemy Documentacion](https://docs.sqlalchemy.org/en/20/)

