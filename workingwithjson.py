import json

class Vehicle:
    def __init__(self, no_of_tires, type) -> None:
        self.no_of_tires = no_of_tires
        self.type = type

if __name__ == "__main__":
    vehicle_1 =  Vehicle(4, "car")
    with open('app.json', 'w') as f: # serialization    
        json.dump(vehicle_1.__dict__, f)

    with open('app.json', 'r') as j: #deserialization
        json_data = json.load(j)
        print(json_data)


