from flask import Blueprint

my_blueprint = Blueprint('my_blueprint', __name__, url_prefix="/blueprint")

@my_blueprint.route('/hello')
def hello():
    return "<h1> Hello from the Blueprint! <h1>"

@my_blueprint.route('/test')
def test():
    return "<h1> Test Function from Blueprint! <h1>"