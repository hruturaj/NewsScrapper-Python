from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from project.models import User

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")

class RegistrationForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password" ,validators=[DataRequired(), EqualTo('password_confirm', message="Please Enter Correct Password")])
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Register")

    def check_email(self, field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError("Email already registered!")
    
    def check_user(self, field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError("User already Exist! Try another username")
    

class WorldForm(FlaskForm):
    country = SelectField("Enter Country Name" ,
                choices=[ ('au', 'Australia'), ('ca', 'Canada'),
                          ('cn', 'China'), ('fr', 'France'), 
                          ('de', 'Germany'), ('in', 'India'), 
                          ('it', 'Italy'), ('jp', 'Japan'), 
                          ('nz', 'New Zealand'), ('uk', 'United Kingdom'),
                          ('us', 'United States') ])
    submit = SubmitField('Search')