#creating a dictionary

dict_1 = {
  "brand": "APPLE",
  "model": "Macbook pro",
  "year": 2020
}
print(dict_1)

#accesing itmes through key

print(dict_1["model"])

#print length of dict

print(len(dict_1))

#changing items in dict

dict_1["model"]="macbook air"

print(dict_1)

#nested dictionaries

Cars = {
    "car1" : {
        "name":"yaris",
        "model":2020
    },
    "car2": {
    "name" : "city",
    "model" : 2022
    },

    "car3" : {
        "name" : "glory",
        "model" : 2024
    }
        }

print(Cars)

print(Cars ["car2"]["name"])
print(type(dict_1))