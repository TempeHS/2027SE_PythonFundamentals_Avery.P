twtter = input("What's your message? ").casefold
twtter = twtter.replace("a", "")
twtter = twtter.replace("e", "")
twtter = twtter.replace("i", "")
twtter = twtter.replace("o", "")
twtter = twtter.replace("u", "")
twtter = twtter.capitalize()
print(twtter)
