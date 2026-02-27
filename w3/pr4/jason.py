import json


import json
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])

# Example: Convert from Python to JSON:
import json
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x)
print(y)

# Example: Convert Python objects into JSON strings, and print the values:
import json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:
# Python (dict) -> JSON (Object)
# Python (list/tuple) -> JSON (Array)
# Python (str) -> JSON (String)
# Python (int/float) -> JSON (Number)
# Python (True) -> JSON (true)
# Python (False) -> JSON (false)
# Python (None) -> JSON (null)

# Example: Convert a Python object containing all the legal data types:
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))

# Using the indent parameter to define the numbers of indents:
json.dumps(x, indent=4)

# Using the separators parameter to change the default separator . , =
json.dumps(x, indent=4, separators=(". ", " = "))

# Order the Result
#sorted alphabetically:
json.dumps(x, indent=4, sort_keys=True)