from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.binary_location = "/Applications/Google Chrome Beta.app/Contents/MacOS/Google Chrome Beta"

s = Service('/Users/matthewlin/chromedriver')
driver = webdriver.Chrome(service=s, chrome_options=chrome_options)

class Product:
  def __init__(self, name = '', company = '', starRating = '', numReviews = '', price = '', link = ''):
    self.name = name
    self.company = company
    self.starRating = starRating
    self.numReviews = numReviews
    self.price = price
    self.link = link

# finds all elements that match selector in given location and returns the first one, or none if there aren't any
def findProperty(loc, selector):
  prop = loc.find_elements(By.CSS_SELECTOR, selector)
  if len(prop) > 0:
    return prop[0]
  return None

def elementExists(loc, selector):
  try:
    WebDriverWait(loc, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
    return True
  except TimeoutException:
    return False

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


# go to product results page
PRODUCT_NAME = "Swiffers Sweepers"
MAX_PAGE_COUNT = 10
driver.get('https://www.amazon.com')
searchBar = findProperty(driver, "input[id='twotabsearchtextbox']")
searchBar.send_keys(PRODUCT_NAME)
searchBar.send_keys(Keys.RETURN)

productArr = []
nextPage = 'placeholder'
pageCount = 0
while pageCount < MAX_PAGE_COUNT and nextPage:
  # find next page button
  if elementExists(driver, "a[aria-label^='Go to next page']"):
    nextPage = findProperty(driver, "a[aria-label^='Go to next page']")
  else:
    nextPage = None

  # get product info
  products = driver.find_elements(By.CSS_SELECTOR, "div[class='s-card-container s-overflow-hidden aok-relative puis-expand-height puis-include-content-margin s-latency-cf-section s-card-border']")
  for product in products:
    name = findProperty(product, "span[class='a-size-base-plus a-color-base a-text-normal']")
    company = findProperty(product, "span[class='a-size-base-plus a-color-base']")
    starRating = findProperty(product, "span[aria-label$='stars']")
    numReviews = findProperty(product, "span[class='a-size-base s-underline-text']")
    priceWhole = findProperty(product, "span[class='a-price-whole']")
    priceFrac = findProperty(product, "span[class='a-price-fraction']")
    link = findProperty(product, "a[class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")
    price = ''
    if priceWhole and priceWhole.text != '':
      price += priceWhole.text
    else:
      price += '0'
    price += '.'
    if priceFrac  and priceFrac.text != '':
      price += priceFrac.text
    else:
      price += '00'

    # printProductInfo(name, company, starRating, numReviews, price)
    productArr.append(Product(
      name.text if name else None,
      company.text if company else None,
      starRating.get_attribute('aria-label').split(' ')[0] if starRating else None,
      # filter out all non-numeric characters
      ''.join(filter(str.isalnum, numReviews.text)) if numReviews else None,
      price if price else None,
      link.get_attribute('href') if link else None,
    ))

  # navigate to next page
  if nextPage:
    nextPage.click()
    pageCount += 1

driver.quit()

# analyze product data
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


"""
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Beginner Python Tutorials'))
    )
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'sow-button-19310003'))
    )
    element.click()

    driver.back()
except:
    driver.quit()
"""