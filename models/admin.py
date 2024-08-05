class user:
      def create_user(details):
         return mongo.db.user_collection.insert_one(details)
