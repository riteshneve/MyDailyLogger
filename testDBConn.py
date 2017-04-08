from flask import Flask, redirect, url_for, request, render_template, json
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'myDailyLogger'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
#conn = mysql.get_db()
cursor = conn.cursor()
#cursor = mysql.get_db().cursor()
#cursor.callproc('sp_createUser',('qwe','qwe','qwe'))
	
#data = cursor.fetchall()

query = "INSERT INTO info (dates, kms, summary) VALUES (20170402, 4, 'TEST')"

cursor.execute(query)
conn.commit()