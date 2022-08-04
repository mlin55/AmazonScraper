from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from scraper.scraper import scrapeForProduct, analyzeProductData

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
  products = []
  if request.method == 'POST':
    try:
      product_name = request.form['productInput']
      products = scrapeForProduct(product_name, 1)
      analyzeProductData(products)
    except:
      return 'There was an issue scraping the data for this product from Amazon'
  return render_template('index.html', products=products)

  # image  |   name    |    price    |      numReviews      |       stars

if __name__ == '__main__':
  app.run(debug=True)