import turtle
import colorsys

t =turtle.Turtle()
s =turtle.Screen()
s.bgcolor('black')
t.speed(0)
n = 100
h =0

for i in range(360):
    col = colorsys.hsv_to_rgb(h,1,0.8)
    h += 1/n
    t.color(col)
    t.left(i)
    for j in range(3):
        t.forward(i*4)
        t.left(120)
