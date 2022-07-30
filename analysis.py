from product import Product

def displayData(productArr):
  minPrice, maxPrice, minReviews, maxReviews, minStarRating, maxStarRating = float('inf'), float('-inf'), float('inf'), float('-inf'), float('inf'), float('-inf')
  cheapest, mostExpensive, leastReviewed, mostReviewed, lowestSR, highestSR = Product(), Product(), Product(), Product(), Product(), Product()
  print(f"Total products found: {len(productArr)}")

  for product in productArr:
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