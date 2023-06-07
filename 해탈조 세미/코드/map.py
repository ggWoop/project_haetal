from google.colab import drive
import csv
import folium

drive.mount('/content/drive')

data = []

with open('/content/drive/MyDrive/dt.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) 
    for row in reader:
        lat = float(row[1])
        lon = float(row[2])
        data.append([lat, lon])

map = folium.Map(location=[37.532600, 127.024612], zoom_start=12)

for point in data:
    folium.Marker(location=point).add_to(map)

map