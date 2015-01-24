#!/usr/bin/python

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import MySQLdb

app = Flask(__name__)
app.config['SECRET_KEY'] = 'development key'

engine = create_engine("mysql+mysqldb://parces:p4rc3s@localhost:3306/parces")
Session = sessionmaker(bind=engine)
session = Session()

IES_REST_URL = "http://ryca.itfip.edu.co:8888"

import views
import estudiante_views
import profesor_views
import tutor_views
