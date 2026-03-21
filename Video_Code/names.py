names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")


# with open("names.txt", "r") as file:
#    for line in file:
#        print("hello,", line.rstrip())

# name = input("What's your name? ")

# with open("names.txt", "a") as file:
#    file.write(f"{name}\n")


# names = []

# for _ in range(3):
#    name = input("What's your name? ")
#    names.append(name)


# for name in sorted(names, reverse=True): the reverse makes it reverse alphabetical order
#    print(f"Hello, {name}")
