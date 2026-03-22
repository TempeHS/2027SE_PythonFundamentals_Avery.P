import sys
if sys.argv > 2:
    print("Too Many Arguments")
    sys.exit
elif sys.argv < 2:
    print("Too Few Arguments")
    sys.exit
else:
    filen = sys.argv


try:
    with open()
except FileNotFoundError:
    print("File Does Not Exist!")
    sys.exit