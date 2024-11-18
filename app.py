from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Get MongoDB credentials from environment variables
username = os.getenv('MONGODB_USERNAME')
password = os.getenv('MONGODB_PASSWORD')
cluster_url = os.getenv('MONGODB_CLUSTER_URL')
db_name = os.getenv('MONGODB_DB_NAME')

# MongoDB Connection URI
mongo_uri = f'mongodb+srv://{username}:{password}@{cluster_url}/{db_name}?retryWrites=true&w=majority'

# Connect to MongoDB Atlas
client = MongoClient(mongo_uri)

# Access the database and collection
db = client[db_name]
products_collection = db.products

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    # Fetch all products from the collection
    products = list(products_collection.find())
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
