from settings import *
from player import *
import time

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.Font(None, 36)

running = True
clock = pygame.time.Clock()

rock_players = [player_object('rock') for _ in range(n_player)]
paper_players = [player_object('paper') for _ in range(n_player)]
scissor_players = [player_object('scissor') for _ in range(n_player)]

flag = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        

    win.fill(SCREEN_COLOR)


    for i in range(n_player):
        rock_players[i].draw(win)
        paper_players[i].draw(win)
        scissor_players[i].draw(win)

        while(flag):
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        flag = False
        
        rock_players[i].move()
        paper_players[i].move()
        scissor_players[i].move()

        collision_matrix_1 = [[l2_norm(rock_players[i], paper_players[j]) for j in range(n_player)] for i in range(n_player)]
        collision_matrix_2 = [[l2_norm(paper_players[i], scissor_players[j]) for j in range(n_player)] for i in range(n_player)]
        collision_matrix_3 = [[l2_norm(scissor_players[i], rock_players[j]) for j in range(n_player)] for i in range(n_player)]

        kill(collision_matrix_1, rock_players, 'paper')
        kill(collision_matrix_2, paper_players, 'scissor')
        kill(collision_matrix_3, scissor_players, 'rock')


    pygame.display.flip()

pygame.quit()
