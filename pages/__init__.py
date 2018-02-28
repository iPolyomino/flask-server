# coding: utf-8

from flask import Flask
import index
import subpage

application = Flask(__name__)

modules_define = [index.app, subpage.app]
for app in modules_define:
    application.register_blueprint(app)
