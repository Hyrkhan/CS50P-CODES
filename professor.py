import random


def main():
    level = get_level()
    score = 0

    for _ in range (0,10):
        x,y = generate_integer(level)
        z = x + y
        times = 0

        while True:
            if times == 3:
                print(f"{x} + {y} = {z}")
                break
            print(f"{x} + {y} =", end="")
            answer = int(input(" "))
            if answer == z:
                score += 1
                break
            else:
                print("EEE")
                times += 1
                pass
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level < 1 or level > 3:
                pass
            else:
                break
    return level


def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x, y


if __name__ == "__main__":
    main()
