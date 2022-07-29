from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.binary_location = "/Applications/Google Chrome Beta.app/Contents/MacOS/Google Chrome Beta"

s = Service('/Users/matthewlin/chromedriver')
driver = webdriver.Chrome(service=s, chrome_options=chrome_options)

driver.get('https://www.amazon.com/s?i=fashion-mens&bbn=19289251011&rh=n%3A7141123011%2Cn%3A19289251011%2Cn%3A7147441011%2Cn%3A679255011&s=date-desc-rank&ds=v1%3A6vrtGgKZxYAVAyhzhU0Rb07V3vFrgeoHQOfDKM5F76c&pd_rd_r=53e15505-bc01-44c9-9ced-e7db1a2011fa&pd_rd_w=o8x3F&pd_rd_wg=oOmbg&pf_rd_p=2216c49b-afd0-4d36-9b66-e775a7e6c9ae&pf_rd_r=5AXK5T11050539W7BBEM&qid=1658435037&rnid=7147441011&ref=Topcard_QuadCat_AF_July_OTC_2_Shoes')

# finds all elements that match selector in given location and returns the first one, or none if there aren't any
def findProperty(loc, selector):
  prop = loc.find_elements(By.CSS_SELECTOR, selector)
  if len(prop) > 0:
    return prop[0]
  return None

try:
  # get text of posts
  products = driver.find_elements(By.CSS_SELECTOR, "div[class='a-section a-spacing-small puis-padding-left-micro puis-padding-right-micro']")
  print(f"number of products found: {len(products)}")
  for product in products:
    name = findProperty(product, "span[class='a-size-base-plus a-color-base a-text-normal']")
    if name:
      print(f"name: {name.text}")
    starRating = findProperty(product, "span[aria-label$='stars']")
    if starRating:
      print(f"star rating: {starRating.get_attribute('aria-label')}\n")
    else:
      print(f"star rating: Unavailable for this item")
    # print(f"star rating: {starRating.text}\n")
    # numReviews = product.find_element(By.CSS_SELECTOR, "span[class='a-size-base s-underline-text']")
    # price = int(product.find_element(By.CSS_SELECTOR, "span[class='a-price-whole']").text + '.' + product.find_element(By.CSS_SELECTOR, "span[class='a-price-fraction']").text)
    # prime = product.find_element(By.CSS_SELECTOR, "span[class='aok-inline-block s-image-logo-view']")
    
    
    # print(f"product name: {name}")
    # print(f"star rating: {starRating}")
    # print(f"num review: {numReviews}")
    # print(f"price: {price}")
    # print(f"prime: {prime}\n")
except:
  print("SOMETHING WENT WRONG")
  driver.quit()
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