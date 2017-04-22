import folium

import pandas as pd
# unemployment = pd.read_csv('./US_Unemployment_Oct2012.csv')
#
# m = folium.Map([43,-100], zoom_start=4)
#
# m.choropleth(
#     geo_str=open('us-states.json').read(),
#     data=unemployment,
#     columns=['State', 'Unemployment'],
#     key_on='feature.id',
#     fill_color='YlGn',
#     )
# m.save('anyNameGoesHere.html')


    # Different code.
state_geo = r'us-states.json'
state_unemployment = r'US_Unemployment_Oct2012.csv'

state_data = pd.read_csv(state_unemployment)

#Let Folium determine the scale
map = folium.Map(location=[48, -102], zoom_start=3)
map.geo_json(geo_path=state_geo, data=state_data,
             columns=['State', 'Unemployment'],
             key_on='feature.id',
             fill_color='YlGn', fill_opacity=0.7, line_opacity=0.2,
             legend_name='Unemployment Rate (%)')
map.save('us_states.html')


# map_2 = folium.Map(location=[45.5236, -122.6750], tiles='Stamen Toner',
# zoom_start=13)
# folium.Marker(location=[45.5244, -122.6699], popup='The Waterfront').add_to(map_2)
# folium.CircleMarker(location=[45.5215, -122.6261], radius=50,
# popup='Laurelhurst Park', color='#3186cc',
# fill_color='#3186cc').add_to(map_2)
# map_2.save('portland.html')


# map_1 = folium.Map(location=[45.372, -121.6972], zoom_start=12,tiles='Stamen Terrain')
# folium.Marker([45.3288, -121.6625], popup='Mt. Hood Meadows',
# icon = folium.Icon(icon = 'cloud')).add_to(map_1)
# folium.Marker([45.3311, -121.7113], popup='Timberline Lodge',
# icon = folium.Icon(color ='green')).add_to(map_1)
# map_1.save('iconTest.html')

# map_osm = folium.Map(location=[45.5236, -122.6750])
# map_osm.save('osm.html')
#
# stamen = folium.Map(location=[45.5236, -122.6750], tiles='Stamen Toner',
# zoom_start=13)
# stamen.save('stamen_toner.html')

    # Zoom to show whole US
# map_us = folium.Map(location=[44, -100], zoom_start=4)
# map_us.save('map.html')

# map_mn = folium.Map(location=[44.97, -93.28], zoom_start=13)
    # Add a marker to geo location
# folium.Marker([44.9729, -93.2831], popup='MCTC').add_to(map_mn)
# map_mn.save('map.html')
