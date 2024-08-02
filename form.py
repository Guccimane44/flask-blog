from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    username =  StringField('Username', 
                            validators=[DataRequired(),Length(min=2, max=20)])
    password = PasswordField('Password', 
                            validators=[DataRequired(), Length(min=6, max=10)])
    confirm_password = PasswordField('Confirm Password',
                            validators=[DataRequired(),Length(min=6, max=10), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username =  StringField('Username', 
                        validators=[DataRequired()])
    password = PasswordField('Password', 
                        validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')
    

    