
import os
from bs4_scrapping_data import Bs4Scrapping
from csv_to_sql import WriteToDB

if __name__ == "__main__":
    if not os.path.isfile('quarterSoup.csv'):
        Bs4Scrapping()
        WriteToDB()
        print('if statement')

    else:
        WriteToDB()
        print('else statement')
