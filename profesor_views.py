#!/usr/bin/python
from flask import request
from main import app, session
from db import instancias_curso,actividades,calificaciones, asistencias
import json

@app.route("/profesor/<int:id_docente>/curso/<int:curso>/instanciascurso",methods=['GET'])
def read_instancias_curso(id_docente,curso):
	"""
	Lista las clases registradas de una curso
	@return json: {"curso": {"id": 1, "curso:" string , "instancias": 
					[
						{"id": int, "tema": string}, 
						{"id": int, "tema": string }, 
						.....
					]
					}
				}

	"""

	#FIXME AGREGAR EL CAMPO ID DOCENTE A A TABLA INSTANCIAS CURSO
	instancias = session.query(instancias_curso.id, instancias_curso.tema).filter_by(curso = curso)
	response = []
	
	for instancia in instancias:
		response.append(  {'id': instancia.id, 'tema': instancia.tema })

	return json.dumps({"curso": {"id": curso, "instancias": response } })


@app.route("/profesor/<int:id_docente>/curso/<int:curso>/instanciascurso",methods=['POST'])
def create_instancias_curso(id_docente,curso):
	"""
	@retorna un ok en caso de que se halla ejecutado la operacion 
	@except status 500 en caso de presentar algun error

	"""
	if request.method == 'POST':
		try:
			
			tema = request.form.get('ic_tema')
			corte = request.form.get('ic_corte')
			fecha = request.form.get('ic_fecha')
			curso = int(request.form.get('ic_curso'))
			
			instancia = instancias_curso(tema = tema , corte = corte , fecha = fecha , curso = curso)
			session.add(instancia)
			session.commit()

		except Exception, e:
			session.rollback()
			return "Operacion No se pudo llevar a cabo", 500
		return "ok"
	else:
		return "Operacion No se pudo llevar a cabo", 500
	


@app.route("/profesor/<int:id_docente>/curso/<int:curso>/instanciascurso/<int:id_instancia>",methods=['PUT'])
def update_instancias_curso(id_docente,curso,id_instancia):
	"""
	@retorna un ok en caso de que se halla ejecutado la operacion 
	@except status 500 en caso de presentar algun error
	
	"""
	if request.method == 'PUT':
		try:
			
			
			tema = request.form.get('ic_tema')
			corte = request.form.get('ic_corte')
			fecha = request.form.get('ic_fecha')
			
			
			instancia = session.query(instancias_curso).filter_by(id = id_instancia).update({instancias_curso.tema : tema, instancias_curso.corte  : corte , instancias_curso.fecha : fecha})
			session.commit()


			

			#instancia = instancias_curso(tema = tema , corte = corte , fecha = fecha , curso = curso)
			#session.add(instancia)
			#session.commit()

		except Exception, e:
			session.rollback()
			return "Operacion No se pudo llevar a cabo", 500
		return "ok"
	else:
		return "Operacion No se pudo llevar a cabo", 500
	


@app.route("/profesor/<int:id_docente>/curso/<int:curso>/instanciascurso/<int:id_instancia>",methods=['DELETE'])
def delete_instancias_curso(id_docente,curso,id_instancia):
	"""
	@retorna un ok en caso de que se halla ejecutado la operacion 
	@except status 500 en caso de presentar algun error
	
	"""
	if request.method == 'DELETE':
		try:
			
			
			
			instancia = session.query(instancias_curso).filter_by(id = id_instancia).delete()
			
			session.commit()


		except Exception, e:
			session.rollback()
			return "Operacion No se pudo llevar a cabo", 500
		return "ok"
	else:
		return "Operacion No se pudo llevar a cabo", 500


@app.route("/profesor/<int:id_docente>/instanciascurso/<int:id_instancia>/actividad",methods=['GET'])
def read_actividades(id_docente, id_instancia):
	"""
	@retorna un ok en caso de que se halla ejecutado la operacion 
	@except status 500 en caso de presentar algun error
	
	"""


	try:
		
		instancias = session.query(instancias_curso.tema).filter_by(id = id_instancia).limit(1)
		tema = []
	
		for instancia_db in instancias:
			tema.append({'tema': instancia_db.tema, 'id': id_instancia })


		actividad = []
		actividades_db = session.query(actividades.descripcion, actividades.id).filter_by(instancias_curso_id = id_instancia)	
		
		for actividad_db in actividades_db:
			actividad.append({'actividad': actividad_db.descripcion, 'id': actividad_db.id }) 


		return json.dumps({'instanciacurso': {'instancia': tema ,'actividades': actividad}})
	
	except Exception, e:
		return "Operacion No se pudo llevar a cabo", 500
	return "ok"

@app.route("/profesor/<int:id_docente>/instanciascurso/<int:id_instancia>/actividad",methods=['POST'])
def create_actividades(id_docente, id_instancia):
	"""
	@retorna un ok en caso de que se halla ejecutado la operacion 
	@except status 500 en caso de presentar algun error
	
	"""

	if request.method == 'POST':

		try:
			
			descripcion = request.form.get('a_descripcion')

			actividad = actividades(instancias_curso_id = id_instancia, descripcion = descripcion)
			session.add(actividad)

			session.commit()
		
		except Exception, e:
			session.rollback()
			return "Operacion No se pudo llevar a cabo", 500
		return "ok"

	else:
		return "Operacion No se pudo llevar a cabo", 500

@app.route("/profesor/<int:id_docente>/instanciascurso/<int:id_instancia>/actividad/<int:id_actividad>",methods=['PUT'])
def update_actividades(id_docente,  id_instancia, id_actividad):
	"""
	@retorna un ok en caso de que se halla ejecutado la operacion 
	@except status 500 en caso de presentar algun error
	
	"""

	if request.method == 'PUT':

		try:
			
			descripcion = request.form.get('a_descripcion')

			actividades_db = session.query(actividades.descripcion).filter_by(id = id_actividad).update({actividades.descripcion : descripcion})	
			session.commit()
		
		except Exception, e:
			session.rollback()
			return "Operacion No se pudo llevar a cabo", 500
		return "ok"

	else:
		return "Operacion No se pudo llevar a cabo", 500

@app.route("/profesor/<int:id_docente>/instanciascurso/<int:id_instancia>/actividad/<int:id_actividad>",methods=['DELETE'])
def delete_actividades(id_docente, id_instancia, id_actividad):
	"""
	@retorna un ok en caso de que se halla ejecutado la operacion 
	@except status 500 en caso de presentar algun error
	
	"""

	if request.method == 'DELETE':

		try:
			
			

			actividades_db = session.query(actividades).filter_by(id = id_actividad).delete()
			session.commit()
		
		except Exception, e:
			session.rollback()
			return "Operacion No se pudo llevar a cabo", 500
		return "ok"

	else:
		return "Operacion No se pudo llevar a cabo", 500


@app.route("/profesor/<int:id_docente>/curso/<int:curso>/instanciascurso/<int:id_instancia>/tutor/<int:id_tutor>/estudiante/<id_estudiante>/actividad/<int:id_actividad>/calificacion",methods=['GET'])
def read_calificaciones(id_docente, curso, id_instancia,id_tutor,id_estudiante,id_actividad):

	calificaciones_desc = session.query(calificaciones.valor).filter_by(actividades_id = id_actividad)
	
	response = []

	for calificacion in calificaciones_desc:
		response.append({'actividad': id_actividad, 'estudiante': id_estudiante, 'calificacion': calificacion.valor})

	return json.dumps(response)

@app.route("/profesor/<int:id_docente>/curso/<int:curso>/instanciascurso/<int:id_instancia>/tutor/<int:id_tutor>/estudiante/<id_estudiante>/actividad/<int:id_actividad>/calificacion",methods=['POST'])
def create_calficaciones(id_docente, curso, id_instancia,id_tutor,id_estudiante,id_actividad): 
	"""
	@retorna un ok en caso de que se halla ejecutado la operacion 
	@except status 500 en caso de presentar algun error
	
	"""

	if request.method == 'POST':
		try:
			
			nota = request.form.get('ca_nota')
			
			calificacion = calificaciones(actividades_id = id_actividad , estudiante = id_estudiante , tutor = id_tutor, valor = nota)
			session.add(calificacion)
			session.commit()

		except Exception, e:
			session.rollback()
			return "Operacion No se pudo llevar a cabo", 500
		return "ok"
	else:
		return "Operacion No se pudo llevar a cabo", 500

@app.route("/profesor/<int:id_docente>/curso/<int:curso>/instanciascurso/<int:id_instancia>/tutor/<int:id_tutor>/estudiante/<id_estudiante>/actividad/<int:id_actividad>/calificacion/<int:id_calificacion>",methods=['PUT'])
def create_calficaciones(id_docente, curso, id_instancia,id_tutor,id_estudiante,id_actividad,id_calificacion):

	"""
	@retorna un ok en caso de que se halla ejecutado la operacion 
	@except status 500 en caso de presentar algun error
	
	"""

	if request.method == 'PUT':

		try:
			
			nota = request.form.get('ca_nota')

			calificaciones_desc = session.query(calificaciones.valor).filter_by(id = id_calificacion).update({calificaciones.valor : nota})	
			session.commit()
		
		except Exception, e:
			session.rollback()
			return "Operacion No se pudo llevar a cabo", 500
		return "ok"

	else:
		return "Operacion No se pudo llevar a cabo", 500 



@app.route("/profesor/<int:id_profesor>/instancia/<int:id_instancia>/asistencia", methods=['POST'])
def registrar_asistencia(id_profesor, id_instancia):
	"""
	@retorna un ok en caso de que se halla ejecutado la operacion 
	@except status 500 en caso de presentar algun error

	"""
	from datetime import datetime
	import pdb
	pdb.set_trace()
	if request.method == 'POST':
		try:

			session.query(asistencias).filter_by(instancias_curso_id = id_instancia).delete()
			session.commit()
			values = json.loads( request.data.decode('8859') )
			for  estudiante in values.get('estudiantes') :
				asistencia = asistencias(estudiante = estudiante , instancias_curso_id = id_instancia)
				session.add(asistencia)
			session.commit()

		except Exception, e:
			session.rollback()
			return "Operacion No se pudo llevar a cabo", 500
		return "ok"
	else:
		return "Operacion No se pudo llevar a cabo", 500


@app.route("/profesor/<int:id_profesor>/instancia/<int:id_instancia>/asistencia", methods=['GET'])
def read_asistencia(id_profesor, id_instancia):

	rows = session.query(asistencias.estudiante).filter_by(instancias_curso_id = id_instancia).order_by(asistencias.estudiante)
	
	response = []

	for row in rows:
		response.append({'estudiante': row.estudiante })

	return json.dumps({"asistencia": { "instancia_curso": id_instancia, "estudiantes": response } } )
