import sys
import tabulate
import csv

if len(sys.argv) > 2:
    sys.exit("Too Many Arguments")
elif len(sys.argv) < 2:
    sys.exit("Too Few Arguments")
else:
    fileName = sys.argv[1]


if fileName.endswith(".csv"):
    try:
        with open(fileName) as file:
            rows = list(csv.reader(file))
            headers = rows[0]
            table = rows[1:]
            print(tabulate.tabulate(table, headers=headers, tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File Does Not Exist!")
else:
    sys.exit("Doesn't end with .csv")
