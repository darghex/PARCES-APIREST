#!/usr/bin/python
from flask import request
from main import app, session
from db import comentarios_propuesta,calificaciones, comentarios_instancia_curso, actividades
import json
from sqlalchemy import and_


@app.route("/")
def index():
	"""
	vista principal
	"""        
	return "<i>API RestFull PARCES Version 0.1</i>"


@app.route("/prematricula/<int:id_prematricula>/comentarios",methods=['GET'])
def read_comentarios_propuesta(id_prematricula):
	

	comentarios =  session.query(comentarios_propuesta.mensaje, comentarios_propuesta.autor, comentarios_propuesta.fecha).filter_by(propuestas_matricula_id = id_prematricula)
	response = []

	for comentario in comentarios:
		
		response.append({'mensaje': comentario.mensaje, 'autor': comentario.autor.decode("8859"), 'fecha': str(comentario.fecha)})

	print response
	return json.dumps({'response': {'id': id_prematricula, 'comentarios': response }})



@app.route("/prematricula/<int:id_prematricula>/comentarios",methods=['POST'])
def create_comentarios_propuesta(id_prematricula):
	"""
	@retorna un ok en caso de que se halla ejecutado la operacion 
	@except status 500 en caso de presentar algun error

	"""
	from datetime import datetime
	
	if request.method == 'POST':
		try:

			values = json.loads( request.data.decode('8859') )
			mensaje = values['com_mensaje']
			autor = values['com_usuario']
			fecha = datetime.today()
			
			comentario = comentarios_propuesta(propuestas_matricula_id = id_prematricula , mensaje = mensaje , autor = autor, fecha = fecha)
			session.add(comentario)
			session.commit()

		except Exception, e:
			session.rollback()
			return "Operacion No se pudo llevar a cabo", 500
		return "ok"
	else:
		return "Operacion No se pudo llevar a cabo", 500


@app.route("/estudiante/<id_estudiante>/instanciascurso/<int:id_instancia>/actividad/<int:id_actividad>/calificacion",methods=['GET'])
def read_est_tut_calficaciones(id_instancia,id_estudiante,id_actividad):

	calificaciones_desc = session.query(calificaciones.valor, calificaciones.estudiante).filter_by(actividades_id = id_actividad, estudiante = id_estudiante)
	
	response = []

	for calificacion in calificaciones_desc:
		response.append({'actividad': id_actividad, 'estudiante': calificacion.estudiante, 'calificacion': calificacion.valor})

	return json.dumps(response)



@app.route("/instancia_curso/<int:id_instancia>/comentarios",methods=['GET'])
def read_comentarios_instancia(id_instancia):
	
	
	comentarios =  session.query(comentarios_instancia_curso.mensaje, comentarios_instancia_curso.autor, comentarios_instancia_curso.fecha).filter_by(instancias_curso_id = id_instancia)
	response = []

	for comentario in comentarios:
		
		response.append({'mensaje': comentario.mensaje, 'autor': comentario.autor.decode("8859"), 'fecha': str(comentario.fecha)})

	print response
	return json.dumps({'response': {'id': id_instancia, 'comentarios': response }})



@app.route("/instancia_curso/<int:id_instancia>/comentarios",methods=['POST'])
def create_comentarios_instancia(id_instancia):
	"""
	@retorna un ok en caso de que se halla ejecutado la operacion 
	@except status 500 en caso de presentar algun error

	"""
	from datetime import datetime
	
	if request.method == 'POST':
		try:
			
			values = json.loads( request.data.decode('8859') )
			mensaje = values['com_mensaje']
			autor = values['com_usuario']
			fecha = datetime.today()
			
			comentario = comentarios_instancia_curso(instancias_curso_id = id_instancia , mensaje = mensaje , autor = autor, fecha = fecha)
			session.add(comentario)
			session.commit()

		except Exception, e:
			session.rollback()
			return "Operacion No se pudo llevar a cabo", 500
		return "ok"
	else:
		return "Operacion No se pudo llevar a cabo", 500



@app.route("/instancia_curso/<int:id_instancia>/actividades/<id_estudiante>",methods=['GET'])
def view_actividades_estudiante( id_instancia, id_estudiante):
	"""
	@retorna un ok en caso de que se halla ejecutado la operacion 
	@except status 500 en caso de presentar algun error
	
	"""
	

	try:
		actividad = []
		actividades_db = session.query(actividades.descripcion, calificaciones.valor).filter_by(instancias_curso_id = id_instancia).outerjoin(calificaciones, and_(actividades.id == calificaciones.actividades_id , calificaciones.estudiante == id_estudiante ))
		
		for actividad_db in actividades_db:
			
			actividad.append({'actividad': actividad_db.descripcion, 'calificacion': actividad_db.valor}) 
		
		return json.dumps({'instancias_curso': {'instancia': id_instancia, 'actividades': actividad  }})
	
	except Exception, e:
		return str(e)
		return "Operacion No se pudo llevar a cabo", 500
	return "ok"

