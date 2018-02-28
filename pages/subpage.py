# coding: utf-8

from flask import Blueprint, render_template

app = Blueprint('subpage', __name__)


@app.route('/subpage')
def index():
    return render_template('index.html', title='sub-page')
