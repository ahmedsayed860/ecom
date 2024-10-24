from flask import Blueprint, render_template


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/register')
def register():
    return render_template('register.html')


@main.route('/about')
def about():
    return render_template('about.html')
