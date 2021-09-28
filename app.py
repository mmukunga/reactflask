import pathlib
from flask import Flask, Response, send_from_directory, jsonify, Blueprint, flash, request, redirect, url_for
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS, cross_origin #comment this on deployment
from api.HelloApiHandler import HelloApiHandler

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

app = Flask(__name__, static_url_path='', static_folder='frontend/build', resources_folder='../resources')
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


@app.route("/flask/get_images/", methods=["GET"])
@cross_origin()
def get_images():
    l = []
    res = cloudinary.api.resources(
    max_results=10, # Antall (maximum er 500, 30 er default)
    prefix='wimf_bunnpris', # Velg folder å hente resources fra
    type='upload') # Velg type: upload er opplastede bilder som alle de er
    l.append(res)

    res1 = cloudinary.api.resources(
    max_results=10, # Antall (maximum er 500, 30 er default)
    prefix='wimf_jacobs', # Velg folder å hente resources fra
    type='upload') # Velg type: upload er opplastede bilder som alle de er
    l.append(res1)
    response = json.dumps(l)
    # response = response.headers.add("Access-Control-Allow-Origin", "*")
    return response



@app.route("/flask/img/<variable_name>/", methods=["GET"]) #<variable_name>/
@cross_origin()
def get_image(variable_name): #variable_name
    l = []
    s = variable_name.replace("+", " ")
    s = str(variable_name).split(',')
    for x in s:
        res = cloudinary.api.resources_by_tag(
            tag=x
        )
        l.append(res)

    if len(l) >= 2:
        l.pop()

    response = json.dumps(l[0])
    return response


@app.route('/flask/oppskriftInfo/<variable_name>/', methods=["GET"])
@cross_origin()
def get_recipe(variable_name):
    s = str(variable_name).replace("+", " ")
    print('1.Hello world - normal! ' + variable_name)
    print('2.Hello world - sys.stderr', file=sys.stderr)
    print(RESOURCES_DIR, file=sys.stderr)   
    print(script_dir)

    path = pathlib.Path(os.path.realpath(__file__))
    path = str(path.parent) + "/resources/Gulasj.txt"
    os.system(path)
    print(path)
    oppskrift = OPPSKRIFT_TEMPLATE.substitute(oppskrift=s)
    print("OPPSKRIFT: " + oppskrift)
    # return oppskrift + ".txt"
    f = open("welcome.txt", "r")
    print(f.read()) 
    f.close()  
    f = open(str("https://reactflask-smb.herokuapp.com"+oppskrift + ".txt"), "rb")
    
    l = []
    for x in f:
        line = str(x).replace("\r", "").replace("\n", "").strip()
        if (line.__eq__("")):
            continue
        elif (line.__eq__(' ')):
            continue
        else:
            l.append(line)
    
    ingrdeiensListe = list()
    for i in range(len(l)):
        if ("Ingredienser:" in str(l[i])):
            for y in range(i+1, len(l)):
                if ("Fremgangs" not in str(l[y])):
                    ingrdeiensListe.append(str(l[y]).replace("•", "").strip())
                elif ("Fremgangs" in str(l[y])):
                    break
    
    fremgangsmaateListe = list()
    for i in range(len(l)):
        if ("Fremgangs" in str(l[i])):
            for y in range(i+1, len(l)):
                if ("Tag:" not in str(l[y])):
                    fremgangsmaateListe.append(str(l[y]).replace("•", "").strip())
                else:
                    break
    
    fremgangsmaateListe.pop()
    tips = ""
    for i in range(len(l)):
        if (str(l[i]).__contains__("Tips")):
            tips = l[i]
            break
    
    undertittel = ""
    for i in range(len(l)):
        if (str(l[i]).__contains__("Undertittel")):
            undertittel = l[i]
            break

    tittel = str(l[0]).replace("Tittel:", "").strip()
                
    # fulldict = dict()
    d = dict()
    d.update({"Undertittel":undertittel.replace("Undertittel:","").strip()})
    d.update({"Ingredienser" : ingrdeiensListe})
    d.update({"Fremgangsmaate" : fremgangsmaateListe})
    d.update({"Tips": tips})
    # d.update({"Alt":l})
    d.update({"Tittel":tittel})

    # fulldict.update({tittel: d})
    
    # l.append(ingrdeiensListe)
    return json.dumps(d)

@app.route('/flask/kategori/<varible_name>/', methods=["GET"])
@cross_origin()
def DynamicUrl(varible_name):
    res = cloudinary.Search()\
        .expression(str(varible_name)+'*')\
        .with_field('context')\
        .with_field('tags')\
        .max_results(100)\
        .execute()
    response = json.dumps(res)
    return response

@app.route('/flask/mmm/', methods=["GET"])
@cross_origin()
def mmm():
    res = cloudinary.api.resources(max_result=100)
    response = json.dumps(res)
    return response
     
