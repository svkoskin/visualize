#!/usr/bin/env python
import json

from flask import Flask, escape, request, render_template

import numpy

from graphs import scatter


class NumpyEncoder(json.JSONEncoder):
    """ Special json encoder for numpy types. Copied from the mpld3/mpld3 repository """

    def default(self, obj):
        try:
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return [self.default(item) for item in iterable]
        if isinstance(obj, (numpy.int_, numpy.intc, numpy.intp, numpy.int8,
            numpy.int16, numpy.int32, numpy.int64, numpy.uint8,
            numpy.uint16,numpy.uint32, numpy.uint64)):
            return int(obj)
        elif isinstance(obj, (numpy.float_, numpy.float16, numpy.float32,
            numpy.float64)):
            return float(obj)
        elif isinstance(obj, (numpy.ndarray,)):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


app = Flask(__name__)

@app.route('/')
def render():
    default_n = 100

    n = None
    errors = []

    n_str = request.args.get('n')
    if n_str:
        try:
            n = int(n_str)
        except ValueError:
            errors.append('n must be a number. Using the default instead.')

    if n is None:
        n = default_n

    graph = scatter.build(n)
    graph_json = json.dumps(graph, cls=NumpyEncoder)
    return render_template('index.html', graph_json=graph_json, n=n, errors=errors)

app.run()
