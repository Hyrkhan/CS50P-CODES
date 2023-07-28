def main():
    ...
    gettime = input("What time is it? ")
    time = convert(gettime)
    if 7.0 <= time and time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time and time <= 13.0:
        print("lunch time")
    elif 18.0 <= time and time <= 19.0:
        print("dinner time")

def convert(time):
    ...
    hours,mins = time.split(":")
    minutes = int(mins) / 60
    return float(int(hours) + minutes)

if __name__ == "__main__":
    main()
