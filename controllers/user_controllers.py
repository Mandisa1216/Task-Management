from flask import Flask,url_for,redirect,Response,request,render_template,session, jsonify
from ..models.user import user
from flask import Flask, render_template, request, redirect, url_for
from models import user

def signup():
    user = {
    "full_name" : request.json.get('full_name'),
    "email" : request.json.get('email'),
    "cell_number" : request.json.get('cell_number'),
    "password" : request.json.get('password')
    }

    user.create_user(user)
    return jsonify({'message': 'succes'}),400

def user_login():
    user_login = {
        'email': request.json.get('email'),
        'password': request.json.get('password')
    }