from PIL import Image

char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ?,;./:!%*$éèà&0123456789'-_()/@+-/=°çê "

phrase = input("[?] Message : ")
l = len(phrase)
colors = []

for lettre in phrase:
    colors.append((0 + char.index(lettre), 0 + char.index(lettre), 0 + char.index(lettre)))

img_name = input("[?] Image name : ")
loaded = False

while not loaded:
    try:
        img = Image.open(img_name)
        width, height = img.size
        loaded = True
    except FileNotFoundError:
        print("\n[!] File not found, try to drag it in this window")
        img_name = input("[?] Image name : ")

pixels = img.load()

space = input("[?] Space between 2 char : ")
done = False

while not done:
    try:
        space = int(space)
        if space >= 0:
            done = True
        else:
            print("\n[!] Space must be greater or equal to 0.")
            space = input("[?] Space between 2 char : ")
    except ValueError:
        print("\n[!] Please input an integer.")
        space = input("[?] Space between 2 char : ")

index = 0
counter = -1

if not width < l * (space + 1):
    if not space == 0:
        for i in range(l * (space + 1)):
            counter += 1
            if counter == 0:
                pixels[width - i - 1, height - 1] = colors[index]
                index += 1
            else:
                if counter == space:
                    counter = -1
    else:
        for i in range(l):
            pixels[width - i - 1, height - 1] = colors[i]

    name = str(space) + "_" + str(l) + '.png'

    img.save(name)

    print("[*] Image " + name + " saved with the message '" + phrase + "'")

else:
    print("\n[!] Error:\n[*]\t• Message longer than image width ( char / pixel )\n[*]\t• Space too long between two char.\n[*] In any case please reduce one of these two values.")
