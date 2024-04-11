from os import system
import cv2

ascii_chars = " .:-=+*#%@"
height = 100

def settings():
    global height
    global ascii_chars
    height = int(input("ENTER NO OF PIXELS VETICALLY(detail of the art depends on it)(default=100)\n"))
    x = int(input('ENTER SENSETIVITY OF DARK REGION(determine how much dark a color should be to not show)(range => 0 to 10)\n'))
    if x < 0: x = 0
    elif x > 10: x = 10
    ascii_chars = x*' '+ascii_chars

def main(): #terminal program using CTRL+C keyboard interrupt
    settings()
    input("TO STOP THE PROGRAM PRESS CTRL+C(KeyboardInterrupt)\nPRESS ANY KEY TO CONTINUE")
    vid = cv2.VideoCapture(0) 
    while True: 
        _,frame = vid.read() 
        frame_converter(frame)

def frame_converter(img):
    img = cv2.cvtColor(resize_live(img), cv2.COLOR_BGR2GRAY)
    h,w = img.shape
    out = ""
    for row in range(h):
        for col in range(w):
            density = img[row,col]
            c = art_char(density)
            out +=  c
        out += "\n" 
    printer(out)

def resize_live(img):
    oh,ow = img.shape[:2]
    width = int(height*(ow/oh))
    return cv2.resize(img,(width,height))

def art_char(intensity):
    ind = (len(ascii_chars)-1)*(intensity/255)
    return ascii_chars[int(ind)]

def printer(out):
    system("clear")
    print(out)
    print("ZOOM OUT")

if __name__ == "__main__":
    main()
