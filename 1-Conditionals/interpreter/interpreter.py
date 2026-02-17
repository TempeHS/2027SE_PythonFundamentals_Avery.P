def main():
    problem = input("What's your math problem? ")
    x, y, z = problem.split(" ")
    x = float(x)
    z = float(z)
    if y == "/":
        print(x / z)
    elif y == "*" or y == "x":
        print(x * z)
    elif y == "-":
        print(x - z)
    else:
        print(x + z)


main()
