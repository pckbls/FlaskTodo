#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask_restful import Resource, reqparse, marshal_with
from src import api, db
from src.models.todo import TodoModel

class Todo(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True, help='the title')
    parser.add_argument('text', type=str, required=True, help='the text')
    parser.add_argument('checked', type=bool, required=False, help='is the task already done?')

    @marshal_with(TodoModel.marshal)
    def get(self, id):
        model = TodoModel.query.filter_by(id=id).first_or_404()
        return model

    @marshal_with(TodoModel.marshal)
    def put(self, id):
        args = Todo.parser.parse_args()

        model = TodoModel.query.filter_by(id=id).first_or_404()
        model.title = args["title"]
        model.text = args["text"]
        if "checked" in args:
            model.checked = args["checked"]

        db.session.commit()

        return model

    @marshal_with(TodoModel.marshal)
    def delete(self, id):
        model = TodoModel.query.filter_by(id=id).first_or_404()
        db.session.delete(model)
        db.session.commit()
        return None, 204

class TodoList(Resource):
    @marshal_with(TodoModel.marshal)
    def get(self):
        return TodoModel.query.all()

    @marshal_with(TodoModel.marshal)
    def post(self):
        args = Todo.parser.parse_args()

        model = TodoModel(args["title"], args["text"])
        if args["checked"] != None:
            model.checked = args["checked"]

        db.session.add(model)
        db.session.commit()

        return model

api.add_resource(TodoList, '/api/todo/')
api.add_resource(Todo, '/api/todo/<string:id>')
