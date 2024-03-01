import turtle

def poligono(tam, lados):
    ang = 360/lados
    for lado in range(lados):
        bob.forward(tam)
        bob.right(ang)

bob = turtle.Turtle()
bob.penup()
bob.right(180)
bob.forward(180)
bob.right(180)
bob.pendown()

for lados in range(3, 7):
    poligono(50, lados)
    bob.penup()
    bob.forward(100)
    bob.pendown()