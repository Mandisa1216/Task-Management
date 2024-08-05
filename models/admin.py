from ..import mongo
from flask import Flask, request, jsonify


class Signup:
    def create_user(admin_data):
        print(f"User created: {admin_data}")
        return True
    
    
class Admin(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password_hash = db.Column(db.String(128), nullable=False)

