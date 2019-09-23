from . import db
from datetime import datetime
from flask_login import UserMixin


class User(db.Model,UserMixin):
    __tablename__='users' # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
	#password is never stored in the DB, an encrypted password is stored
	# the storage should be at least 255 chars long
    password_hash = db.Column(db.String(255), nullable=False)


    # relation to call user.comments and comment.created_by
    comments = db.relationship('Comment', backref='user')

    def __repr__(self): #string print method
        return "<Name: {}, ID: {}>".format(self.name, self.id)
   


class Comment(db.Model):
    __tablename__='comments' 
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, index=True)
    created_at = db.Column(db.DateTime, default=datetime.now())

    # define the foreign key - refers to <tablename.primarykey>
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self): #string print method
        return "<Text: {}, ID: {}, user_id: {}>".format(self.text, self.id, self.user_id)
   

  
   













 # relation to call user.comments and comment.created_by
#    comments = db.relationship('Comment', backref='user')