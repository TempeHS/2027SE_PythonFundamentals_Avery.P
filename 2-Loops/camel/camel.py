camel = input("What is your variable name? ")
snake = ""

for character in camel:
    if character.isupper():
        snake += "_" + character.lower()
    else:
        snake += character

print(snake)
