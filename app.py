from flask import Flask, Response, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from api.HelloApiHandler import HelloApiHandler

import sys
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app) #comment this on deployment
api = Api(app)
api.add_resource(HelloApiHandler, '/flask/hello')

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

@app.route("/about")
def about():
    return 'The About Page!'

@app.route("/blog")
def blog():
    return 'This is the blog'    

@app.route("/blog/<blog_id>")
def blogPost(blog_id):
    return 'This is blog number ' + str(blog_id)

@app.route("/flask/<string:name>")
def hello_world(name):
    app.logger.info('Hello world - app.logger.info')
    return "<p>Hello, Samuel! " + name + "</p>"

@app.route('/flask/<int:id>', methods=['PUT'])
def update_todo(id):
  print('Hello world - normal! ' + id)
  print('Hello world - sys.stderr', file=sys.stderr)
  return Response('test', status=200, mimetype='text/html')
     
