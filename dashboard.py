import folium
import os

mapObj = folium.Map(prefer_canvas=True)

folium.GeoJson("geojson-data\\Squam_Test.geojson", name="Squam Lake").add_to(mapObj)
folium.GeoJson("geojson-data\\China_Lakes.geojson", name="China").add_to(mapObj)

mapObj.save('html-output\\output.html')
