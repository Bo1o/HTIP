from PIL import Image

char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ?,;./:!%*$éèà&0123456789'-_()/@+-/=°çê "


img_name = input("[?] Image name : ")
loaded = False

while not loaded:
    try:
        img = Image.open(img_name)
        width, height = img.size
        loaded = True
    except FileNotFoundError:
        print("[!] File not found.")
        img_name = input("[?] Image name : ")

pixels = img.load()

try:
    liste = list(img_name.replace('.png', ''))
    space = ""
    nb = ""
    found = False
    if "_" in liste:
        for i in range(len(liste)):
            if liste[i] == "_":
                found = True
            if not found:
                space += liste[i]
            else:
                nb += liste[i]

        space = int(space)
        nb = nb[1:]
        nb = int(nb)
    else:
        print("[!] File name must be with looking like this : x_y.png\nNote that x and y must be integers.")
except:
    print("[!] File name must be with looking like this : x_y.png\nNote that x and y must be integers.")


message = ""
counter = -1

for i in range(nb * (space + 1)):
    counter += 1
    if counter == 0:
        message += char[pixels[width - i - 1, height - 1][0]]
    else:
        if counter == space:
            counter = -1


print(message)
