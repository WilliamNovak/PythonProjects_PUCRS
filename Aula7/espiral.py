import turtle

def espiral(total):
    for cont in range(total):
        dist = 2 + cont/4
        ang = 30 - cont/12
        bob.forward(dist)
        bob.left(ang)

bob = turtle.Turtle()
bob.speed(13)
espiral(180)