from flask import Flask,url_for,redirect,Response,request,render_template,session, jsonify
from ..models.admin import Signup
from flask import Flask, render_template, request, redirect, url_for
import bcrypt

def signup():
    admin = {
    "full_name" : request.json.get('full_name'),
    "email" : request.json.get('email'),
    "cell_number" : request.json.get('cell_number'),
    "password" : request.json.get('password')
    }

    admin.create_user(admin)
    return jsonify({'message': 'succes'}),400

def admin_login():
    admin_login = {
        'email': request.json.get('email'),
        'password': request.json.get('password')
    }

    

 