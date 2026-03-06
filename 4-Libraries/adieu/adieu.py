
byes = {}
while True:
    try:
        bye = input().capitalize()
        byes[bye] = 1
    except EOFError:
        print()
        break
print("Adieu, adieu, to ", end="")
lon = len(byes)
for bye in byes:
    if lon > 2:
        print(bye, end=", ")
        lon -= 1
    elif lon == 2:
        print(bye, end=" and ")
        lon -= 1
    elif lon == 1:
        print(bye, end="")
        lon -= 1


print()
