def AddTen(n):
    x = n + 10
    return x

print (AddTen(10))

import turtle
dingus = turtle.Turtle()
def DrawRectangle (Anyturtle, l, w):
    for i in range (2):
        Anyturtle.forward(l)
        Anyturtle.right(90)
        Anyturtle.forward(w)
        Anyturtle.right(90)
DrawRectangle(dingus, 100, 50)
