from flask import Flask, render_template, url_for, request, redirect
from scraper.scraper import scrapeForProduct, analyzeProductData
from PIL import Image, ImageDraw

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
  products = []
  if request.method == 'POST':
    try:
      redirect('/loading')
      product_name = request.form['productInput']
      products = scrapeForProduct(product_name, 1)
      analyzeProductData(products)
      return render_template('index.html', products=products, productName=product_name)
    except:
      return 'There was an issue scraping the data for this product from Amazon'
  else:
    return render_template('index.html', products=products)

@app.route('/loading')
def loading():
  return render_template('loading.html')

  # image  |   name    |    price    |      numReviews      |       stars

if __name__ == '__main__':
  app.run(debug=True)