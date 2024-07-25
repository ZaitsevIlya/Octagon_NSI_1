from flask import Blueprint
from src.controllers.abbreviations import handle_post

reductions = Blueprint('routes', __name__)

@reductions.route('/', methods=['POST'])
def main():
    return handle_post()