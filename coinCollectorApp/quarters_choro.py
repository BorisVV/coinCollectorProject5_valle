import folium, json, sqlite3
import pandas as pd
import os
from pathlib import Path

class QuartersChoro:
    ''' Read data from the db and get columns that are needed for the pandas data
        frame. Read data from the .json file with states and load the abbr (example: AL)
        and replace the state's full namme.
    '''
    # Create a path to find the link to the db(data base).
    dataBase_path = os.path.join('coinSite', 'db.sqlite3')
    # Create a connection to the db.
    conn = sqlite3.connect(dataBase_path)

    df = pd.read_sql_query('''SELECT state from coins_web_app_displayquarters;''', conn)
        # After the table-name ...ters limit 5; to limit a display of 5 rows only
    #print(df)


                # If data needs to be taken from a .csv file.
            # data_link = os.path.join('files', 'quarterSoup.csv') # Path to csv file
            # data = pd.read_csv(data_link) # Data frame from the csv file.

                # This example code is to relace the \r\n that a rows might have in it when print function is used.
            # release_date = data['release date']
            # release_date = [x.replace('\r\n', ' ') for x in release_date]
            # print(release_date)

    # Gets the states in alphabetic order and reset the index
    group_by_state = df.groupby(by=['state']).sum().reset_index()

    # Path to find the file us_states_abbr.json
    path_abbr_states = os.path.join('files', 'us_states_abbr.json')

    # Store the json file in a variable.
    states_abbr = json.load(open(path_abbr_states))

    # Get the names of each states from the .json file without the values (= abbr)
    state_list = list(states_abbr.keys())

    # Creates a dataFrame for states_list.
    all_states = pd.DataFrame({'state': state_list, 'quantity': 0})

    # Appends the all_states to the csv data group_by_state
    all_states_data = group_by_state.append(all_states)

    # This is where the duplicates get dropped in the group_by_state dataFrame (I believe is dataFrame)
    all_states_data = all_states_data.drop_duplicates('state', keep='first')

    # If using .csv use this line of code.
    # For some reason I was getting the 'number' appended to the all_states_data, the next line removes it.
    # all_states_data = all_states_data.drop('number', axis=1)

    # The dataBase states will have NaN in the quantity column, this is because it is a new column.
    # Add the value of one for each state in the column quantity.
    all_states_data = all_states_data.fillna(value=1)

    # Replace the state names with the abbr only.
    group_by_state = all_states_data.replace(states_abbr)

    # Create a choropleth map
    us_states_file = Path('files/us_states.json')

    # Display the side of the map when loads for the first time.
    choromap = folium.Map(location=[40, -120], zoom_start=3)

    # Get the us_states.json, and group_by_state to upload the data to the map.
    choromap.choropleth(
        geo_path = us_states_file,
        # This columns are from the pandas data frame.
        data = group_by_state,
            columns = ['state', 'quantity'],
        key_on = 'id',
        fill_color = 'BuPu', fill_opacity = 0.6, line_opacity = 0.4,
        # threshold_scale = [0, 50],
        legend_name = "States with quarters"
        )
    # Save the choroMap to a file inside the directory maps.
    choromap.save('maps/quarters_map.html')
