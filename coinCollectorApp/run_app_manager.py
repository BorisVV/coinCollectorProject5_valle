
import os
from bs4_scrapping_data import Bs4Scrapping
from csv_to_sql import WriteToDB

if __name__ == "__main__":

    ''' This file is to run the app and upload the information that is needed in
    the database'''
        # First will check to see if the file exist, if it dosn't it will create one,
        #   then it will read the file and store the data in the table that is in the db.
        # Else the WriteToDB class will store the data in the table.
        # Either way, the program will load the data to the db only once.
    if not os.path.isfile('quarterSoup.csv'):
        Bs4Scrapping() # from bs4_scrapping_data.py
        WriteToDB() # from csv_sql.py
        print('Data saved to the table in the db!')

    else:
        WriteToDB() # from csv_sql.py
        print('Data saved to the table in the db!')
