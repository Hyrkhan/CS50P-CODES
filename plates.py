def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length = len(s)-1

    for letters in s:
        if letters.isdigit():
            if letters == "0":
                return False
            else:
                break

    for letter in s:
        if not letter.isalpha() and not letter.isdigit():
            return False

    if s[:2].isdigit():
        return False
    elif length < 2 or length > 6:
        return False
    elif s[length-1:length].isalpha():
        return False
    else:
        return True

main()
