def main():
    while True:
        try:
            fraction = input("What's your fuel at? ")
            x = fraction[0:1]
            z = fraction[2:3]
            x = int(x)
            z = int(z)
            percentage = x / z * 100
            break
        except (ValueError, ZeroDivisionError):
            pass

    if percentage == 100:
        print("F")
    elif percentage == 0:
        print("E")
    else:
        percentage = str(percentage)
        percentage = percentage.replace(".0", "%")
        print(percentage)


main()
