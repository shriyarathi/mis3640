
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


