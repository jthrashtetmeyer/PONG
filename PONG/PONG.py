import pygame
import time
import random
import math
pygame.font.init()

WIDTH, HEIGHT = 750, 690

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("PONG")

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0, 255, 0)

FPS = 60

def get_ball_x_vel(x):
    xv = random.randint(-5, -2)
    return xv
        

def get_ball_y_vel(x): 
    y = math.sqrt(49 - x**2)
    random_up_or_down = random.randint(0,1)
    if random_up_or_down == 1:
        y *= -1
    return y
def get_bounced_y_vel(y):
    y *= -1
    return y
"""I need to create a serve function that handles both the beginning of the game and every time the loop starts over once a player has scored.
the hard part is that it's coded into the main function using variables that are defined and used elsewhere,
so I'll have to move things around and think about whether I need any variables to be global??"""
#def serve():

def main():
    run = True
    
    clock = pygame.time.Clock()

    left_player_height = HEIGHT/2 - 25
    right_player_height = HEIGHT/2 - 25
    left_score = 0
    right_score = 0
    score_font = pygame.font.SysFont("couriernew", 150)
    winner_font = pygame.font.SysFont("couriernew", 50)

    starting_ball_height = random.randint(0, HEIGHT)
    ball_x_position = (WIDTH/2 - 7)
    ball_y_position = starting_ball_height
    serve_counter = 1 

    ball_x_vel = get_ball_x_vel(ball_x_position)
    ball_y_vel = get_ball_y_vel(ball_x_vel)
    
    

    while run:
        hit = False
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and left_player_height > 0:
            left_player_height -= 7
        if keys[pygame.K_s] and left_player_height < HEIGHT - 75:
            left_player_height += 7
        if keys[pygame.K_UP] and right_player_height > 0:
            right_player_height -= 7
        if keys[pygame.K_DOWN] and right_player_height < HEIGHT - 75:
            right_player_height += 7

        
        WIN.fill(BLACK)

        left_label = score_font.render(str(left_score), 1, WHITE)
        right_label = score_font.render(str(right_score), 1, WHITE)
        left_wins_label = winner_font.render("Player 1 wins!", 1, GREEN)
        right_wins_label = winner_font.render("Player 2 wins!", 1, GREEN)
        
        WIN.blit(left_label, (140, 10))
        WIN.blit(right_label, (WIDTH - 230, 10))
        
        left_player = pygame.draw.rect(WIN, WHITE, (0, left_player_height, 15, 75))
        right_player = pygame.draw.rect(WIN, WHITE, (WIDTH - 15, right_player_height, 15, 75))

        pygame.draw.rect(WIN, WHITE, pygame.Rect(WIDTH/2 -7, 0, 15, HEIGHT))
        
        ball = pygame.draw.rect(WIN, RED, pygame.Rect(ball_x_position, ball_y_position, 15, 15))

        
        ball_x_position += ball_x_vel
        ball_y_position += ball_y_vel

        if right_score == 5 or left_score == 5:
            if right_score == 5:
                WIN.blit(right_wins_label, (180, HEIGHT/2))
            else:
                WIN.blit(left_wins_label, (180, HEIGHT/2))
            pygame.display.update()
            pygame.time.delay(5000)
            break

        if pygame.Rect.colliderect(ball, right_player):
            ball_x_vel = 0
            ball_x_vel = -5
        elif pygame.Rect.colliderect(ball, left_player):
            ball_x_vel = 0
            ball_x_vel = 5
        
            
        
            
        if ball_y_position <= 0 or ball_y_position >= HEIGHT:
            ball_y_vel = get_bounced_y_vel(ball_y_vel)

        if ball_x_position <= 0 or ball_x_position >= WIDTH:
            if ball_x_position <= 0:
                right_score += 1
            elif ball_x_position >= WIDTH:
                left_score += 1
            serve_counter += 1
            ball_x_position = (WIDTH/2 - 7)
            ball_y_position = random.randint(0, HEIGHT)
            ball_x_position += ball_x_vel
            ball_y_position += ball_y_vel
            if serve_counter % 2 == 0:
                    ball_x_vel = -5
            else:
                    ball_x_vel = 5
        
            
        pygame.display.update()
    
    
        
    pygame.quit()


if __name__ == "__main__":
    main()
