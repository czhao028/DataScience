
import re
from collections import defaultdict
import pandas as pd
import pickle as pk

countyname_to_node = {}
with open("airports_geocoded.pk", "rb") as pik:
    airportcode_to_county = pk.load(pik)
#populate it with data from CSV, filtered for data from website

class Node:
    def __init__(self, county_name):
        self.county_name = county_name
        self.connections = defaultdict(int)
    def add_connection(self, airport_flights):
        assert type(airport_flights) == tuple
        connection, number_flights = airport_flights
        number_flights = int(number_flights)
        connection_county = airportcode_to_county[connection] #possible error here
        print(connection_county)
        try: # if Node is already assigned to county
            node_connection = countyname_to_node[connection_county]
        except: # if Node not already created
            node_connection = Node(connection_county)
            countyname_to_node[connection_county] = node_connection

        node_connection.increase_connection(self.county_name, number_flights)
        self.increase_connection(connection_county, number_flights)

    def get_connection(self, county_name):
        #returns number of flights between self & county_name
        return self.connections[county_name]

    def increase_connection(self, county_name, num_additional_flights):
        #determines maximum number of flights between self Node & other county
        self.connections[county_name] = max(self.connections[county_name], num_additional_flights)


from selenium import webdriver
regex_search_string = "#\d\s(\w{3})\\n(\d+).*?"
driver = webdriver.Chrome()
for airport_code, county in [("CWA","Marathon County, WI"), ("DCA", "Arlington County, VA"), ("MCO", "Orange County, FL"), ("PHL", "Philadelphia County, PA")]:
    driver.get("https://www.flightradar24.com/data/airports/"+airport_code.lower())
    elem = driver.find_element_by_class_name("top-routes")
    temp_node = countyname_to_node.get(county)
    if temp_node is None:
        temp_node = Node(county)
        countyname_to_node[county] = temp_node
    matches = re.findall(regex_search_string, elem.text)
    for airport_flights in matches:
        temp_node.add_connection(airport_flights)

countyname_to_node
assert "No results found." not in driver.page_source
driver.close()
