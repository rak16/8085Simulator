__author__ = 'Adarsh'

import cherrypy
import MySQLdb
import json
import os

mysql_credentials = json.load(open('mysql_credentials.json'))

# For thread safety with MySQLdb (http://tools.cherrypy.org/wiki/Databases)
def connect_mysql(thread_index = None):
    # Create a connection and store it in the current thread 
    cherrypy.thread_data.db = MySQLdb.connect(**mysql_credentials)
    cherrypy.thread_data.db.autocommit(True)

#Call "connect" for each thread, when it starts
cherrypy.engine.subscribe('start_thread', connect_mysql)

class App(object):
	exposed = True

	# @cherrypy.tools.allow(methods=['POST','GET'])
	# @cherrypy.expose
    #Function for recieving array through AJAX goes here

	@cherrypy.tools.allow(methods=['GET'])
	@cherrypy.expose
	def serve(self):
		return file("dashboard.html")


if __name__ == '__main__':
	cherrypy.server.socket_host = "0.0.0.0"
	cherrypy.server.socket_port = 5555
	conf = {'/static': {'tools.staticdir.on': True,'tools.staticdir.dir': os.path.dirname(os.path.abspath(__file__)) + '/static'}}
	cherrypy.quickstart(App(), config=conf)