import sys
import base64


def encode_base64():
    input_data = sys.stdin.read()
    encoded_data = base64.b64encode(input_data.encode()).decode()
    print(encoded_data)


if __name__ == "__main__":
    encode_base64()
