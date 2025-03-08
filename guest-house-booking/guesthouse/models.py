from guesthouse import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#db classes
class User(db.Model, UserMixin):
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
    address = db.Column(db.String(255), nullable=False)   
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)

'''
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
    __tablename__ = 'foodoptions'
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
#database classes end here'
'''