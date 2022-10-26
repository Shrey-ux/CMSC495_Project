# -*- coding: utf-8 -*-
"""
@author: Tyler Bokey, Joe Hibbler
"""

import os
from os.path import exists
from datetime import datetime
from string import punctuation
from flask import Flask, flash, render_template, abort, session, request, redirect, url_for
from passlib.hash import sha256_crypt

NEW_PASS_FILE = "newpassfile.txt"
COMMON_PASSWORD = "CommonPassword.txt"

#This is a temporary file to store passwords entered
#Only hashed versions of the passwords are stored here
#not the original passwords itself
TEMP_PASS_FILE = "temppassfile.txt"

#This is the direct location of where to locate
#failed logins by user attempts.
FAILED_LOGIN_ATTEMPTS = "failedlogfile.txt"

app = Flask(__name__)
app.debug = True
#using any secret key for hashing to make sure registration or login information
#is not identical
app.secret_key = 'authenticatedsecretkey'

#Open a new file and writes usernames and encrypted passwords to it
if not exists(NEW_PASS_FILE):
    with open(NEW_PASS_FILE, "w", encoding="utf-8") as file:
        file.close()

#Adding the user entered password to the commonly used password list
#Commonpassword.txt so the same password is not used again
common_passwords = set()
with open(COMMON_PASSWORD, "r", encoding="utf-8") as common_passwords_file:
    for entered_password_session in common_passwords:
        common_passwords.add(entered_password_session.strip())

def if_user_registered(current_session_username):
    """ This function checks to make sure the certain user already registered
    in the overall new_pass_file """
    #checks to see if user is already registered by using salt hashing strategy
    with open(NEW_PASS_FILE, "r", encoding="utf-8") as newpassfile:
        for name_already_registered in newpassfile:
            r_username, r_salt_hash = name_already_registered.split()
            r_salt_hash = r_salt_hash + "blank"
            if current_session_username == r_username:
                return True
    return False

def check_for_whitespace(user_string):
    """ This function checks if a string contains spaces or not."""
    entered_string = user_string.split()
    return len(entered_string) > 1

def check_password_complexity(user_password):
    """ This function is designed to check the password complexity requirements
    of a password entered by a user.
    The complexity requirements are as follows:
        -Password must be at least 12 characters in length
        -Password must include at least 1 uppercase character
        -Password must include at least 1 lowercase character
        -Password must include at least 1 number
        -Password must include at least 1 special character.
    """
    #Checking the user met password complexity requirements
    if len(user_password) >= 12:
        if any(the_character.islower() for the_character in user_password):
            if any(the_character.isupper() for the_character in user_password):
                if any(the_character.isdigit() for the_character in user_password):
                    if any(the_character in punctuation for the_character in user_password):
                        return True
    #return False if password does not meet all of the required password complexities
    return False

def right_user_match(curr_username, curr_password):
    """ This function checks to see if the username and password
    of associated user is valid. Returns True if it is valid, False
    if not. """
    with open(NEW_PASS_FILE, "r", encoding="utf-8") as newpassfile:
        for stored_pass_information in newpassfile:
            try:
                username_valid = False
                password_valid = False
                r_username, r_salt_hash = stored_pass_information.split()
                if curr_username == r_username:
                    username_valid = True
                if sha256_crypt.verify(curr_password, r_salt_hash):
                    password_valid = True
                if username_valid and password_valid:
                    return True
            except ValueError:
                pass
    return False


def check_new_pass_match(pass1, pass2):
    """ This function performs password tests to test and see if
    the new passwords entered match each other or not """
    not_match_error = False
    if pass1 != pass2:
        not_match_error = "The new passwords do not match"
    elif pass1 in common_passwords:
        not_match_error = "The new password is commonly used. Please use another password."
    elif not check_password_complexity(pass1):
        not_match_error = "The new password is not complex enough. Try to make it more complex."
    return not_match_error

def logger_check_test(curr_username):
    """ This function is designed to create a log that logs all failed login
    attempts. The log will include the date, time, and the IP address. Logs the
    failed login attempts to a specific file. """
    if not exists(FAILED_LOGIN_ATTEMPTS):
        open(FAILED_LOGIN_ATTEMPTS, "a", encoding="utf-8").close()
    current_time = datetime.now()
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        retrieve_ip_address = request.environ['REMOTE_ADDR']
    else:
        retrieve_ip_address = request.environ['HTTP_X_FORWARDED_FOR']
    with open(FAILED_LOGIN_ATTEMPTS, "a", encoding="utf-8") as failedlogfile:
        failedlogfile.write(current_time.isoformat() + " " + retrieve_ip_address + " "
                              + curr_username + "\n")

#returns the current date and time in the appropriate format.
def get_time_date():
    """ Returns the current time and date """
    time_today = datetime.now()
    date_today = time_today.strftime("%B %d %Y, %I:%M:%S %p")
    return date_today

#the following routes are all available routes or pages to be loaded as part of the webpage
#mulltiple pages are part of this website
@app.route('/')
def home_page():
    """ This function is designed as the root page for all
    webpages and will post the current date and time on the
    webpage """
    date_today = get_time_date()
    if "username" in session:
        return render_template("index.html", content=[date_today])
    return redirect(url_for("login"))

#creates login form, so the user can have the ability to login
@app.route('/login', methods=["POST", "GET"])
def login():
    """ This function will be used for designing the login html webpage,
    so the user can have access to the entirety of the website. """
    if request.method == "POST":
        current_session_username = request.form["username"]
        current_session_password = request.form["password"]
        authenticate_user = False
        authenticate_user_pass = False
        #checking to see if user is already logged in using salt hash
        with open(NEW_PASS_FILE, "r", encoding="utf-8") as newpassfile:
            for name_already_registered in newpassfile:
                r_username, r_salt_hash = name_already_registered.split()
                if current_session_username == r_username:
                    authenticate_user = True
                    if sha256_crypt.verify(current_session_password, r_salt_hash):
                        authenticate_user_pass = True
                        break
                authenticate_user = False
                authenticate_user_pass = False
        #if the correct username or password is not entered
        # a message will be displayed.
        if not authenticate_user or not authenticate_user_pass:
            flash("Invalid username or password entered")
        # else the username that was entered will be stored and will take the user
        # to the index (Home) webpage
        else:
            session["username"] = current_session_username
            return redirect(url_for('login'))
    else:
        if "username" in session:
            return redirect(url_for('login'))
    #login.html webpage form will be rendered for the user to login
    return render_template("login.html")

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
        if "username" in session:
            flash("Logout to create a new registration.")
        current_session_username = None
        current_session_password = None
        error_status = None
        current_session_username = request.form["username"]
        current_session_password = request.form["password"]
        #error messages
        if not current_session_username:
            error_status = "ERROR - Please enter a Username:"
        elif not current_session_password:
            error_status = "ERROR - Please enter a Password:"
        elif if_user_registered(current_session_username):
            error_status = "ERROR - Username already registered."
        elif check_for_whitespace(current_session_username):
            error_status = "ERROR - Username must not contain any spaces."
        elif not check_password_complexity(current_session_password):
            error_status = "ERROR - Please enter a password which meets the complexity requirements below."
        if error_status:
            flash(error_status)
        else:
            password_hash_tech = sha256_crypt.hash(current_session_password)
            with open(NEW_PASS_FILE, "a", encoding="utf-8") as newpassfile:
                newpassfile.write(current_session_username + " " + password_hash_tech + "\n")
            flash("Registration successful, please login.")
            return redirect(url_for('login'))
    return render_template("registration.html")

#This route resembles the Password update form, and the accompanied content
#follows for the Password update form information.
@app.route('/Update_Pass', methods=["POST", "GET"])
def update_password():
    """ This function is designed for the update_pass form webpage """
    if request.method == "POST":
        encounter_error = None
        if "username" in session:
            curr_username = session["username"]
            prev_password = request.form["Old Password"]
            new_pass1 = request.form["New Password"]
            new_pass2 = request.form["Re-enter New Password"]

            encounter_error = check_new_pass_match(new_pass1, new_pass2)

            if not right_user_match(curr_username, prev_password):
                encounter_error = "Incorrect old password entered"
            #if error is produced the message will be displayed on the change password form.
            if encounter_error:
                flash(encounter_error)
            else:
                with open(NEW_PASS_FILE, "r", encoding="utf-8") as newpassfile:
                    with open(TEMP_PASS_FILE, "a", encoding="utf-8") as temppassfile:
                        for stored_pass_information in newpassfile:
                            try:
                                r_username, r_salt_hash = stored_pass_information.split()
                                identical_username = curr_username == r_username
                                identical_password = sha256_crypt.verify(prev_password, r_salt_hash)
                                if identical_username and identical_password:
                                    t_salt_hash = sha256_crypt.hash(new_pass1)
                                    temppassfile.write(curr_username + " " + t_salt_hash + "\n")
                                else:
                                    temppassfile.write(r_username + " " + r_salt_hash + "\n")
                            except ValueError:
                                pass
                try:
                    os.remove(NEW_PASS_FILE + ".bak")
                except OSError:
                    pass
                os.rename(NEW_PASS_FILE, NEW_PASS_FILE + ".bak")
                os.rename(TEMP_PASS_FILE, NEW_PASS_FILE)
                flash("Password has been Updated")
                return render_template("index.html")
        else:
            flash("You must be logged in to change password.")
            return redirect(url_for("login"))
    return render_template("Update_Pass.html")

#authenticates a new user with their name on it
@app.route('/user')
def user():
    """ Serving the page of user's name on it. """
    if "username" in session:
        username = session["username"]
        return f"<h1>{username}</h1>"
    return redirect(url_for('login'))

@app.route('/Page1')
def page1():
    """ DESCRIPTION HERE """
    date_today = get_time_date()
    if "username" in session:
        return render_template('Training.html', content=[date_today])
    return abort(401)

@app.route('/Page2')
def page2():
    """ DESCRIPTION HERE """
    date_today = get_time_date()
    if "username" in session:
        return render_template('Certifications.html', content=[date_today])
    return abort(401)

@app.route('/Page3')
def page3():
    """ DESCRIPTION HERE """
    date_today = get_time_date()
    if "username" in session:
        return render_template("Table.html", content=[date_today])
    return abort(401)

#Starts the executing of program once program enters main.
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
