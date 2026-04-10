def main():
    twitter = input("Say something: ")
    print(shorten(twitter))


def shorten(word):
    result = ""
    not_allowed = ["A", "a", "E", "e", "I", "i", "O", "o"]
    for letter in word:
        if letter not in not_allowed:
            result += letter
    return result


if __name__ == "__main__":
    main()
