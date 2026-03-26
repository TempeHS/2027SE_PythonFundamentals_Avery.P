import sys
import csv

if len(sys.argv) > 3:
    sys.exit("Too Many Arguments")
elif len(sys.argv) < 3:
    sys.exit("Too Few Arguments")
else:
    fileName = sys.argv[1]
    fileOut = sys.argv[2]


if fileName.endswith(".csv"):
    try:
        with open(fileName, "r", newline="") as file, open(
            fileOut, "w", newline=""
        ) as ofile:
            reader = csv.DictReader(file)
            writer = csv.DictWriter(ofile, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                house = row["house"]
                last, first = row["name"].split(", ")
                writer.writerow(
                    {
                        "first": first.strip(),
                        "last": last.strip(),
                        "house": house.strip(),
                    }
                )
    except FileNotFoundError:
        sys.exit("File Does Not Exist!")
else:
    sys.exit("Doesn't end with .csv")
