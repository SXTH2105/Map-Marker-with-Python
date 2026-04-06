# 🗺️ Map Marker with Python

A command-line Python application that lets you drop a marker on an interactive map using either coordinates or a location name — powered by Folium and OpenStreetMap.

---

## 📋 Overview

This project allows users to search for any location in the world by name or by coordinates, place a red marker on an interactive map, save it as an HTML file, and automatically open it in the browser. It uses the Nominatim geocoding API to resolve location names into latitude and longitude.

---

## ✨ Features

- 🔍 Search by **location name** — automatically geocodes using OpenStreetMap's Nominatim API
- 📍 Drop markers using **manual coordinates** (latitude & longitude)
- 🗺️ Generates a fully **interactive map** with zoom and pan support
- 💾 Saves each map as a named **HTML file** in a `Saved Map/` folder
- 🌐 **Auto-opens** the map in your default browser after saving
- 🔁 Supports **multiple markers** in one session (loop-based)
- 🚪 Type `exit` anytime to quit

---

## 🛠️ Tech Stack

- **Python 3**
- **Folium** — for generating interactive Leaflet.js maps
- **Nominatim (OpenStreetMap)** — for geocoding location names to coordinates
- **webbrowser** — for auto-opening the generated map
- **os / json / urllib** — standard library utilities

---

## 🚀 Getting Started

### Prerequisites

Install the required third-party library:

```bash
pip install folium
```

### Installation

1. Clone the repository:

```bash
git clone https://github.com/SXTH2105/Map-Marker-with-Python.git
cd Map-Marker-with-Python
```

2. Run the script:

```bash
python map_marker.py
```

---

## 📖 How It Works

1. The app asks whether you know the coordinates of your location.
2. **If yes** — enter the latitude, longitude, and a name for the marker.
3. **If no** — enter a place name and the app automatically fetches its coordinates via the Nominatim API.
4. A red marker is placed on an interactive Folium map centered on the location.
5. The map is saved as an `.html` file inside the `Saved Map/` folder, named after the location.
6. The map automatically opens in your default web browser.
7. The loop continues, allowing you to mark multiple locations in one session.

---

## 🗂️ Output Example

```
Saved Map/
├── Phnom_Penh.html
├── Eiffel_Tower.html
└── Tokyo.html
```

Each file is a self-contained interactive map that can be shared or opened offline.

---

## 📁 Project Structure

```
Map-Marker-with-Python/
│
└── map_marker.py    # Main application file
```

---

## ⚠️ Notes

- Geocoding relies on the **Nominatim API**, which requires an internet connection and may return no results for very obscure or misspelled locations.
- The Nominatim API has a usage policy — this app sets a proper `User-Agent` header to comply with it.

---

## 🔮 Future Improvements

- Add support for multiple markers on a single map
- Allow custom marker colors and icons
- Add a simple GUI for input instead of the command line
- Export maps as image files (PNG/JPEG)
- Save a history of all marked locations

---

## 👤 Author

**Seth**
- GitHub: [@SXTH2105](https://github.com/SXTH2105)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
