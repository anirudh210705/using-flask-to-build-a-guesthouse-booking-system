from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8ee438fdf6902277304fc65139931456'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


#database classes
db = SQLAlchemy(app)
class User(db.Model):
    '''
    User class contails the information about the user.
    Names are self explainable.
    needs to be modifed
    '''
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable=False, unique = True)
    fname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(20), nullable=False)
    rollnumber = db.Column(db.String(9), nullable= False)
    email = db.Column(db.String(120), nullable= False, unique = True)
    password = db.Column(db.String(60), nullable= False)

class GuestHouse(db.Model):
    """
    Guesthouse class. Names are self explainable.
    """
    __tablename__ = 'GuestHouse'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(60), nullable = False)
    description = db.Column(db.String(60))

class FoodOptions(db.Model):
    """
    unique id for each kind of cusine, cost per day, name of type
    """
    id = db.Column(db.Integer, primary_key=True)
    pricePerDay = db.Column(db.Integer, nullable = False)
    food_type = db.Column(db.String(40), nullable = False)

class BookingQueue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bookingIds = db.Column(db.String(40))

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    roomId = db.Column(db.Integer)
    foodId = db.Column(db.Integer)
    checkInDate = db.Column(db.DateTime)
    checkOutDate = db.Column(db.DateTime)
    dateOfBooking = db.Column(db.DateTime)
    confirmation = db.Column(db.Integer)
    feedback = db.Column(db.String(100))

class Authentication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    val = db.Column(db.Integer)
#database classes end here

#home route
@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

#register route
@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account create for {form.fname.data}!", 'success')
        return redirect(url_for('home'))
    else:
        print("Validation failed:", form.errors)
    
    return render_template('register.html', title='Register', form = form)
#login route
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"You have logged in.", 'success')
        return redirect(url_for('home'))
    return render_template('login.html', title='Login', form = form)


if __name__ == '__main__':
    app.run(debug = True)
