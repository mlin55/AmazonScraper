from scraper.scrape import scrape
from scraper.analysis import assignRecommendationScores, displaySignificantData

def scrapeForProduct(productName, numProducts):
  return scrape(productName, numProducts)

def analyzeProductData(products, reviewWeight, priceWeight, starWeight):
  # analyze product data
  # displaySignificantData(products)
  assignRecommendationScores(products, reviewWeight, priceWeight, starWeight)
  # for product in products:
  #   print(f"Product: {product.name}")
  #   print(f"Link: {product.link}")
  #   print(f"Image: {product.image}\n")