# Determinar a menor distância entre 3 pontos
import turtle, math

def retangulo(tamHoriz, tamVert):
  for lado in range(2):
    bob.forward(tamHoriz)
    bob.right(90)
    bob.forward(tamVert)
    bob.right(90)

def ponto(t,x,y,tam):
  tam = tam / 2
  t.penup()
  t.setposition(x-tam,y-tam)
  t.pendown()
  retangulo(tam*2,tam*2)

def distancia(x1,y1,x2,y2):
    deltax = x1 - x2
    deltay = y1 - y2
    dist = math.sqrt(deltax**2 + deltay**2)
    return dist

def menorDist(x1,y1,x2,y2,x3,y3):
  d12 = distancia(x1,y1,x2,y2)
  d13 = distancia(x1,y1,x3,y3)
  d23 = distancia(x2,y2,x3,y3)
  return min(d12,d13,d23) # min retorna o menor valor

x1 = 0
y1 = 0
x2 = 100
y2 = 100
x3 = 150
y3 = 40

bob = turtle.Turtle()
bob.speed(13)

ponto(bob,x1,y1,8)
ponto(bob,x2,y2,8)
ponto(bob,x3,y3,8)
minDist = menorDist(x1,y1,x2,y2,x3,y3)
print(f"Menor distância: {minDist:.5f}")