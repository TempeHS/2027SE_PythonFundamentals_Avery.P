import random

while True:
    try:
        guess = int(input("Level: "))
        break
    except ValueError:
        pass
guessing = random.randint(1, guess)
while True:
    try:
        level = int(input("Guess: "))
        if level == guessing:
            print("Just Right!")
            break
        elif level > guessing:
            print("Too big!")
            break
        else:
            print("Too small")
            break
    except ValueError:
        pass
