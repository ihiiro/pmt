from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import (Length, EqualTo, Email, DataRequired,
ValidationError)
from app.models import User

class RegisterForm(FlaskForm):
    username = StringField(label='Username:', validators=[Length(min=3, max=20),
    DataRequired()], render_kw={'autofocus':True})
    email = StringField(label='Email Address:', validators=[Email(),
    DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6),
    DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=
    [EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

    def validate_username(self, check_username_input):
        user = User.query.filter_by(username=check_username_input.data).first()
        if user: # if user already exists
            raise ValidationError('username unavailable')

    def validate_email(self, check_email_input):
        user = User.query.filter_by(email=check_email_input.data).first()
        if user:
            raise ValidationError('email address unavailable')

class LoginForm(FlaskForm):
    username = StringField(label='Username:', validators=[DataRequired()],
    render_kw={'autofocus':True})
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Login')