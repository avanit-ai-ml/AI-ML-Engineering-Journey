# 10. Working with JSON module

import json
'''
js_string = '{"role": "AI ML Engineer", "isWorking": true}'

py_obj = json.loads(js_string) # json string to python object

print(type(py_obj))

print(py_obj)
'''

'''
py_objj = {
    "Name" : "Avanit Kumar",
    "is_working" : True,
    "Subject" : ["Python", "AI & ML", "Web Development"]
}

print(type(py_objj))

js_stringg = json.dumps(py_objj) # python object to json string

print(type(js_stringg))

print(js_stringg)
'''

with open("data.json", "r") as f:
    py_obj = json.load(f) # Read from JSON file
    print(type(py_obj))

d = {
    "name": "Avanit Kumar",
    "sub": ["Python", "OOPs", "DSA"],
    "role": "AI ML Engineer",
    "isWorking": True,
    "address": {
        "city": "Jaipur",
        "State": "Rajasthan"
  }
}

with open("data.json", "w") as f:
    json.dump(d, f, indent=4, sort_keys=True) # Write in JSON file
