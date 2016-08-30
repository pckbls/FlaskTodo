#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import os
import tempfile
import json
import src

class FlaskTodoTestCase(unittest.TestCase):

    db_fd = None
    db_path = None

    @classmethod
    def setUpClass(self):
        self.db_fd, self.db_path = tempfile.mkstemp()
        src.Config.SQLALCHEMY_DATABASE_URI = 'sqlite:////' + self.db_path
        src.init()

    @classmethod
    def tearDownClass(self):
        os.close(self.db_fd)
        os.unlink(self.db_path)

    def setUp(self):
        self.app = src.app.test_client()
        with src.app.app_context():
            src.db.create_all()
            src.db.session.commit()

    def tearDown(self):
        with src.app.app_context():
            src.db.drop_all()

    def getTodos(self):
        res = self.app.get('/api/todo/')
        assert res.status_code == 200
        return json.loads(res.data.decode("utf-8"))

    def getTodo(self, id):
        res = self.app.get('/api/todo/' + str(id))
        assert res.status_code == 200
        return json.loads(res.data.decode("utf-8"))

    def addTodo(self, title, text):
        res = self.app.post('/api/todo/', data=dict(
            title=title,
            text=text
        ))
        assert res.status_code == 200

    def deleteTodo(self, id):
        res = self.app.delete('/api/todo/' + str(id))
        assert res.status_code == 204

    def test_empty_db(self):
        data = self.getTodos()
        assert data == []

    def test_complex(self):
        # add a Todo
        self.addTodo('foo', 'bar')

        # check the added Todo
        data = self.getTodo(1)
        assert data['title'] == 'foo' and data['text'] == 'bar'

        # delete that Todo
        self.deleteTodo(1)

        # check if the database is empty again
        self.test_empty_db()
