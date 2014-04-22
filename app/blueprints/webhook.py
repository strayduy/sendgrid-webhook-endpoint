# Third party libs
import flask
from flask import Blueprint

blueprint = Blueprint('webhook',
                      __name__,
                      url_prefix='/webhook',
                      static_folder='../static',
                      template_folder='../templates')

@blueprint.route('/events', methods=['post'])
def events():
    return ''

