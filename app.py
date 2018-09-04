#!/usr/bin/env python3

from flask import *
from os import *

#localhost:7000
webpage = Flask(__name__);

@webpage.route('/')
def index():
  return render_template('index.htm');

@webpage.errorhandler(404)
def not_found(error):
  return render_template('404.htm'), 404;

print(" * Bienvenido al servidor
if __name__ == "main":
  webpage.run(port=7000, debug=True, host='0.0.0.0');
