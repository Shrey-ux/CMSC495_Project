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

#the following routes are all available routes or pages to be loaded as part of the webpage
#mulltiple pages are part of this website
@app.route('/', methods=["POST", "GET"]) #
def index():
    """ This function is designed as the root page for the WebApplication"""
    return render_template("home_page.html")

@app.route('/home_page', methods=["POST", "GET"])
def home_page():
    """ DESCRIPTION HERE """
    return render_template('home_page.html')

@app.route('/sign_up', methods=["POST", "GET"])
def sign_up():
    """ This function will be used for designing the login html webpage,
    so the user can have access to the entirety of the website. """
    return render_template("sign_up.html")

#creates login form, so the user can have the ability to login
@app.route('/login_form', methods=["POST", "GET"])
def login_form():
    """ This function will be used for designing the login html webpage,
    so the user can have access to the entirety of the website. """
    return render_template("login_form.html")

@app.route("/logout_page", methods=["POST", "GET"])
def logout():
    """ Serves as the logout webpage """
    return render_template('logout.html')

#Creates registration form for a new user to register account
@app.route("/register_for_camp", methods=["POST", "GET"])
def register_for_camp():
    """ Serving the Registration.html webpage for user to sign up in case
    if they are not logged in or do not have access """
    return render_template('checkout_form.html')

@app.route('/events', methods=["POST", "GET"])
def events():
    """ DESCRIPTION HERE """
    return render_template('events.html')

@app.route('/Page1', methods=["POST", "GET"])
def page1():
    """ DESCRIPTION HERE """
    return render_template('Training.html')

@app.route('/event_schedule', methods=["POST", "GET"])
def event_schedule():
    """ DESCRIPTION HERE """
    return render_template('event_schedule.html')

@app.route('/about_us', methods=["POST", "GET"])
def about_us():
    """ DESCRIPTION HERE """
    return render_template('about_us.html')

@app.route('/legal_notice', methods=["POST", "GET"])
def legal_notice():
    """ DESCRIPTION HERE """
    return render_template('legal_notice.html')

@app.route('/privacy_statement', methods=["POST", "GET"])
def privacy_statement():
    """ DESCRIPTION HERE """
    return render_template('privacy_statement.html')

#Starts the executing of program once program enters main.
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
