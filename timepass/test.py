
import json

person_dict = {'name': 'Bob',
'age': 12,
'children': None
}
print(person_dict)
person_json = json.dumps(person_dict)

# Output: {"name": "Bob", "age": 12, "children": null}
print(person_json)
