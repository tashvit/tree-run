import sys


def lower_case_text():
    input_data = sys.stdin.read()
    print(input_data.lower())


if __name__ == "__main__":
    lower_case_text()
