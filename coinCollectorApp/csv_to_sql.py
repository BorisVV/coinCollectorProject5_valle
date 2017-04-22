'''Open CSV file
Open sqlite database
for every line in CSV file, write a row to database
Table name: coins_web_app_displayquaters
Column names: same as variable names in model
Generate id, or is the table set up to autoincrement?
'''
import csv
import sqlite3
import os
class WriteToDB:

    conn = sqlite3.connect('coinSite\db.sqlite3')
    c = conn.cursor()

    with open('quarterSoup.csv', 'r') as f:
        reader = csv.reader(f)

        # This line of code is to make sure that list in the csv file doesn't contain empty
        # nested list or they'll get removed
        clean_reader = [x for x in reader if x != []]

            # This for loop, is necesary to get each item from each row.
            # Optional, the variable stores the data a list you can select which item you want.
        to_db = [(i[0], i[1], i[2], i[3], i[4], i[5]) for i in clean_reader]

            # Insert a row of data
        c.executemany('''INSERT INTO coins_web_app_displayquaters(number, state, release_date, elements, engraver, link) VALUES (?,?,?,?,?,?)''', to_db)
            # Save (commit) the changes
        conn.commit()

            # We can also close the connection if we are done with it.
            # Just be sure any changes have been committed or they will be lost.
        conn.close()