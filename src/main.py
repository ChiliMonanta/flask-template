#!/usr/bin/env python3

import os
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask import send_from_directory

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

_log = None
LOG_LEVEL = logging.INFO

def get_logger():
    global _log
    if _log is None:
        logger = logging.getLogger('app1')
        logger.setLevel(LOG_LEVEL)
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', '%m-%d %H:%M:%S')
        fh = RotatingFileHandler('app1.log', maxBytes=10000, backupCount=1)
        fh.setLevel(LOG_LEVEL)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        logging.addLevelName(logging.DEBUG, 'D')
        logging.addLevelName(logging.INFO, 'I')
        logging.addLevelName(logging.ERROR, 'E')
        _log = logger

    return _log

app = Flask(__name__, static_url_path=os.path.join(ROOT_PATH, 'static'))
get_logger()

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

@app.route('/')
@app.route('/index')
def index():
    _log.info('main')
    return send_from_directory('templates', 'index.html')

@app.route('/template/<name>')
def template(name=None):
    return render_template('template.html', name=name)

@app.route('/command', methods=['GET'])
def command():
    return ('', 204)

@app.route('/status', methods=['GET'])
def status():
    arg = request.args.get("arg1")
    return jsonify({"result":arg})

@app.before_first_request
def initialize():
    _log.info('Initialized')

@app.teardown_appcontext
def close(error):
    _log.debug('Teardown %s' % str(error))

if __name__ == '__main__':
    app.run()
    #app.run(host='0.0.0.0')
