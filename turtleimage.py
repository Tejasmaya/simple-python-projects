# import turtle
#
# screen = turtle.Screen()
#
# # click the image icon in the top right of the code window to see
# # which images are available in this trinket
# image = "C:\\Users\\Tejasmaya Sitha\\OneDrive\\Desktop\\wallpaper.JPG"
#
# # add the shape first then set the turtle shape
# screen.addshape(image)
# turtle.shape(image)
#
# screen.bgcolor("lightblue")
#
# move_speed = 10
# turn_speed = 10
#
#
# # these defs control the movement of our "turtle"
# def forward():
#     turtle.forward(move_speed)
#
#
# def backward():
#     turtle.backward(move_speed)
#
#
# def left():
#     turtle.left(turn_speed)
#
#
# def right():
#     turtle.right(turn_speed)
#
#
# turtle.penup()
# turtle.speed(0)
# turtle.home()
#
# # now associate the defs from above with certain keyboard events
# screen.onkey(forward, "Up")
# screen.onkey(backward, "Down")
# screen.onkey(left, "Left")
# screen.onkey(right, "Right")
# screen.listen()


import cv2
import turtle

# # Binary Image
#
# img = cv2.imread("C:\\Users\\Tejasmaya Sitha\\OneDrive\\Desktop\\DSC_0005.jpg", 2)
# ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# width = int(img.shape[1])
# height = int(img.shape[0])
#
# # Turtle Setup
#
# my_screen = turtle.Screen()
# my_screen.screensize(width, height)
# my_pen = turtle.Turtle()
# my_screen.tracer(0)
#
# # Printing Loop
#
# for i in range(int(height / 2), int(height / -2), -1):
#     my_pen.penup()
#     my_pen.goto(-(width / 2), i)
#
#     for l in range(-int(width / 2), int(width / 2), 1):
#         pix_width = int(l + (width / 2))
#         pix_height = int(height / 2 - i)
#         if bw_img[pix_height, pix_width] == 0:
#             my_pen.pendown()
#             my_pen.forward(1)
#         else:
#             my_pen.penup()
#             my_pen.forward(1)
#     my_screen.update()
#
# my_pen.hideturtle()
#
# turtle.done()


import cv2
import turtle

import matplotlib
import numpy as np
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')
import time


def find_closest(p):
    if len(positions) > 0:
        nodes = np.array(positions)
        distances = np.sum((nodes - p) ** 2, axis=1)
        i_min = np.argmin(distances)
        return positions[i_min]
    else:
        return None


def outline():
    src_image = cv2.imread(image, 0)
    blurred = cv2.GaussianBlur(src_image, (7, 7), 0)
    th3 = cv2.adaptiveThreshold(blurred, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                thresholdType=cv2.THRESH_BINARY, blockSize=9, C=2)
    return th3


# USe reduced size image(height upto 800 px , width upto 900px, and size upto 200 kb)
# otherwise it will take more time for processing
# image = 'shiva.jpg'
image = 'mani.jpg'
# image = 'wallpaper.jpg'
# image = "DSC_0005.jpg"
# image = 'WhatsApp Image 2022-10-10 at 10.47.10 PM.jpeg'
im = cv2.imread(image, 0)
th3 = outline()

plt.imshow(th3)
plt.axis('off')
plt.tight_layout()
# plt.show()

WIDTH = im.shape[1]
HEIGHT = im.shape[0]
print(WIDTH, HEIGHT)

CUTOFF_LEN = ((WIDTH + HEIGHT) / 2) / 60  # 60 threshold value
iH, iW = np.where(th3 == [0])
iW = iW - WIDTH / 2
iH = -1 * (iH - HEIGHT / 2)
positions = [list(iwh) for iwh in zip(iW, iH)]

# win = turtle.Screen()
# win.bgcolor('black')

t = turtle.Turtle()
t.color("brown")
t.shapesize(1)
t.pencolor("gray30")

t.speed(0)
turtle.tracer(0, 0)
t.penup()
t.goto(positions[0])
t.pendown()

time.sleep(3)

p = positions[0]
while (p):
    p = find_closest(p)
    if p:
        current_pos = np.asarray(t.pos())
        new_pos = np.asarray(p)
        length = np.linalg.norm(new_pos - current_pos)
        if length < CUTOFF_LEN:
            t.goto(p)
            turtle.update()
        else:
            t.penup()
            t.goto(p)
            t.pendown()
        positions.remove(p)
    else:
        p = None

# turtle.done()
time.sleep(13)
# turtle.Screen().bye()  # close the screen after complete
ts = turtle.getscreen()
ts.getcanvas().postscript(file="image.eps")

# https://convertepstojpg.com/convertepstojpg.aspx
# convert eps file to png or jpg to view the image


# https://github.com/Random-Codez/turtle_python
# https://github.com/pyGuru123/Turtle-Animations
