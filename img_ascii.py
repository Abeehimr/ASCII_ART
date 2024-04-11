from PIL import Image
from os import system
from time import sleep

ascii_chars = " .:-=+*#%@"
height = 100
def height_def():
    global height
    height = int(input("ENTER NO OF PIXELS VETICALLY(detail of the art depends on it)(default=100)\n"))
    if height <= 0: height = 100
def video(name):
    height_def()
    inf = input("DO YOU WANT GIF/MP4 TO DISPLAY ENDLESSLY(Y/N): ")
    input("TO STOP THE PROGRAM PRESS CTRL+C(KeyboardInterrupt)\nPRESS ANY KEY TO CONTINUE")
    with Image.open(f"imgs/{name}") as im:
        while True:
            try:
                converter(im)
                sleep(1/60)
                im.seek(im.tell() + 1)
            except EOFError:
                if inf.upper() == "Y":
                    im.seek(0)
                else:
                    break
def img(name):
    height_def()
    with Image.open(f"imgs/{name}") as im:
        converter(im)
         
def converter(img):
    img = resaaz(img).convert("L")
    w,h = img.size
    pix = img.getdata()
    out = ""
    for row in range(h):
        for col in range(w):
            density = pix[row*w+col]
            out += art_char(density)
        out += "\n" 
    printer(out)
    
def resaaz(img):
    ow,oh = img.size
    width = int(height*(ow/oh))
    return img.resize((width,height))

def art_char(intensity):
    ind = (len(ascii_chars)-1)*(intensity/255)
    return ascii_chars[int(ind)]

def printer(out):
    system("clear")
    print(out)

if __name__ == "__main__":
    name = input("PUT IMAGE/VIDEO IN imgs FOLDER AND WRITE ITS NAME WITH EXTENSION\n").strip()
    try:
        if name.endswith(".gif") or name.endswith(".mp4"):
            video(name)
        else:
            img(name)
    except FileNotFoundError:
        print("FILE NOT FOUND")


