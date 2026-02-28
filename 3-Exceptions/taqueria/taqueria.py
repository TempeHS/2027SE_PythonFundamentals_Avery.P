menus = [
    {
        "baja taco": 4.25,
        "burrito": 7.50,
        "bowl": 8.50,
        "nachos": 11.00,
        "quesadilla": 8.50,
        "super burrito": 8.50,
        "super quesadilla": 9.50,
        "taco": 3.00,
        "tortilla salad": 8.00,
    }
]
x = 0
while True:
    ask = input("What would you like to order? ").casefold()
    if ask != "End" or ask != "end":
        pass
    else:
        break
    for menu in menus:
        if ask in menu:
            x += menu[ask]
            break
        else:
            pass
    question = input("Would you like to order more food? ")
    if question == "Yes" or question == "yes" or question == "y" or question == "Y":
        pass
    elif question == "No" or question == "no" or question == "n" or question == "N":
        break
    else:
        print("Unclear answer looping")
        pass

print("Total:", x)
