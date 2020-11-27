from flask import Flask, g, render_template
import sqlite3

PATH = 'db/jobs.sqlite'
app = Flask(__name__)

def open_connection():
  connection = getattr(g, '_connection', none)
  if connection = None:
    connection = g._connection = sqlite3.connect(PATH)
    
  connection.row_factory = sqlite3.Row
  return connection



@app.route('/')
@app.route('/jobs')
def jobs():
  return render_template('index.html') 
