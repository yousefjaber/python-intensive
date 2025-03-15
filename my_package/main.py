import my_package
from my_package.string_utils import slice_string
from my_package.collection_utils import update_dict
from my_package.data_format_utils import convert_dict_to_json, convert_json_to_dict

def do_something_interesting():
    # Testing string slicing
    result = slice_string("Hello, world!", 0, 5)
    print(f"String slicing result: {result}")

    # Testing collection update
    test_dict = {"name": "John", "age": 30}
    updated_dict = update_dict(test_dict, "age", 31)
    print(f"Updated dictionary: {updated_dict}")

    # Testing data format conversion
    json_data = convert_dict_to_json(test_dict)
    print(f"JSON data: {json_data}")
    converted_dict = convert_json_to_dict(json_data)
    print(f"Converted back to dict: {converted_dict}")

if __name__ == "__main__":
    do_something_interesting()
