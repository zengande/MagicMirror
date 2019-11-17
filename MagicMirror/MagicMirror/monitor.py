from flask_socketio import Namespace
from threading import Lock
from MagicMirror import socketio
import Adafruit_DHT
import random

thread = None
thread_lock = Lock()
connections = 0

sensor = Adafruit_DHT.DHT11
pin = 4

class Monitor(Namespace):
    """description of class"""
    def on_connect(self):
        global thread, thread_lock, connections
        with thread_lock:
            connections += 1
            if thread is None:
                thread = socketio.start_background_task(target=self._read_ht_thread)

    def on_disconnect(self):
        global thread, thread_lock, connections
        with thread_lock:
            connections -= 1
            if connections == 0:
                thread.join()

    def _read_ht_thread(self):
        global connections
        while connections > 0:
            # (random.randint(0,100), random.randint(-20,50))
            humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
            socketio.emit('response_ht',
                          {'humidity': humidity, 'temperature': temperature},
                          namespace='/monitor')
            socketio.sleep(2)
