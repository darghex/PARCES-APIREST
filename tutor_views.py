#!/usr/bin/python
from flask import request
from main import app, session, IES_REST_URL
from db import asignaciones, propuestas_matricula
import json
import requests


@app.route("/tutor/<int:id_tutor>/estudiantes",methods=['GET'])
def read_asigaciones(id_tutor):
	"""
	Carga los estudiantes asignados a un tutor
	@return: json {

					}
	"""

	asignaciones_desc = session.query(asignaciones.estudiante).filter_by(tutor = id_tutor)
	
	""" para debug
	import pdb
	pdb.set_trace()
	"""
	

	parametros = {}
	for i, row in enumerate(asignaciones_desc):		
		parametros.update( { i: row[0]})

	parametros.update({'token': request.args.get('token')})
	rq = requests.get( IES_REST_URL+"/estudiantes", params = parametros)
	return json.dumps(rq.json)

@app.route("/tutor/<int:id_tutor>/estudiantes",methods=['POST'])
def create_asigaciones(id_tutor):
	"""
	@retorna un ok en caso de que se halla ejecutado la operacion 
	@except status 500 en caso de presentar algun error

	"""
	if request.method == 'POST':
		try:
			
			estudiante = request.form.get('as_estudiante')
			fecha = request.form.get('as_fecha')
			
			
			asignacion_db = asignaciones(tutor = id_tutor , estudiante = estudiante , fecha = fecha)
			session.add(asignacion_db)
			session.commit()

		except Exception, e:
			session.rollback()
			return "Operacion No se pudo llevar a cabo", 500
		return "ok"
	else:
		return "Operacion No se pudo llevar a cabo", 500

@app.route("/tutor/<int:id_tutor>/estudiantes/<id_estudiante>",methods=['PUT'])
def create_asigaciones(id_tutor, id_estudiante):


	if request.method == 'PUT':
		try:
			estudiante = request.form.get('as_estudiante')
			fecha = request.form.get('as_fecha')

			#FIXEME: LA TABLA ASIGNACIONES TIENE COMO LLAVE PRIMARIA LA FECHA, ETONCES LAS BUSQUEDAS PARA UPDATE Y DELETE LAS REALIZO
			#POR LA FECHA

			asignaciones_desc = session.query(asignaciones).filter_by(fecha = fecha).update({asignaciones.estudiante: estudiante})
			session.commit()
		except Exception, e:
			session.rollback()
			return "Operacion No se pudo llevar a cabo", 500
		return "ok"
	else:
		return "Operacion No se pudo llevar a cabo", 500

@app.route("/tutor/<int:id_tutor>/estudiantes/<id_estudiante>/fecha/<fecha>",methods=['DELETE'])
def create_asigaciones(id_tutor, id_estudiante,fecha):

	#FIXME AGREGE COMO PARAMETRO LA FECHA DEBIDO A QUE ES LA LLAVE PRIMARIA EN LA TABLA AUNQUE PIENSO QUE LO IDEAL SERIA BUSCAR LA CONMBINACION ESTUDIANTE-TUTOR

	if request.method == 'DELETE':

		try:
			
			asignaciones_db = session.query(asignaciones).filter_by(fecha = fecha).delete()
			session.commit()
		
		except Exception, e:
			session.rollback()
			return "Operacion No se pudo llevar a cabo", 500
		return "ok"

	else:
		return "Operacion No se pudo llevar a cabo", 500


@app.route("/propuesta/<int:id_propuestamatricula>",methods=['POST'])
def create_propuestas_matricula(id_propuestamatricula):
	"""
	@retorna un ok en caso de que se halla ejecutado la operacion 
	@except status 500 en caso de presentar algun error

	"""
	if request.method == 'POST':
		try:
			
			aprovado = request.form.get('pm_aprovado')
			
			propuesta = propuestas_matricula(id = id_propuestamatricula , estudiante = id_estudiante , tutor = id_tutor, estado = aprovado)
			session.add(propuesta)
			session.commit()

		except Exception, e:
			session.rollback()
			return "Operacion No se pudo llevar a cabo", 500
		return "ok"
	else:
		return "Operacion No se pudo llevar a cabo", 500

@app.route("/propuesta/<int:id_propuestamatricula>",methods=['PUT'])
def update_propuestas_matricula(id_propuestamatricula):
	"""
	@retorna un ok en caso de que se halla ejecutado la operacion 
	@except status 500 en caso de presentar algun error

	"""
	
	if request.method == 'PUT':
		try:
			values = json.loads( request.data )
			aprobado = values['pm_aprobado']
			estado = '1' if aprobado == True else '0'
			
			propuestas =  session.query(propuestas_matricula.estado).filter_by(id = id_propuestamatricula).update({propuestas_matricula.estado: estado})
			session.commit()

		except Exception, e:
			session.rollback()
			return "Operacion No se pudo llevar a cabo", 500
		return "{status: 'ok'}"
	else:
		return "Operacion No se pudo llevar a cabo", 500

# @app.route("/tutor/<int:id_tutor>/estudiantes/<id_estudiante>/remisiones",methods=['GET'])
# def read_remisiones(id_tutor, id_estudiante):

# 	remisiones_desc =  session.query(remisiones.id, remisiones.estudiante, remisiones.servicios_bienestar_id, remisiones.motivo, remisiones.fecha).filter_by(estudiante = id_estudiante)

# 	response = []

# 	for remision in remisiones_desc:
# 		response.append({'id': remision.id, 'estudiante': remision.estudiante, 'servicio': remision.servicios_bienestar_id, 'motivo': remision.motivo, 'fecha': remision.fecha.__str__})

# 	return json.dumps(response)










