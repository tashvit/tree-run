import sys


def remove_duplicates():
    input_data = sys.stdin.read()
    words = input_data.split()
    words_without_duplicates = " ".join(sorted(set(words), key=words.index))
    print(words_without_duplicates)


if __name__ == "__main__":
    remove_duplicates()
