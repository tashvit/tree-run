import sys


def title_case_text():
    input_data = sys.stdin.read()
    title_case_text = input_data.title()
    print(title_case_text)


if __name__ == "__main__":
    title_case_text()
