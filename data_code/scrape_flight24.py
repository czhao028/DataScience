
import re
from collections import defaultdict

countyname_to_node = {}
airportcode_to_county = {}

class Node:
    def __init__(self, county_name):
        self.county_name = county_name
        self.connections = defaultdict(int)
    def add_connection(self, airport_flights):
        assert type(airport_flights) == tuple
        connection, number_flights = airport_flights
        connection_county = airportcode_to_county[connection] #possible error here
        print(connection_county)
        try:
            node_connection = countyname_to_node[connection_county]
        except:
            node_connection = Node(connection_county)
            countyname_to_node[connection_county] = node_connection

        existing_edge = node_connection.get_connection(self.county_name)
        if existing_edge > number_flights:
            self.connections[connection] = existing_edge
        else:
            self.connections[connection] = number_flights

    def get_connection(self, county_name):
        #returns number of flights between self & county_name
        return self.connections[county_name]

    def set_connection(self, county_name):
        #sets the max number of flights between one county & another


from selenium import webdriver
regex_search_string = "#\d\s(\w{3})\\n(\d+).*\\n"
driver = webdriver.Chrome()
for airport_code, county in [("MCO", "Orange County, FL"), ("DCA", "Arlington County, VA"), ("PHL", "Philadelphia County, PA")]:
    driver.get("https://www.flightradar24.com/data/airports/"+airport_code.lower())
    elem = driver.find_element_by_class_name("top-routes")
    print(elem)
    matches = re.findall(regex_search_string, elem.text)
    for top_dest, num_flights in matches:
        print(top_dest, num_flights)
    elem.clear()

assert "No results found." not in driver.page_source
driver.close()
