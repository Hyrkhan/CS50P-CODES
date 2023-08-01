while True:
    try:
        x,y = input("Fraction: ").split("/")
        z = int(x) / int(y)
    except ValueError:
        print("Please enter integer only")
    except ZeroDivisionError:
        print("Cannot enter zero")
    else:
        percentage = z * 100
        percent = round(percentage)
        if percent <= 100:
            if percent >= 99:
                print("F")
            elif percent <= 1:
                print("E")
            else:
                print(f"{percent}%")
            break
        else:
            continue
