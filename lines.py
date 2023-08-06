import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith("py"):
     sys.exit("Not a Python file")
else:
    linez = []
    try:
        with open(sys.argv[1]) as file:
            lines = file.readlines()
            for line in lines:
                if line.isspace():
                    pass
                elif line.lstrip().startswith("#"):
                    pass
                else:
                    linez.append(line.lstrip().rstrip())
            print(len(linez))
    except FileNotFoundError:
         sys.exit("File does not exist")
