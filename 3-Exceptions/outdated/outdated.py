def main():
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
        try:
            date = input().capitalize()
            date = date.replace("/", " ")
            date = date.replace(",", " ")
            x, y, z = date.split()
            y = int(y)
            z = int(z)
            if x.isnumeric() and 1 <= int(x) <= 12:
                month_num = int(x)
                if 0 < y < 32:
                    print(f"{z:04}-{month_num:02}-{y:02}")
                    break
                else:
                    print("Try again")
                    pass
            elif x in month and 0 < y < 32:
                print(f"{z:04}-{month[x]:02}-{y:02}")
                break

            else:
                print("Try Again")
                pass
        except ValueError:
            print("Try Again")
            pass


main()
