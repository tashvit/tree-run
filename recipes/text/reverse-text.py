import sys


def reverse_text():
    input_data = sys.stdin.read()
    reversed_text = input_data[::-1]
    print(reversed_text)


if __name__ == "__main__":
    reverse_text()
