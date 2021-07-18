from flask import Flask, redirect, url_for, render_template, request, session
import requests
import json
from datetime import timedelta
#from flask_sqlalchemy import SQLAlchemy
from signalrcore.hub_connection_builder import HubConnectionBuilder
import os
import gevent
from flask_sqlalchemy import SQLAlchemy

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

@app.route("/")
def home():
  url_for('static', filename='style.css')
  return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
    app_server = gevent.wsgi.WSGIServer(('0.0.0.0', 8080), app)
    app_server.serve_forever()