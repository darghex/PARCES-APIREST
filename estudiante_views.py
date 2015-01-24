#!/usr/bin/python
from flask import request
from main import app, session, IES_REST_URL
from db import instancias_curso, propuestas_matricula, actividades, calificaciones, asignaciones
import json
import requests
from sqlalchemy import and_


@app.route("/instanciascurso/<int:curso>/",methods=['GET'])
def view_instancias_curso(curso):
	"""
	Lista las clases registradas de una asignatura
	"""
	
	instancias = session.query(instancias_curso).filter_by(curso = curso)

	response = []
	for instancia in instancias:
		response.append ({'id': instancia.id, 'tema': instancia.tema, 'corte': instancia.corte , 'fecha': instancia.fecha})

	return json.dumps(response)

@app.route("/estudiantes/<id_estudiante>/propuesta",methods=['GET'])	
def est_read_propuestas_matricula(id_estudiante):
	"""
	@retorna un ok en caso de que se halla ejecutado la operacion 
	@except status 500 en caso de presentar algun error

	"""

	propuestas =  session.query(propuestas_matricula.id, propuestas_matricula.tutor, propuestas_matricula.estado).filter_by(estudiante = id_estudiante)

	response = []

	for propuesta in propuestas:
		estado = True if propuesta.estado == 1 else False

		response.append({'id': propuesta.id, 'tutor': propuesta.tutor, 'estado': estado})

	return json.dumps({"propuesta": response})


@app.route("/estudiantes/<id_estudiante>/curso/<int:curso>/actividades",methods=['GET'])
def view_actividades(id_estudiante, curso):
	"""
	@retorna un ok en caso de que se halla ejecutado la operacion 
	@except status 500 en caso de presentar algun error
	
	"""


	try:
		
		instancias = session.query(instancias_curso.id, instancias_curso.tema, instancias_curso.corte, instancias_curso.fecha).filter_by(curso = curso).order_by("fecha desc")
		tema = []
		
		
		for instancia_db in instancias:
			
			actividad = []
			actividades_db = session.query(actividades.descripcion, calificaciones.valor).filter_by(instancias_curso_id = instancia_db.id).outerjoin(calificaciones, and_(actividades.id == calificaciones.actividades_id , calificaciones.estudiante == id_estudiante ))
		
			for actividad_db in actividades_db:
				actividad.append({'actividad': actividad_db.descripcion, 'calificacion': actividad_db.valor}) 
			tema.append({'tema': instancia_db.tema, 'id': instancia_db.id ,'corte': instancia_db.corte, 'fecha': str(instancia_db.fecha), 'actividades': actividad })


		return json.dumps({'instancias_curso': {'instancia': tema }})
	
	except Exception, e:
		return "Operacion No se pudo llevar a cabo", 500
	return "ok"







@app.route("/estudiantes/<id_estudiante>/tutor",methods=['GET'])
def get_tutor(id_estudiante):
	"""
	Carga el perfil del tutor
	@return: json {

					}
	"""
	
	asignaciones_desc = session.query(asignaciones.tutor).filter_by(estudiante = id_estudiante).first()
	
	
	parametros = { 'codigo': asignaciones_desc[0], 'token': request.args.get('token') }

	rq = requests.get( IES_REST_URL+"/profesor", params = parametros)
	return json.dumps(rq.json)
