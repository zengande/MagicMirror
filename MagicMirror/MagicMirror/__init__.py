"""
The flask application package.
"""

from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__, static_url_path="")
socketio = SocketIO(app)

import MagicMirror.views
