employee = {"name": "hari","age": 26,"gender": "male"}
print(employee["age"])

employee["experience"] = "2 years"
print(employee)

del employee["gender"]
print(employee)

print("gender" in employee)
#print("hari" in employee.values)


for key, value in employee.items():
    print(key,value)

print(employee.items())
print(employee.values())
print(employee.keys())


print(employee.get("city", "Sorry, Not found"))