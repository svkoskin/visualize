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
    graph = scatter.build(100)
    graph_json = json.dumps(graph, cls=NumpyEncoder)
    return render_template('index.html', graph_json=graph_json)

app.run()
