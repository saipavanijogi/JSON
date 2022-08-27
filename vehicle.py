# Convert the following Vehicle Object into JSON
# import json

# class Vehicle:
#     def _init_(self, name, engine, price):
#         self.name = name
#         self.engine = engine
#         self.price = price

# vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
import json
from json import JSONEncoder

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

class VehicleEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

v= Vehicle("Toyota Rav4", "2.5L", 32000)

print("Encode Vehicle Object into JSON")
vehicleJson = json.dumps(v, indent=4, cls=VehicleEncoder)
print(vehicleJson)


# Convert it into JSON format
# Expected Output:

# {
#     "name": "Toyota Rav4",
#     "engine": "2.5L",
#     "price": 32000
# }