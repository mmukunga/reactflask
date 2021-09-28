import pathlib
from flask import Flask, Response, send_from_directory, jsonify, Blueprint, flash, request, redirect, url_for
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS, cross_origin #comment this on deployment
from api.HelloApiHandler import HelloApiHandler

import webbrowser
import sys,os,time,datetime

from pathlib import Path

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

OPPSKRIFT_TEMPLATE = Template(r"/resources/${oppskrift}")

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

@app.route('/flask/oppskriftInfo/<variable_name>/', methods=["GET"])
@cross_origin()
def get_recipe(variable_name):
    s = str(variable_name).replace("+", " ")
    print('1.Hello world - normal! ' + variable_name)
    print('2.Hello world - sys.stderr', file=sys.stderr)
    print(RESOURCES_DIR, file=sys.stderr)   
    print(script_dir)

    path = pathlib.Path(os.path.realpath(__file__))
    lst = os.listdir(str(path.parent) + "/resources")
    path = str(path.parent) + "/resources/Gulasj2.txt"  
    print(path)
    f = open(path, 'r', encoding="ISO-8859-1")
    print(f.read()) 
    f.close()

    print(lst[10]) 
    print(webbrowser.open(lst[10]))
    # fulldict.update({tittel: d})
    # l.append(ingrdeiensListe)
    # fulldict = dict()
    d = dict()
    d.update({"Undertittel": "Gulasj.txt"})
    d.update({"Ingredienser" : ["Ingrediens"]})
    d.update({"Fremgangsmaate" : ["Fremgangsmaate"]})
    d.update({"Tips": "tips"})
    # d.update({"Alt":l})
    d.update({"Tittel": "tittel"})
    return json.dumps(d)

@app.route('/flask/mmm/', methods=["GET"])
@cross_origin()
def mmm():
    res = cloudinary.api.resources(max_result=100)
    response = json.dumps(res)
    return response
     
