import pandas, folium, json
import os

data_link = os.path.join('files', 'quarterSoup.csv') # Path to csv file

data = pandas.read_csv(data_link) # Data frame from the csv file.

    # This example code is to relace the \r\n that a rows might have in it when print function is used.
# release_date = data['release date']
# release_date = [x.replace('\r\n', ' ') for x in release_date]
# print(release_date)

# Gets the states in alphabetic order and reset the index
group_by_state = data.groupby(by=['states']).sum().reset_index()
# print(group_by_state)
# This works with any problems.

# Path to find the file us_states_abbr.json
path_abbr_states = os.path.join('files', 'us_states_abbr.json')

# Store the json file in a variable.
states_abbr = json.load(open(path_abbr_states))

# Get the names of each states from the .json file without the values (= abbr)
state_list = list(states_abbr.keys())

# Creates a dataFrame for states_list.
all_states = pandas.DataFrame({'states': state_list})

# Appends the all_states to the csv data group_by_state
all_states_data = group_by_state.append(all_states)

# This is where the duplicates get dropped in the group_by_state dataFrame (I believe is dataFrame)
all_states_data = all_states_data.drop_duplicates('states', keep='first')

# Replace the state names withe the abbr only.
group_by_state = all_states_data.replace(states_abbr)
print(group_by_state)
