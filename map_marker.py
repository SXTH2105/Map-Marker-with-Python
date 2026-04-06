import folium
import os
import sys
import webbrowser

try:
    lat = float(input("Enter latitude: "))
    lon = float(input("Enter longitude: "))
    location_name = input("Enter location name: ")
except ValueError:
    print("Invalid coordinates. Please enter numerical values.")
    sys.exit(1)

m = folium.Map(location=[lat, lon], zoom_start=13)

folium.Marker([lat, lon], popup=location_name, tooltip=location_name, icon=folium.Icon(color="red", icon="info-sign")).add_to(m)

output_dir = "Saved Map"
os.makedirs(output_dir, exist_ok=True)

# create filename from the location name
safe_filename = "".join([c for c in location_name if c.isalpha() or c.isdigit() or c==' ']).rstrip()
filename = f"{safe_filename.replace(' ', '_')}.html" if safe_filename else "map.html"
filepath = os.path.join(output_dir, filename)

m.save(filepath)
print(f"Map saved to {filepath}")

# Automatically open the generated file in the default web browser
absolute_filepath = os.path.abspath(filepath)
webbrowser.open('file://' + absolute_filepath)