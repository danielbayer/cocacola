from flaskblog.models import User, Post
from flaskblog import app
from flask import render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm

posts = [
	{
		'author': 'Daniel Bayer',
		'title': 'TEST',
		'content': 'testContent',
		'date_posted': 'Jan 1 1998'
	},
	{
		'author': 'Idan Lutzki',
		'title': 'TEST1',
		'content': 'testContent1',
		'date_posted': 'Jan 2 1998'
	},
	{
		'author':'Tomer Hadad',
		'title': 'test2',
		'content': 'testContent1',
		'date_posted': 'Jan 3 1998'
	}
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
