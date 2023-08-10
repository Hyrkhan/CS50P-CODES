import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    if matches := re.search(r"^([0-9]+):?([0-9]+)? (AM|PM) to ([0-9]+):?([0-9]+)? (AM|PM)$", s):
        if int(matches.group(1)) > 12 or int(matches.group(4)) > 12:
            raise ValueError("diz big")
        elif matches.group(2) and matches.group(5):
            if int(matches.group(2)) >= 60 or int(matches.group(5)) >= 60:
                raise ValueError("60plus")
            elif matches.group(3) == "AM":
                first = f"{int(matches.group(1)):02}:{matches.group(2)}"
                if matches.group(6) == "AM":
                    second = f"{int(matches.group(4)):02}:{matches.group(5)}"
                else:
                    second = f"{(int(matches.group(4)) + 12)}:{matches.group(5)}"
                return f"{first} to {second}"
            else:
                first = f"{(int(matches.group(1)) + 12)}:{matches.group(2)}"
                if matches.group(6) == "AM":
                    second = f"{int(matches.group(4)):02}:{matches.group(5)}"
                else:
                    second = f"{(int(matches.group(4)) + 12)}:{matches.group(5)}"
                return f"{first} to {second}"
        elif matches.group(2) == None and matches.group(5) == None:
            if matches.group(3) == "AM":
                first = f"{int(matches.group(1)):02}"
                if matches.group(6) == "AM":
                    second = f"{int(matches.group(4)):02}"
                else:
                    second = str(int(matches.group(4)) + 12)
                return f"{first}:00 to {second}:00"
            else:
                first = str(int(matches.group(1)) + 12)
                if matches.group(6) == "AM":
                    second = f"{int(matches.group(4)):02}"
                else:
                    second = str(int(matches.group(4)) + 12)
                return f"{first}:00 to {second}:00"

    else:
        raise ValueError("nope")


if __name__ == "__main__":
    main()
