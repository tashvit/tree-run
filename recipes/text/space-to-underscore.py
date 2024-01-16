import sys


def replace_spaces():
    input_data = sys.stdin.read()
    text_with_underscores = input_data.replace(" ", "_")
    print(text_with_underscores)


if __name__ == "__main__":
    replace_spaces()
