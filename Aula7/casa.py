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
    retangulo(150, 120)
    bob.left(60)
    poligono(150, 3)
    bob.penup()
    bob.right(60)
    bob.forward(30)
    bob.right(90)
    bob.forward(70)
    bob.left(90)
    bob.pendown()
    retangulo(40, 50)


bob = turtle.Turtle()
casa()