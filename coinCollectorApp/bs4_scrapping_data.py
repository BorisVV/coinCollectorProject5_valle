from bs4 import BeautifulSoup
import requests
import csv

url = "https://en.wikipedia.org/wiki/50_State_Quarters"
resp = requests.get(url)
html = resp.text
soup = BeautifulSoup(html,'html.parser')
# This fetches the table that contains the quarters only
table = soup.find('table', {'class': 'wikitable sortable' })
# This list store the list of list from list_of_cellls.
list_of_rows=[]
# This for loop is used to find the tr then loop in the items that are in the tr
for row in table.find_all('tr')[1:]:
    list_of_cells=[] # Used in the next loop
    # This loop gets the text of each column
    img_link_str = ""
    for cell in row.find_all('td'):
        # This appends the text only of the loop
        list_of_cells.append(cell.text)

        # This loop is to get the link and image for the each quarter as html
        img_link = cell.find_all('a', class_ = 'image')
        for link in img_link:
            # This global variable stores the link as string
            img_link_str = (str(link))

        # if stament, some of the rows have eight and others 7 columns and this makes sure that
        #they match by removing the first column on the ones that have eight columns
        if len(list_of_cells) == 8:
            del list_of_cells[0]
            # Deletes the first column

    # Store the imaga link to list_of_cells
    list_of_cells.append(str(img_link_str))

    # Once all the rows are equal to seven then remove the columns 4 (numbers that are not used)
    # and 5 (empty column) because of the link not being a text.
    del list_of_cells[3:5]

    # This appends the list_of_cells to list_of_rows which is used to write to csv file.
    list_of_rows.append(list_of_cells)

    # Open the file and use encoding to format and write to file with the header in the write.row
with open('quarterSoup.csv','w', encoding='utf-8') as outfile:
    writer=csv.writer(outfile)
    writer.writerow(['Number', 'State', 'Release date', 'Elements', 'Engraver', 'Link'])
    writer.writerows(list_of_rows)
