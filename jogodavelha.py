import pygame

# Inicializa o pygame
pygame.init()

# Define o tamanho da tela
width = 600
height = 600

# Cria a tela
screen = pygame.display.set_mode((width, height))

# Define as cores
white = (255, 255, 255)
black = (0, 0, 0)

# Cria a matriz 3x3 que representa o jogo da velha
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

# Define as variáveis que controlam a jogada atual e o vencedor
current_player = 1
winner = 0

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Verifica se o jogador clicou em alguma posição da tela
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Pega as coordenadas do clique
            x, y = event.pos
            # Verifica em qual posição da matriz o jogador clicou
            row = y // 200
            col = x // 200
            # Verifica se a posição está vazia
            if game[row][col] == 0:
                # Marca a jogada
                game[row][col] = current_player
                # Verifica se houve vencedor
                if (game[0][0] == game[1][1] == game[2][2] != 0 or
                    game[0][2] == game[1][1] == game[2][0] != 0):
                    winner = current_player
                for i in range(3):
                    if game[i][0] == game[i][1] == game[i][2] != 0:
                        winner = current_player
                    if game[0][i] == game[1][i] == game[2][i] != 0:
                        winner = current_player
                # Alterna o jogador
                current_player = 3 - current_player
    # Preenche a tela com a cor branca
    screen.fill(white)

    # Desenha as linhas do jogo da velha
    for i in range(1, 3):
        pygame.draw.line(screen, black, (200 * i, 0), (200 * i, 600))
        pygame.draw.line(screen, black, (0, 200 * i), (600, 200 * i))

    # Desenha as jogadas
    for row in range(3):
        for col in range(3):
                if game[row][col] == 1:
    # Desenha um X
                pygame.draw.line(screen, black, (col * 200 + 25, row * 200 + 25), (col * 200 + 175, row * 200 + 175))
                pygame.draw.line(screen, black, (col * 200 + 175, row * 200 + 25), (col * 200 + 25, row * 200 + 175))
                elif game[row][col] == 2:
    pygame.draw.circle(screen, black, (col * 200 + 100, row * 200 + 100), 75)
# Desenha um O
pygame.draw.circle(screen, black, (col * 200 + 100, row * 200 + 100), 75, 2)
# Verifica se houve vencedor
if winner != 0:
    # Escreve o vencedor na tela
    font = pygame.font.Font(None, 50)
    text = font.render("Player {} wins!".format(winner), True, black)
    screen.blit(text, (200, 400))

# Atualiza a tela
pygame.display.update()
# Finaliza o pygame
pygame.quit()