import os
from pymongo import MongoClient
from dotenv import load_dotenv
import unittest

# Load environment variables from .env file
load_dotenv()

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        # Get MongoDB credentials from environment variables
        username = os.getenv('MONGODB_USERNAME')
        password = os.getenv('MONGODB_PASSWORD')
        cluster_url = os.getenv('MONGODB_CLUSTER_URL')
        db_name = os.getenv('MONGODB_DB_NAME')
        
        # MongoDB URI with dynamic environment variables
        self.mongo_uri = f'mongodb+srv://{username}:{password}@{cluster_url}/{db_name}?retryWrites=true&w=majority'

        # Connect to MongoDB Atlas
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[db_name]
        self.products_collection = self.db.products

    def test_insert_document(self):
        # Example test that inserts a document into the collection
        result = self.products_collection.insert_one({'name': 'Test Product', 'price': 10})
        self.assertIsNotNone(result.inserted_id)
