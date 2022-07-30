from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from product import Product
from nav import findProperty, elementExists
from analysis import displayData

chrome_options = Options()
chrome_options.binary_location = "/Applications/Google Chrome Beta.app/Contents/MacOS/Google Chrome Beta"
s = Service('/Users/matthewlin/chromedriver')
driver = webdriver.Chrome(service=s, chrome_options=chrome_options)


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
displayData(productArr)