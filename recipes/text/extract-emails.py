import sys
import re


def extract_emails():
    input_data = sys.stdin.read()
    emails = re.findall(r'\S+@\S+', input_data)
    print(emails)


if __name__ == "__main__":
    extract_emails()
