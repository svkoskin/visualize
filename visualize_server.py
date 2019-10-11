#!/usr/bin/env python

from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def render():
    return 'ok'

app.run()
