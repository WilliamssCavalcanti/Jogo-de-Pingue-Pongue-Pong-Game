from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Configuração da jnaela do jogo
screen = Screen()
screen.bgcolor('black') # Cor do fundo definida como preto
screen.setup(width=800, height=600) # Tamanho da tela 
screen.title('Meu Jogo de Pingue-Pongue / My Pong Game') # Titulo da janela
screen.tracer(0) # Desativa a atualização automática da tela

r_paddle = Paddle((350, 0)) # "Barra"(raquete) da direita na posição x = 350
l_paddle = Paddle((-350, 0)) # "Barra"(raquete) da esquerda na posição x = -350
ball = Ball() # Bola
scoreboard = Scoreboard() # Placar

screen.listen() # Faz a janela escutar os botões do teclado
screen.onkey(r_paddle.go_up, 'Up') # Tecla para cima faz a "barra"(Raquete) direita ir para cima
screen.onkey(r_paddle.go_down, 'Down') # Tecla para baixo faz a "barra"(Raquete) direita ir para baixo
screen.onkey(l_paddle.go_up, 'w') # Tecla " W " faz a "barra"(Raquete) esquerda ir para cima
screen.onkey(l_paddle.go_down, 's') # Tecla " S " faz a "barra"(Raquete) esquerda ir para baixo



game_is_on = True
while game_is_on: # Loop principal do jogo
    time.sleep(ball.move_speed) # Controla a velocidade do jogo com base na bola
    screen.update() # Atualiza a tela manualmente (ja que o tracer está desligado)
    ball.move() # Move a bola

    #Detectar colisão com a parede
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detectar colisão com a barrinha
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < - 320:
        ball.bounce_x()

    #Detectar se a barrinha da direita erra a bola
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point() # Jogador da esquerda marca ponto

    # Detectar se a barrinha da esquerda erra a bola
    if ball.xcor() < -380:
        ball.reset_position() # Jogador da direita marca ponto
    
screen.exitonclick() # Fecha a janela ao clicar
