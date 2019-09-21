from flask import Blueprint,render_template, redirect, url_for, request
from .models import Hotel
from .forms import ContactForm

mainbp = Blueprint('main',__name__)

@mainbp.route('/')
def index():
    tag_line='You need a vacation'
    hotels = get_hotel_list()
    form=ContactForm()
    return render_template('index_reuse.html', tag_line=tag_line,
                    form=form, hotels=hotels)




@mainbp.route('/contact', methods=['GET','POST'])
def create_contact():
     form = ContactForm()
     if form.validate_on_submit():
          print("Form has been submitted successfully")
          print(request.form['user_name'])
     return redirect(url_for('main.index'))



def get_hotel_list():
    brisbane_hotel = Hotel('Brisbane', 'brisbane.jpg',
    'As the capital of the Sunshine State, we are blessed with idyllic subtropical weather all year round.')

    sydney_hotel = Hotel('Sydney', 'sydney.jpg',
    'From splendid Sydney Harbour, idyllic beaches and great national parks, to the marvellous creativity of the Sydney Opera House, dazzling entertainment and fascinating heritage, discover all the things to do and see throughout the year.')

    melbourne_hotel = Hotel('Melbourne', 'melbourne.jpg',
     'A packed agenda of food, wine, sports and arts is your introduction to the best of Melbourne – from its creative, exciting city centre, to its buzzing neighbourhood hubs.')

    hlist = list()
    hlist.append(brisbane_hotel)
    hlist.append(sydney_hotel)
    hlist.append(melbourne_hotel)
    return hlist