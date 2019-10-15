#!/bin/sh
# it runs the flask server

export FLASK_APP=application.py
export FLASK_ENV=development
flask run
