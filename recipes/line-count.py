import sys


def line_counter():
    input_data = sys.stdin.read()
    line_count = input_data.count('\n')
    print(line_count)


if __name__ == "__main__":
    line_counter()
