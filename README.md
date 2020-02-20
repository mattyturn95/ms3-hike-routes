This is the 3rd Milestone Project for Code Institute

# Hike Routes

This Project is designed for users to add, edit and upload there favourite hiking trails so that other users can gain an insight on existing hiking trails

## UX

I have designed this site to be used by people interested in obtaining a valuable insight on existing hiking trails. I have kept in mind that the mobile first approach is vital to ensure user friendliness and to create a great user experience. The users of this site should find it easy to use and easy to maneuver from page to page without getting lost along the way. Being able to add, review and read reviews on hiking trails is the main purpose of this project.

### Wireframes: 
* My WireFrame can be found in my Wireframes folder above. I made use of Balsamiq inorder to create a wireframe.

### User Stories:
As a user of this site i want to be able to do the following:
* access the site and not feel overwhelmed by too much information.
* read upon hiking trails that other users have managed to provide information on.
* access information about whether the hike is suitable for various audiences

## Features

### Layout
Thi site contains multiple html pages which display relevant information to that of the link names.

### Font
I have made use of one particular font so that it creates a sense of minimalism and not to make the pages too busy in terms of reading information that has been portrayed. (font name) - font-family: 'Tomorrow', sans-serif;


### Existing Features
* Navigation Bar - This is on the top of all the pages on the site. The left hand side has the title of the page being "Hike Routes", and when clicked on, will return you to the home page. The rest of the navigation items are aligned on the right hand side of the Nav bar.   They are: "Who we are", "Post A Hike", "Add your own review" and "Hike Reviews". 


* Post a hike - The user is redirected to a seperate page, where you can insert information on your own hike where you can make it visible for future users to see.

* Hike Reviews - This will take you to a form where you can submit your own review on existing hikes that have been entered into the database

## Main Technologies Used

* This project uses Python, HTML, CSS and Javascript programming languages. 

### Tools used

* Visual Studio Code  
* PIP for installation of tools needed in this project.
* Github to update commits into repositiry
* Git to handle version control.
* MongoDb
* Mongodb Atlas

### Other technologies / libraries used:
* PyMongo 
* Bootstrap 4.3.1 
* Fontawesome 
* Google Fonts 
* Materialize

## Testing

### User Testing

#### Below are the list of Internet Browsers that were used to test the display of the website:

1. Google Chrome    
2. Mozilla Firefox
3. Microsoft Edge
4. Internet Explorer

## Deployment

### Local Deployment

This project was developed using the Visual Studio Code IDE.

My Repository is here: https://github.com/mattyturn95/ms3-hike-routes
The Site is live here: https://hike-routes-ms3-code-institute.herokuapp.com/

To deploy this project on your own IDE, folow the steps below:

 Firstly, ensure of the following:
    - You have an IDE, such as VS Code
    - The following must be installed locally on your computer:
            - git
            - PIP
            - Python 3
            - Flask
            - A MongoDB Atlas account
1.  Make your own folder and navigate to it on the terminal. Then enter the following in the terminal:

```
https://github.com/mattyturn95/ms3-hike-routes.git
$ pip install --upgrade pip
$ pip install -r requirements.txt
```
2.  To run the app locally:

```
$ python -m flask run
```

### Heroku Deployment

To Deploy using Heroku Git, use git in the command line:

1. log in to your Heroku account and follow the prompts to create a new SSH public key.

```
$ heroku login
```

2.  Clone the repository. Use Git to clone the projects source code to your local machine.

```
$ heroku git:clone -a hike-routes-ms3-code-institute

$ cd hike-routes-ms3-code-institute 
```
3.  create your requirements.txt file

```
$ pip freeze --local > requirements.txt

```
4.  create your procfile file

```
$ echo web: python app.py > Procfile

```

5.  Deploy your changes.

```
$ git add .
$ git commit -am "commit message"
$ git push heroku master
```
6.  In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7.  Set the following config vars:

```
IP : 0.0.0.0
PORT: 5000
MONGO_URI: mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority

8. In the heroku dashboard, click on the button "Open App".

The app should open in a new tab.
```

### Media
- The background image was sourced from https://unsplash.com

### Content

All content was written by myself







