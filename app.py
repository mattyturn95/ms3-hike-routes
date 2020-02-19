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

# ADD_HIKE page:


@app.route("/add_new_hike")
def add_new_hike():
    return render_template("add_hike.html")

# This function POSTs the input data from the user, to the database:


@app.route("/insert_hike", methods=['POST'])
def insert_hike():
    hike = mongo.db.hike_names
    hike.insert_one(request.form.to_dict())
    return redirect(url_for('get_hike_names'))

# Function to load UPDATE_HIKE page:

@app.route("/edit_hike/<hike_id>")
def edit_hike(hike_id):
    the_hike = mongo.db.hike_names.find_one({"_id": ObjectId(hike_id)})
    return render_template("update_hike.html", hike=the_hike)