from flask import Blueprint, render_template, request
from .models import Listing
from . import db


bp = Blueprint('result', __name__, url_prefix='/results')

@bp.route('/condition_id=<game_condition>') 
def condition(game_condition):
  listings = Listing.query.filter_by(game_condition=game_condition).all()
  return render_template('result.html', listings=listings)

@bp.route('/classification_id=<game_classification>') 
def classification(game_classification):
    listings = Listing.query.filter_by(game_classification=game_classification).all()
    return render_template('result.html', listings=listings)

@bp.route('/platform_id=<game_platform>') 
def platform(game_platform):
    print(game_platform)
    listings = Listing.query.filter_by(game_platform=game_platform).all() 
    return render_template('result.html', listings=listings)

@bp.route('/genre_id=<game_genre>') 
def genre(game_genre):
    listings = Listing.query.filter_by(game_genre=game_genre).all() 
    return render_template('result.html', listings=listings)