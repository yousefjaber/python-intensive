import json

def convert_dict_to_json(input_dict: dict) -> str:
 
    return json.dumps(input_dict)

def convert_json_to_dict(input_json: str) -> dict:
 
    return json.loads(input_json)
