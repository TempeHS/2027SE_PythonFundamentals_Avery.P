month = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}

while True:
    date = input().capitalize()
    date = date.replace("/", " ")
    date = date.replace(",", " ")
    x, y, z = date.split()
    if x in month and y < 32 and y > 0:
        print(f"{z:04}-{month[x]:02}-{y:02}")
        break
    else:
        pass
