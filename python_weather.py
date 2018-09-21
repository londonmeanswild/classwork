#
# (c) Landon Marchant 2017
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser

# Requests google headlines

import requests
import urllib2
from bs4 import BeautifulSoup

# Retrieve URL
URL = 'http://web.williams.edu/weather/'
page = urllib2.urlopen(URL)
weather = page.read(page) #.read
# parse url through 'lxml.parse' per BS Documentation
source = BeautifulSoup(weather, 'html.parser') #(headlines, "lxml")
#print(source)
the_table = source.table
data_row = []
header_row = []
for row in the_table.find_all('tr'):
    for header in row.find_all('th'):
        header_row.append(header.text)
# print(header_row)

"""
    # this parses the header row text
temp_unit_indicator = (header_row[0].split('('[0]))
average_wind_text = (header_row[2].split('/')[0])
wind_direction_text = (header_row[2].split('/')[1])
average_wind = average_wind_text + wind_direction_text
humidity_header = (header_row[5])
"""

for row in the_table.find_all('tr'):
    for data in row.find_all('td'):
       data_row.append(data.text)

# this parses the data row

fahrenheit = float(data_row[0].split(',')[1])
average_wind_speed = (data_row[2].split('/')[0])
wind_direction = (data_row[2].split('/')[1])
average_wind_int = (average_wind_speed, wind_direction)
relative_humidity = float(data_row[5])

print("The current temperature is {0} degrees Fahreheit.".format(fahrenheit))
print("The average wind speed (mph) and direction is {}".format(average_wind_speed + '/' + wind_direction))
print("The relative humidity is {} percent.".format(relative_humidity))


