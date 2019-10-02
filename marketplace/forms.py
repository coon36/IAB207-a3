
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo

#login form
class LoginForm(FlaskForm):
    user_name = StringField("Username", validators=[InputRequired('Please enter your username.')])
    password = PasswordField("Password", validators=[InputRequired('Please enter your password.')])
    submit = SubmitField("Login")

#registration form
class RegisterForm(FlaskForm):
    user_name = StringField("Username", validators=[InputRequired('Please enter a username.')])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email address.")])
    #linking two fields - password should be equal to data entered in confirm
    password = PasswordField("Password", validators=[InputRequired('Please enter a password.'),
                  EqualTo('confirm', message="Passwords should match.")])
    confirm = PasswordField("Please confirm your password.")
    #submit button
    submit = SubmitField("Register")

# for jared, whenever
#create listing form
#class CreateListingForm(FlaskForm):
#    listing_title = StringField("Listing Title:", validators=[InputRequired('Please enter a title.')])
#    purchase_price =
