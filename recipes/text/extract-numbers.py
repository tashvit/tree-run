import sys
import re


def extract_numbers():
    input_data = sys.stdin.read()
    numbers = re.findall(r'\d+', input_data)
    print(numbers)


if __name__ == "__main__":
    extract_numbers()
