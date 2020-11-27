from flask import Flask, g, render_template
import sqlite3

PATH = 'db/jobs.sqlite'
app = Flask(__name__)



@app.route('/')
@app.route('/jobs')
def jobs():
  return render_template('index.html') 
