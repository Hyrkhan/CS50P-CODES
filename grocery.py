list = {}
isthere = False

while True:
    try:
        item = input("").strip().upper()
    except EOFError:
        print()
        """
        for (key, value) in list.items():
            print("{value} {key}".format(key = key, value = value))
        """
        for key in sorted(list):
            print(list[key], key)
        break
    else:
        while True:
            for (key, value) in list.items():
                if key == item:
                    list[item] = value + 1
                    isthere = True
                    break
            if not isthere:
                list[item] = 1
                break
            else:
                isthere = False
                break
        pass
