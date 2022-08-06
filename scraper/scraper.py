from scraper.scrape import scrape
from scraper.analysis import assignRecommendationScores, displaySignificantData

def scrapeForProduct(productName, numProducts):
  return scrape(productName, numProducts)

def analyzeProductData(products):
  # analyze product data
  displaySignificantData(products)
  assignRecommendationScores(products, 0.4, 0.4, 0.2)
  # for product in products:
  #   print(f"Product: {product.name}")
  #   print(f"Link: {product.link}")
  #   print(f"Image: {product.image}\n")