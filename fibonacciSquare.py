def square(t,l):
    t.pencolor("black")
    for i in range(4):
        t.forward(l)
        t.left(90)
        if i==1:
            pos = t.pos()
    t.pencolor("red")
    #t.left(45)
    arc(t, l, 4)
    #t.goto(pos)
    #t.left(45)
    return pos

def arc(t, r, p=4):
    t.speed("fastest")
    import math
    for i in range(360/p):
        t.left(1)
        t.forward(2*math.pi*r/360)
        

from turtle import *
t=Turtle(shape="turtle")
t.width(3)
t.right(90)
l = 17
fibo_num = 8

fibonacci =[1,1]
for i in range(fibo_num-2):
    fibonacci.append(fibonacci[-1]+fibonacci[-2])

for i in fibonacci:      
    p=square(t,i*l)
    t.goto(p)
    
