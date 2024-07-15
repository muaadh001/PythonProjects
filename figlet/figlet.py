from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) == 1:
    RandomFont = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    RandomFont = False
else:
    print("Invalid Usage")
    sys.exit(1)

msg = input("input: ")
figlet.getFonts()

if RandomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(msg))
    except:
        print("Invalid Usage")
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())

print("Output: ")
print(figlet.renderText(msg))
