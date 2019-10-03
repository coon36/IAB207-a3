
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, IntegerField, FloatField
from wtforms.validators import InputRequired, Length, Email, EqualTo, DataRequired
from wtforms import RadioField, StringField, SubmitField, SelectField
from wtforms.fields.html5 import DateField

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





ALLOWED_FILE = {'png', 'jpg', 'JPG', 'PNG', 'bmp', 'JPEG'}

class ItemCreationForm(FlaskForm):
    listing_title = StringField('Listing Title', validators=[InputRequired()])
    purchase_price = StringField('Price', validators=[InputRequired()], )
    description = TextAreaField('Description', validators=[InputRequired(), Length(min=10, max=200)])
    game_condition = RadioField('Condition Of Game', choices=[('value','New'),('value_two','Preowned')])
    game_release_date = DateField('Release Date', validators=[InputRequired()], format='%Y-%m-%d')
    game_genre = SelectField('Genre', choices=[('Action', 'Action'), ('Adventure', 'Adventure',), ('Casual', 'Casual'), 
    ('Party', 'Party'), ('Role-Playing', 'Role-Playing'), ('Simulation', 'Simulation'), 
    ('Strategy', 'Strategy'), ('Sports', 'Sports'), ('MMO', 'MMO')])
    game_classification = SelectField('Classification', choices=[('G', '(G)'), ('PG', '(PG)'), ('M', '(M)'), ('MA', '(MA15+)'), ('R18', '(R18+)')])
    game_platform = SelectField('Platform', validators=[InputRequired()], choices=[('Arcade', 'Arcade'), ('Atari', 'Atari'), 
    ('Commodore 64', 'Commodore 64'), ('Nintendo', 'Nintendo'), ('Nintendo 3DS', 'Nintendo 3DS'), ('Nintendo DS', 'Nintendo DS'),  
    ('Nintendo Switch', 'Nintendo Switch'), ('Nintendo Wii', 'Nintendo Wii'), ('Nintendo Wii U', 'Nintendo Wii U'),  ('PC', 'PC'),
    ('Playstation 3', 'Playstation 3'), ('Playstation Classic', 'Playstation Classic'), ('Playstation Vita', 'Playstation Vita'),
    ('SEGA', 'SEGA'), ('Xbox 360', 'Xbox 360'), ('Xbox One', 'Xbox One')])
    listing_img_url = FileField('Upload Image', validators=[FileRequired(message='Image can not be empty'),
                                            FileAllowed(ALLOWED_FILE, message='Only supports png, jpg, JPG, PNG, bmp, JPEG')])
    submit = SubmitField("Create Listing")