from bs4 import BeautifulSoup
import urllib3
import selenium

# from requests import get
# response = get("https://www.flightradar24.com/data/airports/mco")
#
# soup = BeautifulSoup(response)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
regex_search_string = "#\d\s(\w{3})\\n(\d+).*\\n"
driver = webdriver.Chrome()
driver.get("https://www.flightradar24.com/data/airports/mco")
elem = driver.find_element_by_class_name("top-routes")
print(elem)
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
