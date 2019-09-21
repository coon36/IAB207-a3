# In forms.py
#add the types of files allowed as a set
ALLOWED_FILE = {'png', 'jpg', 'JPG', 'PNG', 'bmp'}

class DestinationFileForm(FlaskForm):
  name = StringField('Country', validators=[InputRequired()])
  description = TextAreaField('Description', 
            validators=[InputRequired(), Length(min=10, max=200)])
  
  #create a filefield that takes two validators - File required and File Allowed
  image = FileField('Destination Image', validators=[FileRequired(message='Image can not be empty'),
                                         FileAllowed(ALLOWED_FILE, message='Only support png, jpg, JPG, PNG, bmp')])
    
  currency = StringField('Currency', validators=[InputRequired()])
  submit = SubmitField("Create")

# in __init__.py create_app function

#the folder to store images
    UPLOAD_FOLDER = '/static/image'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    

#in the views.py
# a simple function: does not handle errors in file types and file not being uploaded

#for file upload
from werkzeug.utils import secure_filename
import os



def check_upload_file(form):
 # get file data from form
    fp = form.image.data
    filename = fp.filename
  # get the current path of the module file… store file relative to this path
    BASE_PATH = os.path.dirname(__file__)
  #upload file location – directory of this file/static/image
    upload_path = os.path.join(BASE_PATH, 'static/image', secure_filename(filename))
 # store relative path in DB as image location in HTML is relative
    db_upload_path = '/static/image/'+ secure_filename(filename)
   # save the file and return the db upload path
    fp.save(upload_path)
    return db_upload_path


# views.py the route to create the destination
@bp.route('/create', methods = ['GET', 'POST'])
def create():
  form = DestinationFileForm()
  if form.validate_on_submit():
    # call the function that checks the file and returns
    db_file_path = check_upload_file(form)

    destination = Destination(name=form.name.data, 
                description=form.description.data,
                image=db_file_path,
                currency=form.currency.data)
    # add the object to the db session
    db.session.add(destination)
    # commit to the database
