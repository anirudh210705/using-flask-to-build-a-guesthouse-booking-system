from guesthouse.models import User#, GuestHouse, FoodOptions, BookingQueue, Booking, Authentication
from flask import render_template, url_for, flash, redirect
from guesthouse.forms import RegistrationForm, LoginForm
from guesthouse import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

#register route
@app.route("/register", methods=['GET','POST'])
def register():
    '''
    if current_user.is_authenticated:
        return redirect(url_for('home'))
        '''
    form = RegistrationForm()
    if form.validate_on_submit():
        '''
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
            username = form.username.data,
            fname = form.fname.data,
            lname = form.lname.data,
            rollnumber = form.rollnumber.data,
            email = form.email.data,
            address = form.address.data,
            age = form.age.data,
            gender = form.gender.data,
            password = hashed_password
        )
        #db.session.add(user)
        #db.session.commit()
        '''
        flash(f"your account has been created! You are now able to log in", 'success')
        return redirect(url_for('login'))
    else:
        print("Validation failed:", form.errors)
    
    return render_template('register.html', title='Register', form = form)
#login route
@app.route("/login", methods=['GET', 'POST'])
def login():
    '''if current_user.is_authenticated:
        return redirect(url_for('home'))'''
    form = LoginForm()
    if form.validate_on_submit():
        '''user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)'''
        return redirect(url_for('home'))
    else :
        flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form = form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))