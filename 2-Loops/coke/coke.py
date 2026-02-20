def main():
    get_money()


def get_money():
    money = 50
    while money > 0:
        n = int(input("Insert coins: "))
        if n == 10:
            money -= 10

        elif n == 25:
            money -= 25

        elif n == 5:
            money -= 5
        else:
            print("Invalid coin type")
        if money > 0:
            print("Amount owed:", money)
    if money <= 0:
        money = abs(money)
        print("Change Owed:", money)

    return money


main()
