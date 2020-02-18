import os
import env
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'hike_routes'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', "Env Not loaded")
mongo = PyMongo(app)

# Function to load HOME page:

@app.route("/")
@app.route("/get_hike_names")
def get_hike_names():
    return render_template("home.html", hikes=mongo.db.hike_names.find())

# Function to load ABOUT page:


@app.route("/about")
def about():
    return render_template("about.html")