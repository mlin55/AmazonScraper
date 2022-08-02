from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from scraper.scraper import scrapeForProduct, analyzeProductData

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
  # if request.method == 'POST':
  #   try:
  #     product_name = request.form['productInput']
  #     products = scrapeForProduct(product_name)
  #   except:
  #     return 'There was an issue scraping the data for this product from Amazon'
  products = scrapeForProduct('Water bottles', 10)
  analyzeProductData(products)
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)