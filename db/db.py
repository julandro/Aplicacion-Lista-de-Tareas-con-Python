import sqlalchemy
import sqlalchemy.orm
import datetime

from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime


engine = create_engine('sqlite:///db/db.db')

Base = declarative_base()

class Tarea(Base):
    __tablename__ = 'tareas'
    
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=True)
    nombre = Column(String, nullable=True)
    descripcion = Column(String, nullable=True)
    fecha_creacion = Column(DateTime, default=datetime.datetime.today())
    realizado = Column(Boolean, default=False)
    
Base.metadata.create_all(engine)

Sesion = sessionmaker(bind=engine)
sesion = Sesion()

def crearTareaDB(nombre='', descripcion='', realizado=False):
    nueva_tarea = Tarea(nombre=nombre, descripcion=descripcion, realizado=realizado)
    sesion.add(nueva_tarea)
    sesion.commit()    

def eliminarTareaDB(id):
    tarea = sesion.query(Tarea).filter_by(id=id).first()
    sesion.delete(tarea)
    sesion.commit()
    
def mostrarTareasDB():
    tareas = sesion.query(Tarea).all()
    listaTareas = []
    for tarea in tareas:
        listaTareas.append({
            'id': tarea.id,
            'nombre': tarea.nombre,
            'descripcion': tarea.descripcion,
            'fecha_creacion': tarea.fecha_creacion,
            'realizado': tarea.realizado
        })
    return listaTareas

def reemplazarTareasDB(id, datos):
    sesion.query(Tarea).filter_by(id=id).update(datos)
    sesion.commit()
    