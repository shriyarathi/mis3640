import turtle
import  math

def c1(radius):
    width(3)
    circle(radius/2., 180)
    circle(radius, 180)
    left(180)
    circle(-radius/2., 180)
    end_fill()
    left(90)
    up()
    forward(radius*0.35)
    right(90)
    down()
    color(color1, color2)
    begin_fill()
    circle(radius*0.15)
    left(90)
    up()
    backward(radius*0.35)
    down()
    left(90)
   mainloop()