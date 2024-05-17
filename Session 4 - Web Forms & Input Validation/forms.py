from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SelectField,
    DateField,
    PasswordField,
    SubmitField,
    BooleanField
)
from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    Optional,
    EqualTo
)


class SignupForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(), Length(2, 30)]
    )
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )
    gender = SelectField(
        "Gender",
        choices=["Male", "Female", "Other"],
        validators=[Optional()]
    )
    dob = DateField(
        "Date of Birth",
        validators=[Optional()]
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(5, 25)]
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[DataRequired(), Length(5, 25), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(5, 25)]
    )
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")
