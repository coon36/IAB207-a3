from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField
from wtforms.validators import InputRequired

# this is a form class that inherits from FlaskForm
class CommentForm(FlaskForm):
  #the form is simple with a text field and a submit button
  text = TextAreaField('Comment', [InputRequired()])
  submit = SubmitField('Create')
