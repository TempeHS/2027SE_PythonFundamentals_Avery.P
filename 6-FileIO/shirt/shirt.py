import sys
from PIL import Image, ImageOps


if len(sys.argv) > 3:
    sys.exit("Too Many Arguments")
elif len(sys.argv) < 3:
    sys.exit("Too Few Arguments")
else:
    before = sys.argv[1]
    after = sys.argv[2]

if not before.endswith(".jpg") or not after.endswith(".jpg"):
    sys.exit("Invalid File Type")


with Image.open(before) as person, Image.open("took.png") as shirt:
    fitted = ImageOps.fit(person, shirt.size)
    fitted.paste(shirt, (0, 0), shirt)
    fitted.save(after)
