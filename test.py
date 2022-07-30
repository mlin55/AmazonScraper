from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.binary_location = "/Applications/Google Chrome Beta.app/Contents/MacOS/Google Chrome Beta"

s = Service('/Users/matthewlin/chromedriver')
driver = webdriver.Chrome(service=s, chrome_options=chrome_options)

driver.get('https://www.amazon.com/s?i=fashion-mens&bbn=19289251011&rh=n%3A7141123011%2Cn%3A19289251011%2Cn%3A7147441011%2Cn%3A679255011&s=date-desc-rank&ds=v1%3A6vrtGgKZxYAVAyhzhU0Rb07V3vFrgeoHQOfDKM5F76c&pd_rd_r=53e15505-bc01-44c9-9ced-e7db1a2011fa&pd_rd_w=o8x3F&pd_rd_wg=oOmbg&pf_rd_p=2216c49b-afd0-4d36-9b66-e775a7e6c9ae&pf_rd_r=5AXK5T11050539W7BBEM&qid=1658435037&rnid=7147441011&ref=Topcard_QuadCat_AF_July_OTC_2_Shoes')

class Product:
  def __init__(self, name = '', company = '', starRating = '', numReviews = '', price = ''):
    self.name = name
    self.company = company
    self.starRating = starRating
    self.numReviews = numReviews
    self.price = price

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

productArr = []
nextPage = 'placeholder'
while nextPage:
  # find next page button
  if elementExists(driver, "a[aria-label^='Go to next page']"):
    nextPage = findProperty(driver, "a[aria-label^='Go to next page']")
  else:
    nextPage = None

  # get product info
  products = driver.find_elements(By.CSS_SELECTOR, "div[class='a-section a-spacing-small puis-padding-left-micro puis-padding-right-micro']")
  for product in products:
    name = findProperty(product, "span[class='a-size-base-plus a-color-base a-text-normal']")
    company = findProperty(product, "span[class='a-size-base-plus a-color-base']")
    starRating = findProperty(product, "span[aria-label$='stars']")
    numReviews = findProperty(product, "span[class='a-size-base s-underline-text']")
    priceWhole = findProperty(product, "span[class='a-price-whole']")
    priceFrac = findProperty(product, "span[class='a-price-fraction']")
    price = ''
    if priceWhole:
      price += priceWhole.text
    else:
      price += '0'
    price += '.'
    if priceFrac:
      price += priceFrac.text
    else:
      price += '00'

    # printProductInfo(name, company, starRating, numReviews, price)
    productArr.append(Product(
      name.text if name else None,
      company.text if name else None, 
      starRating.get_attribute('aria-label').split(' ')[0] if starRating else None,
      numReviews.text if numReviews else None,
      price if price else None
    ))

  # navigate to next page
  if nextPage:
    nextPage.click()

driver.quit()

# analyze product data
minPrice, maxPrice, minReviews, maxReviews, minStarRating, maxStarRating = float('inf'), float('-inf'), float('inf'), float('-inf'), float('inf'), float('-inf')
cheapest, mostExpensive, leastReviewed, mostReviewed, lowestSR, highestSR = Product(), Product(), Product(), Product(), Product(), Product()
print(f"Total products found: {len(productArr)}")

for product in productArr:
  price = float(product.price)
  # if price == 0 then the price was not recorded, so we don't want to include it
  if minPrice > price and price != 0:
    minPrice = price
    cheapest = product
print(f"Cheapest product: {cheapest.name}")
print(cheapest)


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