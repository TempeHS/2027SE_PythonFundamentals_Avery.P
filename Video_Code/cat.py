def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("meow")


main()


# while True:
#    n = int(input("what's n? "))
#    if n > 0:
#        break

# for _ in range(n):
#    print("meow")

# for _ in range(3):
#    print("meow")

# count = 0
# while count != 3:
#    print("meow")
#    count += 1

# print("meow\n" * 3, end="")
