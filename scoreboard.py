from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white') # Cor do texto(placar)
        self.penup() # Impede que a tartaruga desenhe linhas
        self.hideturtle() # esconde o cursor da tartaruga (só mostra o texto)
        self.l_score = 0 # Placar do jogador da esquerda
        self.r_score = 0 # Placar do jogador da direita
        self.update_scoreboard() # Atualiza o placar inicial

    def update_scoreboard(self): # Atualiza o placar da tela
        self.clear() # Limpa o texto anterior
        self.goto(-100, 200) # Posição do placar do jogador da esquerda
        self.write(self.l_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200) # Posição do placar do jogador da direita
        self.write(self.r_score, align='center', font=('Courier', 80, 'normal'))

    def l_point(self):
        # Adiciona um ponto ao jogador da esquerda
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        # Adiciona um ponto ao jogador da direita
        self.r_score += 1
        self.update_scoreboard()
