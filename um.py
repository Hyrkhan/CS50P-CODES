import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    num = 0
    list = re.findall(r"\bum\b", s, re.IGNORECASE)
    for _ in list:
        num += 1
    return int(num)

if __name__ == "__main__":
    main()
