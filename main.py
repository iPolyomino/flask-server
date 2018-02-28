# coding: utf-8

from pages import application

app = application


if __name__ == '__main__':
    application.run(host='localhost', port=8080, debug=True)
