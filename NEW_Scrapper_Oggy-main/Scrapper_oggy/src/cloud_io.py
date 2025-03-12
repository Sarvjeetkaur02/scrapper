 
from pymongo import MongoClient

class MongoIO:
    def __init__(self):
        # Replace with your MongoDB connection string
        self.client = MongoClient("your_mongodb_connection_string")
        self.db = self.client["myntra_reviews"]

    def store_reviews(self, product_name, reviews):
        """
        Store reviews in MongoDB.
        """
        collection = self.db[product_name]
        collection.insert_many(reviews.to_dict("records"))
