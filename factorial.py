import turtle
def draw_tree(l, level):
    width = t.width()  # save the current pen width

    t.width(width * proportion)  # narrow the pen width

    l = proportion * l

    #left path
    t.lt(s)
    t.fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    t.bk(l)

    #right path
    t.rt(2 * s)
    t.fd(l)
    if level < lv:
        draw_tree(l, level + 1)

    #going back
    t.bk(l)
    t.lt(s)
    t.width(width)  # restore the previous pen width

# set up
t = turtle.Turtle(shape="turtle")
t.lt(90)
lv = 13 #for paper 10 levels for paper 13 levels
l = 100#120  initial LENG stem
s = 45#35 for paper 17 ANGLE
proportion = 2.0/3#3.0/4
t.width(lv)
t.penup()
t.bk(l) #SET up position

#first stem
t.pendown()
t.fd(l) #first stem
t.speed("fastest")
#call recursive function
draw_tree(l, 2)
t.color("blue")
t.pencolor("green")
turtle.done()
