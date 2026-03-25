import sys

if len(sys.argv) > 2:
    sys.exit("Too Many Arguments")
elif len(sys.argv) < 2:
    sys.exit("Too Few Arguments")
else:
    fileName = sys.argv[1]


if fileName.endswith(".py"):
    try:
        with open(fileName) as file:
            counter = 0
            for line in file:
                sline = line.lstrip()
                if not sline:
                    continue
                if sline.startswith("#"):
                    continue
                counter += 1
    except FileNotFoundError:
        sys.exit("File Does Not Exist!")
else:
    sys.exit("Doesn't end with .py")


print(f"Lines of code is: {counter}")
