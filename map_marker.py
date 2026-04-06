import folium
import os
import sys
import webbrowser
import urllib.request
import urllib.parse
import json

while True:
    print("\n--- New Map Marker ---")
    choice = input("Do you know the coordinates of the place? (y/n) or type 'exit' to quit: ").strip().lower()
    
    if choice == 'exit':
        print("Exiting...")
        break

    if choice == 'y':
        try:
            lat = float(input("Enter latitude: "))
            lon = float(input("Enter longitude: "))
            location_name = input("Enter location name: ")
        except ValueError:
            print("Invalid coordinates. Please enter numerical values.")
            continue
    else:
        location_name = input("Enter location name to search: ")
        if location_name.lower().strip() == 'exit':
            print("Exiting...")
            break
            
        print(f"Searching coordinates for '{location_name}'...")
        
        url = f"https://nominatim.openstreetmap.org/search?q={urllib.parse.quote(location_name)}&format=json&limit=1"
        req = urllib.request.Request(url, headers={'User-Agent': 'MapMarkerPythonApp/1.0'})
        
        try:
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
                if data:
                    lat = float(data[0]['lat'])
                    lon = float(data[0]['lon'])
                    print(f"Found coordinates: Latitude {lat}, Longitude {lon}")
                else:
                    print("Could not find coordinates for that location.")
                    continue
        except Exception as e:
            print(f"Error fetching coordinates: {e}")
            continue

    m = folium.Map(location=[lat, lon], zoom_start=13)

    popup_text = f"<b>{location_name}</b><br>Lat: {lat:.6f}<br>Lon: {lon:.6f}"
    folium.Marker([lat, lon], popup=popup_text, tooltip=location_name, icon=folium.Icon(color="red", icon="info-sign")).add_to(m)

    output_dir = "Saved Map"
    os.makedirs(output_dir, exist_ok=True)

    # create filename from the location name
    safe_filename = "".join([c for c in location_name if c.isalpha() or c.isdigit() or c==' ']).rstrip()
    filename = f"{safe_filename.replace(' ', '_')}.html" if safe_filename else "map.html"
    filepath = os.path.join(output_dir, filename)

    m.save(filepath)
    print(f"Map saved to {filepath}")

    # auto open generated map
    absolute_filepath = os.path.abspath(filepath)
    webbrowser.open('file://' + absolute_filepath)