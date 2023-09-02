import turtle
vr = turtle.Turtle()
turtle.Screen().bgcolor('white')

turtle.pensize(4)
vr.speed (10)


def drawcurve():
    for i in range(200):
        
        vr.right(1)
        vr. forward(1)
        
vr.color('purple', 'purple')
 
vr.begin_fill()
vr.left(140)
vr.forward(111.65)
drawcurve()
vr.left(120)
drawcurve()

vr.forward(111.65)
 
vr.end_fill()
vr.penup()
vr.goto(77, -40)
vr.pendown()
vr.hideturtle()