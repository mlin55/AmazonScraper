from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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