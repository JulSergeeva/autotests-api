from attr.validators import min_len
from jsonschema import validate
from jsonschema.exceptions import ValidationError

schema = {
  "type": "object",
  "properties": {
    "username": {"type": "string", "minLength": 5, "maxLength": 15}
  },
  "required": ["username"]
}
data = {
    'name': 'Alice',
    'age': 30
}

try:
    validate(instance=data, schema=schema)
except ValidationError as e:
    print("Ошибка")


