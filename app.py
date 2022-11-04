# -*- coding: utf-8 -*-
"""
@authors: Tyler Bokey, Joe Hibbler, Shrey Shah
"""

import os
from os.path import exists
from string import punctuation
from flask import Flask, flash, render_template, abort, session, request, redirect, url_for

app = Flask(__name__)
app.debug = True

def if_user_registered(current_session_username):
    """ This function checks to make sure the certain user already registered
    in the overall new_pass_file """
    #checks to see if user is already registered by using salt hashing strategy   

#the following routes are all available routes or pages to be loaded as part of the webpage
#mulltiple pages are part of this website
@app.route('/')
def home_page():
    """ This function is designed as the root page for all
    webpages and will post the current date and time on the
    webpage """
    if "username" in session:
        return render_template("index.html")
    return redirect(url_for("login"))

#creates login form, so the user can have the ability to login
@app.route('/login_form', methods=["POST", "GET"])
def login():
    """ This function will be used for designing the login html webpage,
    so the user can have access to the entirety of the website. """
    if request.method == "POST":

@app.route("/logout")
def logout():
    """ Serves the logout webpage """
    if "username" in session:
        session.pop("username", None)
        flash("You have successfully logged out.")
    return redirect(url_for('login'))

#Creates registration form for a new user to register account
@app.route("/registration", methods=["POST", "GET"])
def registration():
    """ Serving the Registration.html webpage for user to sign up in case
    if they are not logged in or do not have access """
    if request.method == "POST":

#This route resembles the Password update form, and the accompanied content
#follows for the Password update form information.
@app.route('/Update_Pass', methods=["POST", "GET"])
def update_password():

@app.route('/Page1')
def page1():
    """ DESCRIPTION HERE """
    if "username" in session:
        return render_template('Training.html')
    return abort(401)

@app.route('/Page2')
def page2():
    """ DESCRIPTION HERE """
    if "username" in session:
        return render_template('Certifications.html')
    return abort(401)

@app.route('/Page3')
def page3():
    """ DESCRIPTION HERE """
    if "username" in session:
        return render_template("Table.html")
    return abort(401)

#Starts the executing of program once program enters main.
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
