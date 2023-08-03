import inflect

p = inflect.engine()
list = []

while True:
    try:
        name = input("Name: ")
    except EOFError:
        for item in list:
            print(item)
        mylist = p.join(list)
        print("Adieu, adieu, to",mylist)
        break
    else:
        list.append(name)
        pass
