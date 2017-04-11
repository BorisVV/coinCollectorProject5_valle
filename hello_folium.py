import folium

    # Center map
map_us = folium.Map(location=[32.806671, -86.791130])
map_us.save('map.html')


    # Zoom to show whole US
# map_us = folium.Map(location=[44, -100], zoom_start=4)
# map_us.save('map.html')

# map_mn = folium.Map(location=[44.97, -93.28], zoom_start=13)
    # Add a marker to geo location
# folium.Marker([44.9729, -93.2831], popup='MCTC').add_to(map_mn)
# map_mn.save('map.html')
