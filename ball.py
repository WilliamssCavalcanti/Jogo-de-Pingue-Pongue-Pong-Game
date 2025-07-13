from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')   # Cor da bola definida para branco
        self.shape('circle')  # Formato foi definido como circulo
        self.penup() # Isso impede que a bola fique desenhando o caminho
        self.x_move = 10 # velocidade inicial do eixo X
        self.y_move = 10 # velocidade inicial do eixo y
        self.move_speed = 0.1 # velocidade de moviemento (tempo entre frames)

    def move(self): 
        # Move a bola somando os valores atuais de x e y
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # Inverte a direção no eixo Y ( quando bate no teto ou chão)
        self.y_move *= -1
    
    def bounce_x(self):
        # Inverte a direção no eixo X ( quando bate nas "barras"(raquetes))
        self.x_move *= -1
        # Aumenta a velocidade da bola a cada colisão com a "barra"(raquete)
        self.move_speed *= 0.9
    
    def reset_position(self):
        # Reposiciona a bola no centro e redefine a velocidade
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x() # Faz a bola começar indo na direção oposta
