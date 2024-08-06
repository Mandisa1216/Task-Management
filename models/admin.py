from ..import mongo
from flask import Flask, request, jsonify


class Signup:
    def create_user(admin_data):
        print(f"User created: {admin_data}")
        return True
    
    
