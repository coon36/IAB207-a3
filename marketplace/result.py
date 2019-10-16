# from flask import Blueprint, render_template
# from .models import Listing
# from . import db
from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import Listing, Bid
from .forms import ItemCreationForm
from datetime import datetime, date
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os
from sqlalchemy import desc

bp = Blueprint('result', __name__, url_prefix='/results')

@bp.route('/condition/<game_condition>') 
def condition(game_condition): 
  listings = Listing.query.filter_by(game_condition=game_condition).all() 
  return render_template('Result.html', listings=listings)

@bp.route('/classification/<game_classification>') 
def classification(game_classification): 
    listings = Listing.query.filter_by(game_classification=game_classification).all()
    return render_template('Result.html', listings=listings)

@bp.route('/platform/<game_platform>') 
def platform(game_platform): 
    print(game_platform)
    listings = Listing.query.filter_by(game_platform=game_platform).all() 
    return render_template('Result.html', listings=listings)

@bp.route('/genre/<game_genre>') 
def genre(game_genre): 
    listings = Listing.query.filter_by(game_genre=game_genre).all() 
    return render_template('Result.html', listings=listings)