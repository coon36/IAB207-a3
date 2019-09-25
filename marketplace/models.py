from . import db
from datetime import datetime
from flask_login import UserMixin, LoginManager

class User(db.Model,UserMixin):
    __tablename__='Users' # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    account_creation_date = db.Column(db.Date, nullable=False)
    profile_img_url = db.Column(db.String(60), nullable=False, default='default.jpg')
    user_name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    email_id = db.Column(db.String(100), index=True, nullable=False)
	#password is never stored in the DB, an encrypted password is stored
	# the storage should be at least 255 chars long
    password_hash = db.Column(db.String(255), nullable=False)

    def __repr__(self): #string print method
        return "<Name: {}, ID: {}>".format(self.user_name, self.id)

class Bid(db.Model):
    __tablename__='Bids'

    id = db.Column(db.Integer, primary_key=True)
    date_of_bid = db.Column(db.Date, nullable=False)
    bid_price = db.Column(db.Float, nullable=False)
    ##FOREIGN KEY IS USER_ID AND LISTING_ID

    def __repr__(self):
        return "<Name: {}, ID: {}>".format(self.date_of_bid, self.id)


class Transaction(db.Model):
    __tablename__ = 'Purchases'

    id = db.Column(db.Integer, primary_key=True)
    purchase_date = db.Column(db.Date, nullable=False)
    price_paid = db.Column(db.Float, nulllable=False)

    #foreign keys are user_id and listing_id
    def __repr__(self):
        return "<Name: {}, id: {}>".format(self.purchase_date, self.id)


class Listing(db.Model):

    __tablename__= 'Items'
    id = db.Column(db.Integer, primary_key=True)
    listing_title = db.Column(db.String(150), index=True)
    purchase_price = db.Column(db.Float, nulllable=False)
    date_posted = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    availability_status = db.Column(db.String(64), nullable=False)
    game_condition = db.Column(db.String(64), nullable=False)
    game_release_date = db.Column(db.Date, nullable=False)
    listing_img_url = db.Column(db.String(60), nullable=False, default='default.jpg')
    game_classification = db.Column(db.String(64), nullable=False)
    game_platform = db.Column(db.String(64), nullable=False)
    game_genre = db.Column(db.String(64), nullable=False)
    backwards_compatibility = db.Column(db.String(64), nullable=False)

    hotelid = db.Column(db.Integer, db.ForeignKey('hotels.id'))
    userid = db.Column(db.Integer, db.ForeignKey('users.id'))
    # foreign key is user_id

    def __repr__(self):
        return "<id: {} from user {} >".format(self.comment, self.userid)


