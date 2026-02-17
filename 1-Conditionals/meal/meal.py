def main():
    time = input("What is the time? ")
    convert(time)


def convert(i):
    i = i.replace(":", "")
    i = int(i)
    if 800 >= i >= 700:
        print("Breakfast")
    elif 1300 >= i >= 1200:
        print("Lunch time")
    elif 1900 >= i >= 1800:
        print("Dinner time")
    else:
        print("No meal :(")


main()
