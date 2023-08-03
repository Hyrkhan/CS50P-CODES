import sys
from pyfiglet import Figlet

listfonts = Figlet().getFonts()
thereisfont = False

if len(sys.argv) == 1:
    fonts = "standard"
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        fonts = sys.argv[2]
        for font in listfonts:
            if font == fonts:
                thereisfont = True
        if not thereisfont:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")

phrase = input("Input: ")

f = Figlet(font=fonts)
print("Output:")
print(f.renderText(phrase))
