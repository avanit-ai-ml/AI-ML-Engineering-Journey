# 10. Dictionary Methods

info = {
    "Name" : "Avanit Kumar",
    "Department" : "Computer Science",
    "Age": 22,
    "Subjects": ["Datastructures & Algorithms", "Database Management System", "Computer Networks"]
}

print(info.keys()) # Returns all keys

print(info.values()) # Returns all values

print(info.items()) # Returns (key, val) pairs

print(info.get("Age")) # Returns all according to key

info.update({ # Add new items to dict
    "CGPA": 7.3
})

print(info)

info.clear() # Delete everyting from Dictionary

new_info = info.copy() # Copy the Dictionary