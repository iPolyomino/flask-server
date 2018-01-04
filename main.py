# coding: utf-8

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='INDEX PAGE')


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
