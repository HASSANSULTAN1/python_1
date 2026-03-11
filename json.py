import json

x = {
  "name": "Hassan",
  "age": 22,
  "city": "Lahore"
}

y = json.loads(x)
print(y["age"])
