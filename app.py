# -*- coding: utf-8 -*-
"""
@authors: Tyler B, Joe H, Shrey S
"""

import os
from os.path import exists
from string import punctuation
from logging import FileHandler, WARNING
from flask import Flask, flash, render_template, abort, session, request, redirect, url_for
#from wsgiref.simple_server import make_server

app = Flask(__name__)
app.debug = True
# Error reporting for prod server, remove the commented out # when deploying
# F_H = FileHandler('errorlogs.txt')
# F_H.setLevel(WARNING)
# app.logger.addHandler(F_H)

# Production server for web app, remove the commented out # when deploying
# def web_app(environment,response):
#    status='200 OK'
#    headers=[('content-type','text/html; charset=utf-8')]
#    response(status,headers)
#    return [b'<h2>This is WSGI server</h2>']

# with make_server('',5000,web_app) as server:
#    print('serving on port 5000...\nvisit http://127.0.0.1:5000\nTo exit press ctrl + c')
#    server.serve_forever()

# the following routes are all available routes or pages to be loaded as part of the webpage
# multiple pages are part of this website

# Error reporting for the prod server, will print out errors to 'errorlogs.txt'
# @app.route('/')
# def error_los():
#    return 1/0


@app.route('/', methods=["POST", "GET"])
def index():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template("home_page.html")


@app.route('/home_page', methods=["POST", "GET"])
def home_page():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template('home_page.html')


@app.route('/sign_up', methods=["POST", "GET"])
def sign_up():
    """This function will be used for designing the login html webpage,
    so the user can have access to the entirety of the website.

    Returns:
        _type_: _description_
    """
    return render_template("sign_up.html")

# creates login form, so the user can have the ability to login


@app.route('/login_form', methods=["POST", "GET"])
def login_form():
    """This function will be used for designing the login html webpage,
    so the user can have access to the entirety of the website.

    Returns:
        _type_: _description_
    """
    return render_template("login_form.html")


@app.route("/logout_page", methods=["POST", "GET"])
def logout_page():
    """Serves as the logout webpage

    Returns:
        _type_: _description_
    """
    return render_template('logout_page.html')


@app.route("/update_password", methods=["POST", "GET"])
def update_password():
    """Serves as the update password page.

    Returns:
        _type_: _description_
    """
    return render_template('update_password.html')

# Creates registration form for a new user to register account


@app.route("/register_for_camp", methods=["POST", "GET"])
def register_for_camp():
    """Serving the Registration.html webpage for user to sign up in case
    if they are not logged in or do not have access

    Returns:
        _type_: _description_
    """
    return render_template('checkout_form.html')


@app.route('/events', methods=["POST", "GET"])
def events():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template('events.html')


@app.route('/staff_login', methods=["POST", "GET"])
def staff_login():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template('staff_login.html')


@app.route('/staff_dashboard', methods=["POST", "GET"])
def staff_dashboard1():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template('staff_dashboard.html')


@app.route('/event_schedule', methods=["POST", "GET"])
def event_schedule():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template('event_schedule.html')


@app.route('/about_us', methods=["POST", "GET"])
def about_us():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template('about_us.html')


@app.route('/legal_notice', methods=["POST", "GET"])
def legal_notice():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template('legal_notice.html')


@app.route('/privacy_statement', methods=["POST", "GET"])
def privacy_statement():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template('privacy_statement.html')


# Starts the executing of program once program enters main.
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
