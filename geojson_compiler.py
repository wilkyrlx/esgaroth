import geojson

class GeojsonCompiler:

   def __init__(self, target_file):
      self.path = "output\\" + target_file + ".geojson"

   def add_polygon(self, new_data):
      with open(self.path, 'r+') as f:
         file_data = geojson.load(f)

      file_data['features'].append(new_data)   

      with open(self.path, 'w') as f:
         geojson.dump(file_data, f)
   
   

test_comp = GeojsonCompiler('myfile') 
point = geojson.Point((12, 37.24))
x = geojson.Feature(geometry=point, properties={"country": "Spain"})
test_comp.add_polygon(x)



