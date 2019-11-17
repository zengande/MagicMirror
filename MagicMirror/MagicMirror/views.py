"""
Routes and views for the flask application.
"""
import time
from flask import Flask
from MagicMirror import app,socketio
from MagicMirror.monitor import Monitor
from MagicMirror.weather import Weather

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return app.send_static_file('html/index.html')

@app.route('/weather',methods=['get'])
def weather():
    return Weather.getWeather("7f1494e17bcf4e8f92520f9f23c04b6b")

socketio.on_namespace(Monitor("/monitor"))