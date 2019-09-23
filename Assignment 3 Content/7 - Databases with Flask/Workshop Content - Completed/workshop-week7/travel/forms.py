from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField
from wtforms.validators import InputRequired, Length

class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()])
  submit = SubmitField('Create')

class DestinationForm(FlaskForm):
  name = StringField('Country', validators=[InputRequired()])
  description = TextAreaField('Description', 
            validators=[InputRequired(), Length(min=10, max=200)])
  image = StringField('Cover Image', validators=[InputRequired()])
  currency = StringField('Currency', validators=[InputRequired()])
  submit = SubmitField("Create")

