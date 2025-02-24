from flask import render_template, url_for, flash, redirect
from start import app, db, bcrypt
from start.forms import RegistrationForm, LoginForm
from start.models import User, Post
from flask_login import login_user, current_user, logout_user


posts = [
    {
        'author' : "Lee Kaburu",
        'title' : "Blog post 1",
        'content' : "First post content",
        "date_posted" : "April 30 2023"
    }, 
    {
        'author' : "John Doe",
        'title' : "Blog post 2",
        'content' : "Second post content",
        "date_posted" : "April 25 2023"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title='About ')


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been created! You are now able to log in!", "success")
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash("Login Unsuccussful. Please check email and password", "danger")
    return render_template('login.html', title='login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
def account():
    if current_user.is_authenticated:
        return render_template('account.html', title='Account')
    return redirect(url_for('login'))
