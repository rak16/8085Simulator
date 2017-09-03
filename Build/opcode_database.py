import csv
import MySQLdb

db = MySQLdb.connect("localhost","root","","simulator" )
cursor = db.cursor()
csv_data = csv.reader(file('op_codes.csv'))
for row in csv_data:
    cursor.execute('INSERT INTO ins(instructions, op_codes) VALUES ("%s", "%s")', row)
db.commit()
cursor.close()
print "Done"
