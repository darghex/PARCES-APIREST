from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from main import engine


Base = declarative_base()
Base.metadata.reflect(engine)

from sqlalchemy.orm import relationship, backref

class instancias_curso(Base):
	__table__ = Base.metadata.tables['instancias_curso']

class actividades(Base):
	__table__ = Base.metadata.tables['actividades']

class asignaciones(Base):
	__table__ = Base.metadata.tables['asignaciones']
	
class propuestas_matricula(Base):
	__table__ = Base.metadata.tables['propuestas_matricula']

class comentarios_propuesta(Base):
		__table__ = Base.metadata.tables['comentarios_propuesta']

class calificaciones(Base):
	__table__ = Base.metadata.tables['calificaciones']

class comentarios_instancia_curso(Base):
	__table__ = Base.metadata.tables['comentarios_instancia_curso']

class asistencias(Base):
 	__table__ = Base.metadata.tables['asistencias']
