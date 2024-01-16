import sys
import json


def clean_and_format_json():
    input_data = sys.stdin.read()

    # Attempt 1: Single quotes to double quotes
    json_attempt_1 = input_data.replace("'", "\"")

    # Attempt 2: Remove additional escape characters
    json_attempt_2 = json_attempt_1.replace("\\", "")

    # Attempt 3: Find and extract valid JSON substring
    json_start = json_attempt_2.find('{')
    json_end = json_attempt_2.rfind('}')
    valid_json = json_attempt_2[json_start:json_end + 1]

    try:
        # Attempt to load the valid JSON
        json_data = json.loads(valid_json)
        formatted_json = json.dumps(json_data, indent=2)
        print(formatted_json)
    except json.JSONDecodeError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    clean_and_format_json()
