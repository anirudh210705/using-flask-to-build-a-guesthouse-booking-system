from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):
  '''
  Registration class 
  first, last name of minimum length 3 to maxlength 20
  9 charachter rollnumber
  '''
  #username
  fname = StringField('First Name', validators=[DataRequired(), Length(min = 3, max = 20)])
  lname = StringField('Last Name', validators=[DataRequired(), Length(min = 3, max = 20)])
  #rollnumber
  rollnumber = StringField('Roll Number', validators=[DataRequired(), Length(min = 9, max = 9)])
  #email
  email = StringField('Email', validators=[DataRequired(), Email()])
  #password
  password = PasswordField('Password', validators = [DataRequired()])
  confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
  
  #submit
  submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
  '''
  login form
  login trough email address
  '''
  #email
  email = StringField('Email', validators=[DataRequired(), Email()])
  #password
  password = PasswordField('Password', validators = [DataRequired()])
  remember = BooleanField('Remember Me')
  #submit
  submit = SubmitField('Login')
