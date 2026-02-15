name = input("What is your name? ")


match name:
    case "Luffy" | "Zoro" | "Nami":
        print("Straw Hats")
    case "Shanks":
        print("Red Hair")
    case __:
        print("Who?")
