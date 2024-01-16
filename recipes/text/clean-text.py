import sys
import re


def clean_text():
    input_data = sys.stdin.read()
    cleaned_text = re.sub(r'\W+', ' ', input_data)
    print(cleaned_text)


if __name__ == "__main__":
    clean_text()
