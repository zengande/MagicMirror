"""
Routes and views for the flask application.
"""

import psutil
import time
from threading import Lock
from flask import Flask
from flask_socketio import SocketIO
from MagicMirror import app,socketio

thread = None
thread_lock = Lock()

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return app.send_static_file('html/index.html')

@socketio.on('connect', namespace="/wechat")
def connect():
    print('connected!')
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)

# 后台线程 产生数据，即刻推送至前端
def background_thread():
    count = 0
    while True:
        socketio.sleep(5)
        count += 1
        t = time.strftime('%M:%S', time.localtime())
        # 获取系统时间（只取分:秒）
        cpus = psutil.cpu_percent(interval=None, percpu=True)
        # 获取系统cpu使用率 non-blocking
        socketio.emit('response',
                      {'data': [t, cpus], 'count': count},
                      namespace='/wechat')
