from scrape import scrape
from analysis import assignRecommendationScores, displaySignificantData

products = scrape('Gaming PC', 10)
# analyze product data
displaySignificantData(products)
assignRecommendationScores(products)
for product in products:
  print(f"Product: {product.name}")
  print(f"Link: {product.link}\n")