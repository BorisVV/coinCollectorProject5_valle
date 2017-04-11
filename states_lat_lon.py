''' This is a beatifuSoup scrapping to get the states and their latitude and longitude.
'''

from bs4 import BeautifulSoup
import requests
import csv

url = "https://inkplant.com/code/state-latitudes-longitudes"
    # Get request
resp = requests.get(url)
    # Read in html in text mode
html_text = resp.text
    # Use beautifulSoup with hmtl parser
soup = BeautifulSoup(html_text, 'html.parser')
    # Get the table with the a specific name and all its rows and columns.
table = soup.find('table', class_='table table-hover')
# print(table)

lat_lon_list = []

    # Get each row in text mode from the table
for row in table:
    # This stores the items in the table by dividing them in sections.
    list_split = []
        # This for loop is to iterate each row and stores it in the array.
    for split in row:
        list_split.append(split.text)
    # Append each time it loops, one list_split at a time.
    lat_lon_list.append(list_split)

    # When getting the csv file I noticed that the first row (heading) doen't split or has comma separator.
    # For that reason I removed it from the list lat_lon_list.
lat_lon_list.pop(0)

    # This creates the csv file and it creates it.
with open('states_lat_lon.csv', 'w', encoding='utf-8') as latLonFile:
    writer = csv.writer(latLonFile)
        # Notice the writerows, it is used to add arrays to csv files.
    writer.writerows(lat_lon_list)
