#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = None
db = None
api = None

class Config(object):
    ERROR_404_HELP = False
    BUNDLE_ERRORS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../sqlite.db'

def init(config_object = None):
    global app, db, api

    app = Flask(__name__, static_folder='../static')
    app.config.from_object(config_object if config_object else Config)

    db = SQLAlchemy(app)

    api = Api(app)
    import src.api
