from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'eeff23d482f6fe2af2bc27ae52df9a22'

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
        flash(f'Account created for {form.username.data}!', 'success')
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

if __name__ == '__main__':
    app.run(debug=True)