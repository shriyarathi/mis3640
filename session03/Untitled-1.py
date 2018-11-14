
import math
import turtle
radius=int(input("What is the radius? "))
petals=int(input("How many petals? "))
#radius=110
#petals=4


def draw_arc(b,r):
    c=2*math.pi*r 
    ca=c/(360/60)  
    n=int(ca/3)+1  
    l=ca/n  
    for i in range(n):
        b.fd(l)
        b.lt(360/(n*6))


def draw_petal(b,r):
    draw_arc(b,r)
    b.lt(180-60)
    draw_arc(b,r)
    b.rt(360/petals-30)  


shriya=turtle.Turtle()


for i in range(petals):
    draw_petal(shriya,radius)
    shriya.lt(360/4)



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
