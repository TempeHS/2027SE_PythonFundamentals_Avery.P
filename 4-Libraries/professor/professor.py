import random


def main():
    turns = 10
    correct = 0
    attempts = 1
    if get_level():
        while turns > 0:
            try:
                if attempts == 1:
                    randomx = random.randint(1, 9)
                    randomy = random.randint(1, 9)
                if attempts <= 3:
                    answer = randomx + randomy
                    guess = int(input(f"{randomx} + {randomy} "))
                if guess == answer and attempts <= 3:
                    attempts = 1
                    turns -= 1
                    correct += 1
                    pass
                elif attempts > 3:
                    print(answer)
                    attempts = 1
                    turns -= 1
                    pass
                else:
                    print("EEE")
                    attempts += 1
                    pass
            except ValueError:
                print("EEE")
                attempts += 1
                pass
        print(f"{correct}/10")


def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if 3 >= lvl >= 1:
                return True
            else:
                pass
        except ValueError:
            pass


if __name__ == "__main__":
    main()
