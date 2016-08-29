# About

Recently I've discovered the Flask web framework. I've created this simple Todo App to get familiar with the following tools and techniques:
* Flask
* Flask-RESTful
* Flask-SQLAlchemy
* Bootstrap
* Backbone.js

# Screenshot

![screenshot](https://github.com/pckbls/FlaskTodo/raw/work/screenshot.png)

# How to run

Either start the app via the `start.sh` script or use Docker:

```bash
docker build -t flasktodo .
docker run --rm -ti -p 5000:5000 --name FlaskTodo flasktodo	
```

In both cases the app will be accessible via `http://localhost:5000`.
