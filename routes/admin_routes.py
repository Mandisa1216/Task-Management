from flask import Blueprint
from ..controllers import admin_controllers
from ..routes import admin_routes

app.route ('/signup',methods = ["POST","GET"])(admin_controllers.signup)
app.route ('/login',methods = ["POST","GET"]) (admin_controllers.login)