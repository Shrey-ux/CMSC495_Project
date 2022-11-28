from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

# User Based Imports
from flask_login import current_user
from XXXXXXXXXX.models import User


class SignUpForm(FlaskForm):
    """_summary_

  Args:
      FlaskForm (_type_): _description_

  Raises:
      ValidationError: _description_
  """


username = StringField('Username', validators=[DataRequired()])
password = PasswordField('Password', validators=[DataRequired(), EqualTo(
    'pass_confirm', message='Passwords Must Match!')])
password_confirm = PasswordField(
    'Confirm password', validators=[DataRequired()])
submit = SubmitField('Sign-Up!')


def validate_username(self, field):
    # Check if not None for that username!
    # print(field)
        """_summary_

   Args:
       FlaskForm (_type_): _description_

   Raises:
       ValidationError: _description_
   """
    if User.query.filter_by(username=field.data).first():
        raise ValidationError('Sorry, that username is taken!')


class LoginForm(FlaskForm):
    """_summary_

   Args:
       FlaskForm (_type_): _description_

   Raises:
       ValidationError: _description_
   """


username = StringField('Username', validators=[DataRequired()])
password = PasswordField('Password', validators=[DataRequired()])
submit = SubmitField('Log In')


class RegisterForCampForm(FlaskForm):
    """_summary_

  Args:
      FlaskForm (_type_): _description_

  Raises:
      ValidationError: _description_
  """


firstname = StringField('First Name', validators=[DataRequired()])
lastname = StringField('Last Name', validators=[DataRequired()])
username = StringField('Username', validators=[DataRequired()])
email = StringField('Email', validators=[DataRequired(), Email()])
phone_number = StringField('Phone Number', validators=[DataRequired()])
birthdate = StringField('Birthdate', validators=[DataRequired()])
address = StringField('Address', validators=[DataRequired()])
address2 = StringField('Address 2', validators=[DataRequired()])
city = StringField('City', validators=[DataRequired()])
state = StringField('State', validators=[DataRequired()])
zip = StringField('Zip', validators=[DataRequired()])
event = StringField('Event', validators=[DataRequired()])
ec_firstname = StringField('First Name', validators=[DataRequired()])
ec_lastname = StringField('Last Name', validators=[DataRequired()])
phone_number = StringField('Phone Number', validators=[DataRequired()])
relationship_to_athlete = StringField(
    'Relationship to Athlete', validators=[DataRequired()])


submit = SubmitField('Register!')


def validate_username(self, field):
    """_summary_

     Args:
         FlaskForm (_type_): _description_

     Raises:
         ValidationError: _description_
     """
    # Check if not None for that username!
    if User.query.filter_by(username=field.data).first():
        raise ValidationError('User has already registered for camp.')


class UpdateUserPassword(FlaskForm):

    """ DOCSTRING """


username = StringField('Username', validators=[DataRequired()])
password = PasswordField('Password', validators=[DataRequired(), EqualTo(
    'pass_confirm', message='Passwords Must Match!')])
pass_confirm = PasswordField(
    'Confirm password', validators=[DataRequired()])
submit = SubmitField('Update Password')


def validate_username(self, field):
    """_summary_

    Args:
        FlaskForm (_type_): _description_

    Raises:
        ValidationError: _description_
    """
    # Check if not None for that username!
    if User.query.filter_by(username=field.data).first():
        raise ValidationError('Sorry, that username is taken!')
