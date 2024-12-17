# Aplicación de Gestión de Tareas 📒

#### Vista Previa
![Vista previa del proyecto](assets/img/preview.png)


## Descripción

Este proyecto esta basado en un aplicativo de Gestión de Tareas, que nos puede servir para organizarnos con los pendientes que tengamos


---

## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso](#uso)
- [Características](#características)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Puntaje Sonarqube](#puntaje-sonarqube)
- [Créditos](#créditos)
- [Recursos y Enlaces Adicionales](#recursos-y-enlaces-adicionales)

---

### Requisitos Previos
1. **Python**
        
        Tener instalado Python en su versión 3.11.9

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
   - Con `python` en la terminal:

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
- **[Sesion Actual]:** Esta es un sesión que nos permite agregar y marcar tareas por un periodo de tiempo limitado. Y se perderan sus datos si recargas la página
- **[JSON]:** En este modo podemos interactuar directamente con un archivo JSON, por lo cual los datos perduraran por un periodo de tiempo ilimitado, tambien podremos ver las tareas agregadas al JSON, agregar tareas, marcarlas como realizadas y descargar el archivo 
- **[Database]:** En este modo interactuamos directamente con una base de datos sqlite en modo local, por lo cual los datos también perduraran por un periodo de tiempo ilimitado, podemos ver las tareas agregadas a la db, agregar tareas, marcarlas como realizadas y al hacerlo quedan eliminadas de la base de datos.

#### Manejo de Archivos
- **[Descarga de JSON]:** Con esta funcionalidad podremos descargar el json con el que estemos trabajando.
- **[Importar JSON]:** Esta funcionalidad nos permite visualizar un archivo JSON externo en la tabla.
- **[Guardar el JSON]:** Esta funcionalidad se nos muestra despues de ingresar un archivo JSON y nos permite reemplazar el archivo JSON externo por el actual 


---

### Tecnologías Utilizadas

- **Python en su totalidad**
- **Frontend:** Streamlit
- **Librerias/Modulos:** Streamlit, Pandas, SQLalchemy
- **Base de Datos:** SQLite

---

## Estructura del Proyecto

```plaintext
APP-LISTADETAREAS-PYTHON/
├── data/                # Directorio donde se almacena el JSON
│   ├── datos.json     # El archivo .json para almacenar tareas
├── db/                # Carpeta con archivos relacionados a la base de datos
│   ├── db.db           # La base de datos SQL local
│   ├── db.py     # Conexión a la base de datos junto con funciones importantes de conexion
├── functions/                # Directorio que aloja las funcionalidades del proyecto
│   ├── functions.py     # Funciones de manejo de datos y archivos
├── app.py              # Código Fuente Principal 
├── requeriments.txt        # Modulos necesarios
├── README.md           # Documentación principal
```


## Puntaje SonarQube

![Vista previa del proyecto](assets/img/sonar.png)


## Créditos

- **Autor:** Julian Alejandro Camacho Mendoza
- **Contacto:** julandro.mza@gmail
 Cel: 323 2304966


---

## Recursos y Enlaces Adicionales

- [Streamlit Documentacion](https://docs.streamlit.io/)
- [SQLAlchemy Documentacion](https://docs.sqlalchemy.org/en/20/)

