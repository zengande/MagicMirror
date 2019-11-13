"""
Routes and views for the flask application.
"""
import time
from flask import Flask
from MagicMirror import app,socketio
from MagicMirror.monitor import Monitor

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return app.send_static_file('html/index.html')

socketio.on_namespace(Monitor("/monitor"))