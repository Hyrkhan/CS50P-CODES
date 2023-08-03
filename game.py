import random


while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        pass
    else:
        if level <= 0:
            pass
        else:
            break
number = random.randint(1,level)

while True:
    try:
        answer = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if answer < 0:
            pass
        elif answer == number:
            print("Just right!")
            break
        elif answer > number:
            print("Too large!")
            pass
        elif answer < number:
            print("Too small!")
            pass
