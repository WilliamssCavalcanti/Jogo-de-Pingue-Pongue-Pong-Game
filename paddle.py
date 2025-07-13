from turtle import Turtle

class Paddle(Turtle):


    def __init__(self, position):
        super().__init__()
        self.shape('square') # Define a forma das "barras"(raquetes) como quadrados
        self.color('white') # Define a cor das "barras"(raquetes) como brancas
        self.shapesize(stretch_wid=5, stretch_len=1) # Estica a forma para deixar mais parecida com as "barras"(raquetes) das versões antigas do jogo
        self.penup() # Impede que as "barras"(raquetes) desenhem ao se movimentar
        self.goto(position) # Move a raquete para a posição inicial (definida ao criar o objeto)

    def go_up(self):
        new_y = self.ycor() + 20 # Move a "barra"(raquete) 20 unidades para cima
        self.goto(self.xcor(), new_y)

    def go_down(self): # Move a "barra"(raquete) 20 unidades para baixo
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
