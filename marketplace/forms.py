
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, IntegerField, DateField, FloatField
from wtforms.validators import InputRequired, Length, Email, EqualTo, DataRequired
from wtforms import RadioField, StringField, SubmitField

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


ALLOWED_FILE = {'png', 'jpg', 'JPG', 'PNG', 'bmp', 'JPEG'}

class ItemCreationForm(FlaskForm):
    listing_title = StringField('Listing Title', validators=[InputRequired()])
    purchase_price = StringField('Price', validators=[InputRequired()], )
    description = TextAreaField('Description', validators=[InputRequired(), Length(min=10, max=200)])
    game_condition = RadioField('Condition Of Game', choices=[('value','New'),('value_two','Preowned')])
    game_release_date = DateField('Release Date', validators=[InputRequired()], format='%Y-%m-%d')
    game_genre = StringField('Genre', validators=[InputRequired()])
    game_classification = StringField('Classification', validators=[InputRequired(),])
    game_platform = StringField('Platform', validators=[InputRequired()])
    listing_img_url = FileField('Upload Image', validators=[FileRequired(message='Image can not be empty'),
                                            FileAllowed(ALLOWED_FILE, message='Only supports png, jpg, JPG, PNG, bmp, JPEG')])
    submit = SubmitField("Create Listing")