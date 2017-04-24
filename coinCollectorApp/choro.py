import pandas, folium, json
import os

class Choro:
    data_link = os.path.join('files', 'quarterSoup.csv') # Path to csv file
    data = pandas.read_csv(data_link) # Data frame from the csv file.

            # This example code is to relace the \r\n that a rows might have in it when print function is used.
        # release_date = data['release date']
        # release_date = [x.replace('\r\n', ' ') for x in release_date]
        # print(release_date)

    # Gets the states in alphabetic order and reset the index
    group_by_state = data.groupby(by=['states']).sum().reset_index()

    # Path to find the file us_states_abbr.json
    path_abbr_states = os.path.join('files', 'us_states_abbr.json')

    # Store the json file in a variable.
    states_abbr = json.load(open(path_abbr_states))

    # Get the names of each states from the .json file without the values (= abbr)
    state_list = list(states_abbr.keys())

    # Creates a dataFrame for states_list.
    all_states = pandas.DataFrame({'states': state_list, 'quantity': 0})

    # Appends the all_states to the csv data group_by_state
    all_states_data = group_by_state.append(all_states)

    # This is where the duplicates get dropped in the group_by_state dataFrame (I believe is dataFrame)
    all_states_data = all_states_data.drop_duplicates('states', keep='first')

    # For some reason I was getting the 'number' appended to the all_states_data, the next line removes it.
    all_states_data = all_states_data.drop('number', axis=1)

    # The data from the csv shows NaN and this code changes it to 1 for each state that matches.
    all_states_data = all_states_data.fillna(value=1)


    # Add the value of one for each state in the column quantity.
    all_states_data = all_states_data.fillna(value=1)


    # Replace the state names with the abbr only.
    group_by_state = all_states_data.replace(states_abbr)

    from pathlib import Path

    # Create a choropleth map
    us_states_file = Path('files/us_states.json')

    # Display the side of the map when loads for the first time.
    choromap = folium.Map(location=[40, -120], zoom_start=3)

    # Get the us_states.json, and group_by_state to upload the data to the map.
    choromap.choropleth(
        geo_path = us_states_file,
        data = group_by_state,
            columns = ['states', 'quantity'],
        key_on = 'id',
        fill_color = 'BuPu', fill_opacity = 0.6, line_opacity = 0.4,
        # threshold_scale = [0, 50],
        legend_name = "Quaters per states"
        )
    # Save the choroMap to a file inside the directory maps.
    choromap.save('maps/choro_map.html')
