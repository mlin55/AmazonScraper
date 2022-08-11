from scraper.scrape import scrape
from scraper.analysis import assignRecommendationScores

def scrapeForProduct(productName, numProducts):
  return scrape(productName, numProducts)

def analyzeProductData(products, reviewWeight, priceWeight, starWeight):
  assignRecommendationScores(products, reviewWeight, priceWeight, starWeight)