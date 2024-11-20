from flask import Blueprint, render_template, redirect, flash, url_for
from .forms import RegisterForm
from app import bcrypt



auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		username = form.username.data
		email = form.email.data
		passwd_hash = bcrypt.generate_password_hash(form.passwd.data).decode('utf-8')
		flash('Your registration is successful', 'success')
		return redirect(url_for('main.index'))
	return render_template('auth/register.html', form=form)