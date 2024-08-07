from ..import mongo
from flask_bcrypt import Bcrypt


class Get_admin:
    def admin_collection(admin_data):
        return mongo.db.user_collection.insert_one(admin_data)
        
    
    
