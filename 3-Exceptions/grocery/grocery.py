items = []
while True:
    try:
        item = input("Add to your list: ")
        if item:
            if item in items:
                items[count] += 1
            else:
                items[count] = 1
    except EOFError:
        print()
        break
for item, count in items.items():
    print(f"{count} {item}")
