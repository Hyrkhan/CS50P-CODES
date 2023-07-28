x,y,z = input("Expression: ").strip().split(" ")

x = int(x)
z = int(z)

match y:
    case "+":
        print(float(x + z))
    case "-":
        print(float(x - z))
    case "*":
        print(float(x * z))
    case "/":
        print(float(x / z))
