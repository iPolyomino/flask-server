# coding: utf-8

import os
from flask import Flask, send_from_directory
import index
import subpage

application = Flask(__name__)


@application.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


modules_define = [index.app, subpage.app]
for app in modules_define:
    application.register_blueprint(app)
