#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os
import src

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == 'create_db':
            src.init()
            src.db.create_all()
            src.db.session.commit()
        elif sys.argv[1] == 'tests':
            import unittest
            import tests
            suite = unittest.TestLoader().loadTestsFromTestCase(tests.todo.FlaskTodoTestCase)
            unittest.TextTestRunner(verbosity=2).run(suite)
    else:
        src.init()

        if os.environ.get('DEBUG') == 1:
            src.app.run(debug=True)
        else:
            src.app.run(debug=False, host='0.0.0.0')
