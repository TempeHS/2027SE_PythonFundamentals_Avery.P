from pyfiglet import Figlet
import sys

s = input("What is your message? ")


figlet = Figlet()
figlet.getFonts()


if len(sys.argv) == 1:
    pass

elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    f = sys.argv[2]
    if f not in figlet.getFonts():
        sys.exit("Wrong Font")
    figlet.setFont(font=f)

else:
    sys.exit("You messed up something")

print(figlet.renderText(s))
