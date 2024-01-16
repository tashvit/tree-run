import sys
import base64


def decode_base64():
    input_data = sys.stdin.read()
    decoded_data = base64.b64decode(input_data.encode()).decode()
    print(decoded_data)


if __name__ == "__main__":
    decode_base64()
