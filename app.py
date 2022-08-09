from flask import Flask, render_template, url_for, request, redirect
from scraper.scraper import scrapeForProduct, analyzeProductData

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
  products = []
  if request.method == 'POST':
    # try:
    product_name = request.form['productName']
    num_products = int(request.form['numProducts'])
    review_weight = float(request.form['reviewDropdown'])
    price_weight = float(request.form['priceDropdown'])
    rating_weight = float(request.form['ratingDropdown'])
    products = scrapeForProduct(product_name, num_products)
    analyzeProductData(products, review_weight, price_weight, rating_weight)
    return render_template('index.html', products=products, productName=product_name, numProducts=num_products)
    # except:
    #   return 'There was an issue scraping the data for this product from Amazon'
  else:
    return render_template('index.html', products=products)

@app.route('/loading')
def loading():
  return render_template('loading.html')

  # image  |   name    |    price    |      numReviews      |       stars

if __name__ == '__main__':
  app.run(debug=True)