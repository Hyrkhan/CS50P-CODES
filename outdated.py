list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
day = ""
while True:
    user_input = input("Date: ").strip().title()
    for i in user_input:
        if i == "/":
            month, day_temp, year = user_input.split("/")
            break
        elif i == "-":
            month, day_temp, year = user_input.split("-")
            break
        elif i == " ":
            month, day_temp, year = user_input.split(" ")
            break

    if day_temp.isalpha():
        pass
    for monthlist in list:
        if monthlist == month:
            month = str(list.index(monthlist)+1)
            break
    if day_temp.isalpha():
        pass
    elif not day_temp.isdigit():
        for i in day_temp:
            if i.isdigit():
                day += i
    else:
        day = day_temp
    year,month,day = int(year),int(month),int(day)
    if month > 12:
        pass
    elif day > 31:
        pass
    else:
        break
year,month,day = int(year),int(month),int(day)
print(f"{year}-{month:02d}-{day:02d}")
