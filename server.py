__author__ = 'Adarsh'

import cherrypy
import MySQLdb.cursors
import json
import os


mysql_credentials = json.load(open('mysql_credentials.json'))
conn = MySQLdb.connect(**mysql_credentials)
cursor = conn.cursor(MySQLdb.cursors.DictCursor)

class App(object):
	exposed = True


	@cherrypy.tools.allow(methods=['POST','GET'])
	@cherrypy.expose
	def execute(self,ins_arr):
		print ins_arr	
    #Function for recieving array through AJAX goes here
	@cherrypy.tools.allow(methods=['GET'])
	@cherrypy.expose
	def serve(self):
		query = 'SELECT * FROM ins'
		cursor.execute(query)
		result = cursor.fetchall()
		return json.dumps(result)
		return file("dashboard.html")


if __name__ == '__main__':
	cherrypy.server.socket_host = "0.0.0.0"
	cherrypy.server.socket_port = 5555
	conf = {'/static': {'tools.staticdir.on': True,'tools.staticdir.dir': os.path.dirname(os.path.abspath(__file__)) + '/static'}}
	cherrypy.quickstart(App(), config=conf)