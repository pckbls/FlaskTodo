#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

# flask
app = Flask(__name__, static_folder='../static')
app.config['ERROR_404_HELP'] = False
app.config['BUNDLE_ERRORS'] = True

# flask-sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../sqlite.db'
db = SQLAlchemy(app)

# flask-restful
api = Api(app)

import src.api
