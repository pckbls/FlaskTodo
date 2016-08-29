#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask_restful import fields
from src import db

class TodoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    text = db.Column(db.String(600))
    checked = db.Column(db.Boolean)

    marshal = {
        'id': fields.Integer,
        'title': fields.String,
        'text': fields.String,
        'checked': fields.Boolean
    }

    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.checked = False
