from sqlalchemy import create_engine, Column, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

# Ruta de la base de datos
db_path = os.path.join(os.path.dirname(__file__), '..', 'predicciones.db')
engine = create_engine(f'sqlite:///{db_path}', echo=False)

# Declarar modelo base
Base = declarative_base()

# Definición de la tabla de predicciones
class Prediccion(Base):
    __tablename__ = 'predicciones'
    id = Column(Integer, primary_key=True)
    ciclismo = Column(Float)
    fumadores = Column(Float)
    resultado = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Crear tabla si no existe
Base.metadata.create_all(engine)

# Crear sesión
Session = sessionmaker(bind=engine)
