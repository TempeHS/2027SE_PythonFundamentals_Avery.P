d = [key]
while True:
    try:
        list = input("Add to your list: ")
        d[key] = d.get(list, 0) + 1
    except EOFError:
        break
print(d)
