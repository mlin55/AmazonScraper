class Product:
  def __init__(self, name = '', company = '', starRating = '', numReviews = '', price = '', link = ''):
    self.name = name
    self.company = company
    self.starRating = starRating
    self.numReviews = numReviews
    self.price = price
    self.link = link

def printProductInfo(name, company, starRating, numReviews, price):
  if name:
    print(f"NAME: {name.text}")
  else:
    print(f"NAME: Unavailable for this item")
  if company:
    print(f"COMPANY: {company.text}")
  else:
    print(f"COMPANY: Unavailable for this item")
  if starRating:
    print(f"STAR RATING: {starRating.get_attribute('aria-label')}")
  else:
    print(f"STAR RATING: Unavailable for this item")
  if numReviews:
    print(f"NUM REVIEWS: {numReviews.text}")
  else:
    print(f"NUM REVIEWS: Unavailable for this item")
  print(f"PRICE: {price}\n")