#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'create_db':
        from src import db
        from src.api.todo import TodoModel

        db.create_all()
        db.session.add(TodoModel('maurice zwo drei', 'bla bla bla'))
        db.session.add(TodoModel('lustige tierchen', 'lol lol'))
        db.session.commit()
    else:
        from src import app

        if os.environ.get('DEBUG') == 1:
            app.run(debug=True)
        else:
            app.run(debug=False, host='0.0.0.0')
