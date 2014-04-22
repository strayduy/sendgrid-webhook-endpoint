# Third party libs
import flask
from flask import Blueprint
from flask import request

# Our libs
from ..database import EventsDB

blueprint = Blueprint('webhook',
                      __name__,
                      url_prefix='/webhook',
                      static_folder='../static',
                      template_folder='../templates')

@blueprint.route('/events', methods=['post'])
def events():
    data = request.get_json()
    EventsDB.db.events.insert(data)
    return ''

