from flask import Blueprint
from ..controllers import admin_controllers

app = Blueprint('admin', __name__)

# Define routes within the blueprint
app.route('/signup', methods=['POST', 'GET'])(admin_controllers.signup)
app.route('/login', methods=['POST', 'GET'])(admin_controllers.admin_login)
