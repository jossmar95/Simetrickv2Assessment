import requests
import jsonschema
import json
from jsonschema import validate

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)
assert response.status_code == 200
data = json.loads(response.text)

schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "completed": {"type": "boolean"}
    },
    "required":  ["userId", "id", "title", "completed"]
}
jsonschema.validate(data, schema)

# Approach # 2
# def validatejson(jsonData):
#     try:
#         validate(instance=jsonData, schema=schema)
#     except jsonschema.exceptions.ValidationError as err:
#         return False
#     return True
#
#
# # Convert json to python object.
# jsonData = json.loads('{"userId": 1, "id": 1, "title": "delectus aut autem", "completed": false}')
# # validate it
# isValid = validatejson(jsonData)
# if isValid:
#     print(jsonData)
#     print("Given JSON data is Valid")
# else:
#     print(jsonData)
#     print("Given JSON data is InValid")
