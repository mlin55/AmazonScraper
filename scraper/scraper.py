from scrape import scrape
from analysis import assignRecommendationScores, displaySignificantData

products = scrape('Sofa', 10)
# analyze product data
displaySignificantData(products)
assignRecommendationScores(products)
for product in products:
  print(f"Product: {product.name}")
  print(f"Link: {product.link}")
  print(f"Image: {product.image}\n")