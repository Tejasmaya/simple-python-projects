# Awesome Project
import turtle

from turtle import *
import time

color('red')
begin_fill()
pensize(10)
left(50)
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)
end_fill()
pensize(1)
color('white')
left(51)
forward(130)
pensize(10)
color('green')
left(270)
forward(80)
circle(40, 190)
left(349)
forward(68)
time.sleep(5)

ts = turtle.getscreen()
ts.getcanvas().postscript(file="heart.eps")
# https://epsviewer.org/onlineviewer.aspx
# convert eps file to png or jpg to view the image
