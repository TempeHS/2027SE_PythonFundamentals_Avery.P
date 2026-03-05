byes = {}
while True:
    try:
        bye = input().capitalize()
        byes[bye] = 1
    except EOFError:
        print()
        break
print("Adieu, adieu, to ", end="")
for bye in byes:
    print(bye, end=", ")


print()
