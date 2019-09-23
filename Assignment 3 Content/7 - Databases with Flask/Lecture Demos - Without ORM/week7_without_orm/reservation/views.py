from flask import Blueprint,render_template, redirect, url_for, request
from .models import Hotel, Room, _connect_db, close, create_hotel,add_room, get_hotels
from .forms import ContactForm, HotelForm
mainbp = Blueprint('main',__name__)

@mainbp.route('/')
def index():
    tag_line='You need a vacation'
    hotels = get_hotel_list()
    form=ContactForm()
    return render_template('index_bootstrap.html', tag_line=tag_line,
                    form=form, hotels=hotels)




@mainbp.route('/contact', methods=['GET','POST']) # both get and post
def create_contact():
     print('In contact view function')
     form = ContactForm()
     if form.validate_on_submit():
          print("Form has been submitted successfully")
          print(request.form['user_name'])
     return redirect(url_for('main.index'))


@mainbp.route('/hotel/create', methods=['GET','POST']) # both get and post
def add_hotel():
     print('In create hotel')
     form = HotelForm()
     
     if form.validate_on_submit():
          print("Form has been submitted successfully")
          _connect_db()

          new_hotel = Hotel(form.name.data, form.description.data,
                              form.image.data)
          
          hotel_id = create_hotel(new_hotel)
          add_room(hotel_id, form.room.room_type.data, 
                              form.room.room_desc.data,
                              form.room.num_rooms.data, 
                              form.room.price.data)
          
          #return redirect(url_for('main.create_hotel'))
          close()
     return render_template('forms.html', form=form)



def get_hotel_list():
     
     _connect_db()
     hotelList = get_hotels()
     close()
     return hotelList