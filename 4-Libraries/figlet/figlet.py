from pyfiglet import Figlet
import sys

s = input("What is your message? ")
figlet = Figlet()
figlet.getFonts()
figlet.setFont(font=f)

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

print(figlet.renderText(s))
