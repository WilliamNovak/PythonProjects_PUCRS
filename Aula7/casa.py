import turtle

def poligono(tam, lados):
    ang = 360/lados
    for lado in range(lados):
        bob.forward(tam)
        bob.right(ang)

def retangulo(tamHoriz, tamVert):
    for cont in range(2):
        bob.forward(tamHoriz)
        bob.right(90)
        bob.forward(tamVert)
        bob.right(90)
    
def casa():
    retangulo(110, 80)
    bob.left(60)
    poligono(110, 3)
    bob.penup()
    bob.right(60)
    bob.forward(30)
    bob.right(90)
    bob.forward(50)
    bob.left(90)
    bob.pendown()
    retangulo(20, 30)


bob = turtle.Turtle()
for x in range(-300, 250, 120):
    bob.penup()
    bob.setposition(x,0)
    bob.setheading(0)
    bob.pendown()
    casa()