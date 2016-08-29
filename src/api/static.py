#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# TODO: DO NOT USE FOR PRODUCTION
# Static files should be served by a web server such as nginx

from src import app

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)
