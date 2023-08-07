import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".png") and not sys.argv[1].endswith(".jpg"):
    sys.exit("Invalid output")
elif not sys.argv[2].endswith(".png") and not sys.argv[2].endswith(".jpg"):
    sys.exit("Invalid output")
elif sys.argv[1].endswith(".jpg") and sys.argv[2].endswith(".png"):
    sys.exit("Input and output have different extensions")
elif sys.argv[1].endswith(".png") and sys.argv[2].endswith(".jpg"):
    sys.exit("Input and output have different extensions")
else:
    try:
        shirt = Image.open(sys.argv[1])
        overlay = Image.open("shirt.png")
    except FileNotFoundError:
         sys.exit("File does not exist")
    else:
        size = overlay.size

        copy1 = shirt.copy()

        resized_shirt = ImageOps.fit(copy1, size)
        resized_shirt.paste(overlay, overlay)
        resized_shirt.save(f'{sys.argv[2]}')
