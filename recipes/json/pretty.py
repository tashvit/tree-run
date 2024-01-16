import json
import sys


def prettify_json():
    input_data = sys.stdin.read()
    json_object = json.loads(input_data)
    pretty_json = json.dumps(json_object, indent=4)
    print(pretty_json)


if __name__ == "__main__":
    prettify_json()
