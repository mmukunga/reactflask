import pathlib
from flask import Flask, Response, send_from_directory, jsonify, Blueprint, flash, request, redirect, url_for
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS, cross_origin #comment this on deployment
from api.HelloApiHandler import HelloApiHandler

import webbrowser
import sys,os,time,datetime

from pathlib import Path

from collections import defaultdict

import sys
import logging

from string import Template
import cloudinary
import cloudinary.api

import json

cloudinary.config(
    cloud_name = "wimf",
    api_key = "162995398385258",
    api_secret="3QGyv6kLxceY2sJpLA0HTU78Aco",
    secure=True
)

OPPSKRIFT_TEMPLATE = Template(r"/app/resources/${oppskrift}")

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app) #comment this on deployment
api = Api(app)
api.add_resource(HelloApiHandler, '/flask/hello')


BASE_DIR = Path(__file__).resolve().parent
script_dir = BASE_DIR/'resources'
RESOURCES_DIR = BASE_DIR.joinpath('resources')

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

@app.route("/flask/<string:name>")
def hello_world(name):
    app.logger.info('Hello world - app.logger.info')
    return "<p>Hello, Samuel! " + name + "</p>"

@app.route('/flask/<int:id>', methods=['PUT'])
def update_todo(id):
  print('Hello world - normal! ' + id)
  print('Hello world - sys.stderr', file=sys.stderr)
  return Response('test', status=200, mimetype='text/html')

@app.route('/flask/oppskriftInfo/<string:filename>', methods=["GET"])
@cross_origin()
def get_recipe(filename):
    MY_FILENAME = "Gulasj.txt"
    
    search_path = r'/app/resources'
    selected_files = find_files(MY_FILENAME, search_path)
    print(selected_files)

    file_dict = defaultdict(list)
    meny_innhold = list()

    with open(selected_files[0], 'r', encoding="ISO-8859-1") as f:
        for line in f:
           line = line.rstrip() 
           print(line) 
           if line not in ["Tittel:", "Undertittel:", "Ingredienser:", "Fremgangsmåte:", "Tips:"]:
              print('1.line..'+line.rstrip())  
              meny_innhold.append(line)
           else:
              print('2.line..')   
              file_dict[line].append(meny_innhold)
              meny_innhold = list()
        f.close()
    
    print("\n", dict(file_dict))
    return json.dumps(file_dict)

@app.route('/flask/mmm/', methods=["GET"])
@cross_origin()
def mmm():
    res = cloudinary.api.resources(max_result=100)
    response = json.dumps(res)
    return response
     
def find_files(filename, search_path):
   result = []
   # Wlaking top-down from the root
   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result
