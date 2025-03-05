from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8ee438fdf6902277304fc65139931456'

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
    
    return render_template('register.html', title='Register', form = form)
#login route
@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form = form)


if __name__ == '__main__':
    app.run(debug = True)