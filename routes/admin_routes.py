from flask import Blueprint
from ..controllers import user_controllers
from ..routes import user_routers

app.route ("/signup",methods = ["POST","GET"])(admin_controllers.signup)
app.route ("/login",methods = ["POST","GET"]) (admin_controllers.login)