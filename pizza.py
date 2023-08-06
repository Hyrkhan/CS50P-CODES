import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
     sys.exit("Not a csv file")
else:
    menu = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for lines in reader:
                menu.append(lines)
            print(tabulate(menu[1:], headers=menu[0] ,tablefmt="grid"))
    except FileNotFoundError:
         sys.exit("File does not exist")
