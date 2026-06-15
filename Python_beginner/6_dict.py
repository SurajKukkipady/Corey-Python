student = {
    "name": "John",
    "age": 25,
    "courses": ["Math", "CompSci"]}

print(student)
print(student["name"])
print(student.get("name"))
print(student.get("phone"))
print(student.get("phone", "Not Found"))