import turtle


def draw_multicolored_square(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)

size=20


for j in range(5):
    draw_multicolored_square(tess, size)
    size= size + 20
    tess.penup()
    tess.forward(-10)
    tess.right(90)
    tess.forward(10)
    tess.left(90)
    tess.pendown()
    

wn.mainloop()
    
