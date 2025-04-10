import json


person = {
    "name": "riyaz",
    "age": 23,
    "email": "riyaz23@email.com"
}


with open("person.json", "w") as file:
    json.dump(person, file, indent=4)


with open("person.json", "r") as file:
    data = json.load(file)
    print(data)
