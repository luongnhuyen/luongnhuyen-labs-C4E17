person = {
"name": "Quan",
"age": 22,
"gender": "undefined",
"address": "Ha Noi",
"login_count":7
}

print(person.keys())
if "name" in person.keys():
    print("Found")

print(person.values())
if "Quan" in person.values():
    print("Found")
