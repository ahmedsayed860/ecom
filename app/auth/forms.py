from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class RegisterForm(FlaskForm):
    username = StringField("Nom d'utilisateur", validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    passwd = PasswordField('Mot de passe', validators=[DataRequired(), EqualTo('confirm_passwd', message='Password must match')])
    confirm_passwd = PasswordField('Confirm Password')
    submit = SubmitField("S'enregistrer")