from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

#username and password
username = 'c0920016'
password = 'harish1234sree'

# Connect to MongoDB Atlas
client = MongoClient(f'mongodb+srv://{username}:{password}@shop-db.eexyk.mongodb.net/shop_db?retryWrites=true&w=majority&appName=shop-db')
db = client.shop_db
products_collection = db.products

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products = list(products_collection.find())
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
