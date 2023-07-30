sentence = input("camelCase: ")

print("snake_case: ", end="")
for letters in sentence:
    if letters.isupper():
        print("_"+letters.lower(), end="")
    else:
        print(letters, end="")
print()
