import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    students = []
    students2 = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({"name": row["name"], "house": row["house"]})
    except FileNotFoundError:
         sys.exit(f"Could not read {sys.argv[1]}")
    else:
        for student in students:
            lastname, firstname = student["name"].lstrip().rstrip().split(",")
            students2.append({"firstname" :firstname, "lastname": lastname,
                              "house": student["house"]})
        with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            for student in students2:
                writer.writerow({"first": student["firstname"],
                                 "last": student["lastname"],
                                 "house": student["house"]})


