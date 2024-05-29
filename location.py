import geopy
from geopy.geocoders import Nominatim
import folium
import tkinter as tk
from tkinter import ttk
from tkinter import *
from io import BytesIO
from PIL import Image, ImageTk
import requests

def get_location():
    # Initialize geolocator
    geolocator = Nominatim(user_agent="geoapiExercises")
    
    # Get location based on IP address
    response = requests.get("https://ipinfo.io")
    data = response.json()
    location = data['loc'].split(',')
    latitude = float(location[0])
    longitude = float(location[1])

    # Get address
    address = geolocator.reverse(f"{latitude}, {longitude}").address

    return latitude, longitude, address

def show_map(latitude, longitude):
    # Create a folium map
    map_ = folium.Map(location=[latitude, longitude], zoom_start=15)
    folium.Marker([latitude, longitude], tooltip='Current Location').add_to(map_)
    
    # Save the map as an HTML file
    map_.save("map.html")

    # Convert the HTML file to an image
    img_data = BytesIO()
    map_.save(img_data, close_file=False)
    img_data.seek(0)
    img = Image.open(img_data)

    return img

def display_map_window():
    # Get the current location
    latitude, longitude, address = get_location()

    # Create the map
    img = show_map(latitude, longitude)
    
    # Create a Tkinter window
    root = tk.Tk()
    root.title("Current Location")

    # Convert the image to a format that Tkinter can display
    img_tk = ImageTk.PhotoImage(img)

    # Create a label to display the image
    label = tk.Label(root, image=img_tk)
    label.pack()

    # Create a label to display the address
    address_label = tk.Label(root, text=address, wraplength=400)
    address_label.pack()

    # Start the Tkinter main loop
    root.mainloop()

# Call the function to display the map window
if __name__ == "__main__":
    display_map_window()
