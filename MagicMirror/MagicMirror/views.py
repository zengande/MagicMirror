"""
Routes and views for the flask application.
"""

import psutil
import time
from threading import Lock
from flask import Flask
from flask_socketio import SocketIO
from MagicMirror import app,socketio
import Adafruit_DHT

thread = None
thread_lock = Lock()

sensor = Adafruit_DHT.DHT11
pin = 4

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return app.send_static_file('html/index.html')

@socketio.on('connect', namespace="/monitor")
def connect():
    print('connected!')
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=read_ht_thread)

def read_ht_thread():
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        socketio.emit('response_ht',
                      {'humidity': humidity, 'temperature': temperature},
                      namespace='/monitor')
        socketio.sleep(2)