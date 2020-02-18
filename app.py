import os
import env
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'kerry_rivers'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', "Env Not loaded")
mongo = PyMongo(app)