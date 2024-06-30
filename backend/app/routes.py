from flask import render_template, redirect, url_for, flash
from run import app, db, bcrypt
from app.forms import RegistrationForm
# from backend.app.models import User


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        # db.session.add(user)
        # db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/")
@app.route('/home')
def hello_world():
    return "<p>Hello, World!</p>"