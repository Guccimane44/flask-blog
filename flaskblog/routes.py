from flask import render_template, url_for, flash, redirect
from flaskblog.form import RegistrationForm, LoginForm
from flaskblog import app


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Good day to ya',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Hello World',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, title='Home')


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == '000000':
            flash(f'Login successful for {form.username.data}!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login falied. Please check your username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
