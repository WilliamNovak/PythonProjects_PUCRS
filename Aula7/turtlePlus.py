import turtle

def quadrado(lado): # funcao que desenha quadrado
    for count in range(4):
        bob.forward(lado) # desenha para frente(linha reta)
        bob.right(90) # gira 90 graus

screen = turtle.Screen()
screen.clear() # limpa tela
screen.screensize(600, 400) # inicializa uma tela com o tamanho

bob = turtle.Turtle()
bob.speed(3) # velocidade do desenho (1 a 13)

for quad in range(4):
    quadrado(50)
    
    bob.penup() # Levanta a caneta, nao desenhar
    bob.left(90) # Vira para esquerda, para apontar para cima
    bob.forward(50) # Sobe
    bob.right(90) # Vira para direita para começar novo quadrado
    bob.pendown() # Coloca novamente a caneta para desenhar