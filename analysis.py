from product import Product

def displaySignificantData(products):
  minPrice, maxPrice, minReviews, maxReviews, minStarRating, maxStarRating = float('inf'), float('-inf'), float('inf'), float('-inf'), float('inf'), float('-inf')
  cheapest, mostExpensive, leastReviewed, mostReviewed, lowestSR, highestSR = Product(), Product(), Product(), Product(), Product(), Product()
  print(f"Total products found: {len(products)}")

  for product in products:
    if product.price:
      price = float(product.price)
      # if price == 0 then the price was not recorded, so we don't want to include it
      if minPrice > price and price != 0:
        minPrice = price
        cheapest = product
      if maxPrice < price and price != 0:
        maxPrice = price
        mostExpensive = product

    if product.numReviews:
      numReviews = float(product.numReviews)
      if minReviews > numReviews:
        minReviews = numReviews
        leastReviewed = product
      if maxReviews < numReviews:
        maxReviews = numReviews
        mostReviewed = product

    if product.starRating:
      starRating = float(product.starRating)
      if minStarRating > starRating:
        minStarRating = starRating
        lowestSR = product
      if maxStarRating < starRating:
        maxStarRating = starRating
        highestSR = product

  print(f"Cheapest product: {cheapest.name}")
  print(f"Link: {cheapest.link}\n")
  print(f"Most expensive product: {mostExpensive.name}")
  print(f"Link: {mostExpensive.link}\n")
  print(f"Least reviewed product: {leastReviewed.name}")
  print(f"Link: {leastReviewed.link}\n")
  print(f"Most reviewed product: {mostReviewed.name}")
  print(f"Link: {mostReviewed.link}\n")
  print(f"Lowest star rating product (out of 5): {lowestSR.name}")
  print(f"Link: {lowestSR.link}\n")
  print(f"Highest star rating product (out of 5): {highestSR.name}")
  print(f"Link: {highestSR.link}\n")

# Assigns each product in the list a value based on the number of reviews, price, and star rating, then returns them in sorted decreasing order
def assignRecommendationScores(products):
  N = len(products)
  # find average for numReviews, price, and starRating
  avgNumReviews, avgPrice, avgStarRating = 0, 0, 0
  for product in products:
    if product.numReviews:
      avgNumReviews += float(product.numReviews)
    if product.price:
      avgPrice += float(product.price)
    if product.starRating:
      avgStarRating += float(product.starRating)
  
  avgNumReviews /= N
  avgPrice /= N
  avgStarRating /= N
  
  # score = variance(numReviews) * 0.4 + variance(price) * 0.4 + variance(starRating) * 0.2 idk im not a statistician
  for i in range(N):
    if not products[i].numReviews or not products[i].price or not products[i].starRating:
      products[i].assignScore(float('-inf'))
      continue

    reviewScore = (float(products[i].numReviews) - avgNumReviews) / avgNumReviews
    priceScore = -1 * (float(products[i].price) - avgPrice) / avgPrice
    starRatingScore = (float(products[i].starRating) - avgStarRating) / avgStarRating

    products[i].assignScore(reviewScore * 0.4 + priceScore * 0.4 + starRatingScore * 0.2)
  
  products.sort(key = lambda product : product.score, reverse = True)
  return products