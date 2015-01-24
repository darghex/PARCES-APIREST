#!/usr/bin/python
"""

"""

from main import app
class Config:
	DEBUG = True
	SECRET_KEY = ''
	HOST =  '0.0.0.0';
	PORT = 8000


if __name__ == '__main__':
	
    app.run(host = Config.HOST,
    	port = Config.PORT,
    	debug = Config.DEBUG
    	)
