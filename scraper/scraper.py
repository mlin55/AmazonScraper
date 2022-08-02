from scraper.scrape import scrape
from scraper.analysis import assignRecommendationScores, displaySignificantData

def scrapeForProduct(productName, maxPageCount):
  return scrape(productName, maxPageCount)

def analyzeProductData(products):
  # analyze product data
  displaySignificantData(products)
  assignRecommendationScores(products)
  for product in products:
    print(f"Product: {product.name}")
    print(f"Link: {product.link}")
    print(f"Image: {product.image}\n")