import sys
import csv
import json


def csv_to_json():
    input_data = sys.stdin.read()
    csv_reader = csv.DictReader(input_data.splitlines())
    json_data = json.dumps(list(csv_reader), indent=2)
    print(json_data)


if __name__ == "__main__":
    csv_to_json()
