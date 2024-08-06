from flask import Blueprint
from ..controllers import admin_controllers

app = Blueprint('admin', __name__)

# Define routes within the blueprint
app.route('/signup_admin', methods=['POST'])(admin_controllers.signup_admin)

