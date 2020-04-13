# from bs4 import BeautifulSoup
# import urllib3
# import selenium
import re
# from requests import get
# response = get("https://www.flightradar24.com/data/airports/mco")
#
# soup = BeautifulSoup(response)

from selenium import webdriver
regex_search_string = "#\d\s(\w{3})\\n(\d+).*\\n"
driver = webdriver.Chrome()
for airport_code in ["MCO", "DCA", "PHL"]:
    driver.get("https://www.flightradar24.com/data/airports/"+airport_code.lower())
    elem = driver.find_element_by_class_name("top-routes")
    print(elem)
    matches = re.findall(regex_search_string, elem.text)
    for top_dest, num_flights in matches:
        print(top_dest, num_flights)
    elem.clear()

assert "No results found." not in driver.page_source
driver.close()
