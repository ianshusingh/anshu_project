from turtle import *

def square(d=100):
    for i in range(4):
        fd(d)
        lt(90)
        
def polygon(side=3, dis=50):
    for i in range(side):
        fd(dis)
        lt(360/side)
        
square()
polygon(6,100)
#square(150)
#square(200)
#square(250)
hideturtle()
mainloop()