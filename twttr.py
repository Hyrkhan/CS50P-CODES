sentence = input("Input: ")
vowels = ["A","E","I","O","U"]

for letters in sentence:
    if letters.upper() in vowels:
        continue
    else:
        print(letters, end="")

print()
