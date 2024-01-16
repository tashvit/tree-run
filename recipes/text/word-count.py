import sys


def count_words():
    input_data = sys.stdin.read()
    word_count = len(input_data.split())
    print(word_count)


if __name__ == "__main__":
    count_words()
