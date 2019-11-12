"""
This script runs the MagicMirror application using a development server.
"""

from os import environ
from MagicMirror import app,socketio

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    socketio.run(app, host=HOST,  port=PORT,debug=True)
