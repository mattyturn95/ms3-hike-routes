import os
import env
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'hike_routes'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', "Env Not loaded"
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

# UPDATE_HIKE function - This updates a HIKES info on the db:

@app.route("/update_hike/<hike_id>", methods=["POST"])
def update_hike(hike_id):
    river = mongo.db.hike_names
    river.update({'_id': ObjectId(hike_id)}, {
        'hike_name' : request.form.get('hike_name'),
        'status' : request.form.get('status'),
        'birds' : request.form.get('birds'),
        'easy_or_hard' : request.form.get('easy_or_hard'),
        'mountain_gear_required' : request.form.get('mountain_gear_required')
    })
    return redirect(url_for('get_hike_names'))

# delete hike record function:

@app.route("/delete_hike/<hike_id>")
def delete_hike(hike_id):
    mongo.db.hike_names.remove({'_id': ObjectId(hike_id)})
    return redirect(url_for('get_hike_names'))
    

# Function to load Review a Hike page:

@app.route("/leave_review")
def leave_review():
    return render_template("leave_review.html", hikes=mongo.db.hike_names.find())

# Function to insert User review to DB:

@app.route("/insert_review", methods=['POST'])
def insert_review():
    review = mongo.db.hike_reviews
    review.insert_one(request.form.to_dict())
    return redirect(url_for('read_review'))

# Function to load READ REVIEWS page:

@app.route("/read_review")
def read_review():
    return render_template("read_review.html", reviews=mongo.db.hike_reviews.find())


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=False)
