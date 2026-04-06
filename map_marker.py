import folium

m = folium.Map(location=[10.8231, 106.6297], zoom_start=13)

folium.Marker([10.8231, 106.6297], popup="Ho Chi Minh City", tooltip="Capital of Vietnam", icon=folium.Icon(color="red", icon="info-sign")).add_to(m)

m.save("map.html")
print("Map saved to map.html")