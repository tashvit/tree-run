import sys
import subprocess


def execute_python_code():
    python_code = sys.stdin.read()
    with open("temp.py", "w") as file:
        file.write(python_code)
    process = subprocess.Popen([sys.executable, "-u", "temp.py"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                               universal_newlines=True, encoding="utf-8")
    stdout, _ = process.communicate()
    print(stdout)


if __name__ == "__main__":
    execute_python_code()
