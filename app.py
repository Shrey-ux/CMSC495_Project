# -*- coding: utf-8 -*-
"""
@authors: Tyler B, Joe H, Shrey S
"""


import os
from os.path import exists
from string import punctuation
from logging import FileHandler, WARNING
from flask import Flask, flash, render_template, abort, session, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed
from werkzeug.security import generate_password_hash, check_password_hash
from wsgiref.simple_server import make_server
import pyodbc
import pandas as pd


def connectionClose():
    '''Close the connection to the database'''
    conn.commit()
    conn.close()


def databaseConnect():
    '''Creates a connection to the database
    can be accessed globally'''
    global conn
    # You can replace the server name with outward TCP IP address to deploy globally
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-62CDVC6\SQLEXPRESS01;'
                          'Database=MDFootballCamp;'
                          'UID=tyler;'
                          'PWD=password;')


def insertToUsers():
    insertUser = str(
        " INSERT INTO [dbo].[Users] ([username] ,[password] ,[staffuser])" + "VALUES" + somrStriungVariable)


def insertToRegDB(regValue):

    # valueLS = str(" ('Dhaval', 'Patel', 'dpatel', 'dpatel@gmail.com', '2676165627', '2010-01-01', '5111 Westland', '', 'Arbutus', 'Maryland', '21226', 'qb_event', 'Tyler', 'Smith', '1234567890', 'Friend','No', 'password') ")

    insert_db = str(" INSERT INTO [dbo].[MDFOOTBALLCAMP] " +
                    " ([firstname] ,[lastname] ,[username] ,[email] ,[phone_number] ,[birthdate] ,[address] ,[address2] " +
                    " ,[city] ,[state] ,[zip] ,[event] ,[ec_firstname] ,[ec_lastname] ,[ec_phone_number] ,[relationship_to_athlete] " +
                    " ) VALUES " + regValue)

    databaseConnect()
    conn.execute(insert_db)
    connectionClose()


app = Flask(__name__)
app.debug = True


@app.route('/handle_registration_data', methods=['POST'])
def handle_registration_data():
    # projectpath = request.form['firstName']

    regValue = str("('" + request.form['firstName'] + "', " +
                   "'" + request.form['lastName'] + "', " +
                   "'" + request.form['username'] + "', " +
                   "'" + request.form['email'] + "', " +
                   "'" + request.form['phone_number'] + "', " +
                   "'" + request.form['birthdate'] + "', " +
                   "'" + request.form['address'] + "', " +
                   "'" + request.form['address2'] + "', " +
                   "'" + request.form['city'] + "', " +
                   "'" + request.form['state'] + "', " +
                   "'" + request.form['zip'] + "', " +
                   "'" + request.form['event'] + "', " +
                   "'" + request.form['ec_firstname'] + "', " +
                   "'" + request.form['ec_lastname'] + "', " +
                   "'" + request.form['ec_phone_number'] + "', " +
                   "'" + request.form['relationship_to_athlete'] + "') "
                   # "'" + request.form['password'] + "') "
                   )

    insertToRegDB(regValue)

    return render_template('home_page.html')


@app.route('/handle_signup_data', methods=['POST'])
def handle_registration_data():
    # projectpath = request.form['firstName']

    # valueLS = str(" ('Dhaval', 'Patel', 'dpatel', 'dpatel@gmail.com', '2676165627', '2010-01-01', '5111 Westland', '', 'Arbutus', 'Maryland', '21226', 'qb_event', 'Tyler', 'Smith', '1234567890', 'Friend') ")

    value = str("('" + request.form['firstName'] + "', " +
                "'" + request.form['lastName'] + "', " +
                "'" + request.form['username'] + "', " +
                "'" + request.form['email'] + "', " +
                "'" + request.form['phone_number'] + "', " +
                "'" + request.form['birthdate'] + "', " +
                "'" + request.form['address'] + "', " +
                "'" + request.form['address2'] + "', " +
                "'" + request.form['city'] + "', " +
                "'" + request.form['state'] + "', " +
                "'" + request.form['zip'] + "', " +
                "'" + request.form['event'] + "', " +
                "'" + request.form['ec_firstname'] + "', " +
                "'" + request.form['ec_lastname'] + "', " +
                "'" + request.form['ec_phone_number'] + "', " +
                "'" + request.form['relationship_to_athlete'] + "') "
                # "'" + request.form['password'] + "') "
                )

    insertToDB(value)

    return render_template('home_page.html')


@app.route('/', methods=["POST", "GET"])
def index():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template('home_page.html')


@app.route('/home_page', methods=["POST", "GET"])
def home_page():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template('home_page.html')

# Creates sign-up form for a new user to register account


@app.route('/sign_up', methods=["POST", "GET"])
def sign_up():
    """This function will be used for designing the login html webpage,
    so the user can have access to the entirety of the website.

    Returns:
        _type_: _description_
    """
    return render_template('sign_up.html')

# creates login form, so the user can have the ability to login


@app.route('/login', methods=["POST", "GET"])
def login():
    """This function will be used for designing the login html webpage,
    so the user can have access to the entirety of the website.

    Returns:
        _type_: _description_
    """
    return render_template("login_form.html")


@app.route("/logout", methods=["POST", "GET"])
def logout():
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


@app.route("/register_for_camp", methods=["GET", "POST"])
def register_for_camp():
    """Serving the Registration.html webpage for user to sign up in case
    if they are not logged in or do not have access

    Returns:
        _type_: _description_
    """
    return render_template('register_for_camp.html')


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
def staff_dashboard():
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
