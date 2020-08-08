# Getting our dependencies
from flask import (
    Flask,
    render_template,
    request,
    flash,
)  # For creating a Flask app and render html templates
from flask_sqlalchemy import SQLAlchemy  # For our database
from datetime import datetime
import json  # To open JSON files

# # from werkzeug import secure_filename # To upload files
# import pickle # To read pkl files

# with open('config.json', 'r') as f:  # Fetching our Configuration JSON File
#     params = json.load(f)["params"] # Obtaining our parameters from the JSON

# local_server = True # If we are working on local server


app = Flask(__name__)  # Create our app
app.secret_key ="secret"
# if local_server:
#     app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri'] # username:password@localhose/database_name
# else:
#     app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
# db = SQLAlchemy(app)

# class Contacts(db.Model):
#     '''
#     Name,phone number,email,message
#     '''
#     id = db.Column(db.Integer,primary_key = True)
#     name = db.Column(db.String(80), unique=False, nullable=False)
#     phone_no = db.Column(db.String(12), unique=False, nullable=True)
#     email_id = db.Column(db.String(80), unique=False, nullable=False)
#     message = db.Column(db.String(500), unique=False, nullable=False)

db = SQLAlchemy(app)

with open("config.json", "r") as f:  # Fetching our Configuration JSON File
    params = json.load(f)["params"]  # Obtaining our parameters from the JSON

local_server = True  # If we are working on local server

if local_server:
    app.config["SQLALCHEMY_DATABASE_URI"] = params[
        "local_uri"
    ]  # username:password@localhose/database_name
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = params["prod_uri"]
db = SQLAlchemy(app)


@app.route("/", methods=["GET"])  # Default end point
@app.route("/home", methods=["GET"])  # Default end point
def home():
    try:  # Try catch block helps us to debug any server side error
        return render_template("index.html")
    except Exception as e:
        return str(e)


class Contacts(db.Model):

    """contact database attributes..
        name,email,phone_num,msg,date
    """

    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=False, nullable=False)
    email = db.Column(db.String(60), nullable=False)
    phone_num = db.Column(db.String(20), unique=False, nullable=False)
    msg = db.Column(db.String(200), unique=False, nullable=False)
    date = db.Column(db.String(30), unique=False, nullable=True)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        """add entry to database (fetching from the html page)"""
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        msg = request.form.get("message")

        """ now entry to database
        name, email, phone_num, msg, date
        """
        entry = Contacts(
            name=name, email=email, phone_num=phone, msg=msg, date=datetime.now()
        )
        db.session.add(entry)
        db.session.commit()
        """mail.send_message("New Message from blog", sender=email,
                          recipients=params["gmail_user"],
                          body=msg + "\n")"""
        flash("Message Sent Successfully!", "success!")
    return render_template("contact.html", params=params)


# @app.route('/contact', methods=['GET', 'POST'])  # End point for Contact Page
# def contact():
#     try:  # Try catch block helps us to debug any server side error
#         if (request.method == 'POST'):
#             '''
#             Add entry to our database
#             '''
#             ## The parameter passed to request.form.get is the name of the field in the html file rendered
#             name = request.form.get('name')
#             email = request.form.get('email')
#             phone = request.form.get('phone_no')
#             msg = request.form.get('message')
#             entry = Contacts(name = name,email_id = email,phone_no = phone, message = msg )
#             db.session.add(entry) # Start a new session for our database
#             db.session.commit() # Commit our entry

#         # Don't forget to action = "/route", method = "POST" in the html file for the submit button

#         return render_template('contact.html', params = params)
#     except Exception as e:
#         return str(e)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
