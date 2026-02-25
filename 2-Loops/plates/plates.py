def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if length(s) and beginnum(s) and ischar(s) and middlenum(s):
        return True


def length(l):
    if len(l) > 6 or len(l) < 2:
        return False
    else:
        return True


def beginnum(n):
    if n[0:2].isalpha():
        return True
    else:
        return False


def ischar(c):
    if c.isalnum():
        return True
    else:
        return False


def middlenum(m):
    lrn = len(m) - 2
    lon = len(m) - 1
    ltn = len(m) - 3
    lan = len(m) + 1
    if (
        m[2:ltn].isnumeric()
        or m[3:lrn].isnumeric()
        or m[4:lon].isnumeric()
        and m[len(m) : lan].isalpha()
    ):
        return False
    else:
        return True


main()
