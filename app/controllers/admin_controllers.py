from flask import Flask,url_for,redirect,Response,request,render_template,flash, jsonify
from bson.objectid import ObjectId
from ..models.admin import  Get_admin
from flask_jwt_extended import JWTManager,create_access_token,jwt_required,get_jwt_identity,get_jwt


def signup_admin():
 if request.method == 'POST':
    full_name = request.json.get('full_name')
    email = request.json.get('email')
    cell_number = request.json.get('cell_number')
    password = request.json.get('password')
    
    signup = {'full_name': full_name,  'email': email,'cell_number': cell_number, 'password': password,}
    Get_admin.create_new(signup)
   
    return jsonify({'message': 'succesful'})

# def admin_login():
#     admin_login = {
#         'email': request.json.get('email'),
#         'password': request.json.get('password')
#     }

    

 