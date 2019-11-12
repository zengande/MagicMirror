"""
This script runs the MagicMirror application using a development server.
"""

from os import environ
from MagicMirror import app,socketio

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    DEBUG = environ.get('Environment', 'Production')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    isDebug = DEBUG == "Development"
    socketio.run(app, host=HOST,  port=PORT,debug=isDebug)
