def main():
    hello = input("Greet me. ")
    if hello.startswith("hello"):
        print("$0")
    elif detective(hello) == True:
        print("$20")
    else:
        print("$100")


def detective(i):
    if i.startswith("h"):
        return True


main()
