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

random_up_or_down = random.randint(0, 1)

def get_ball_y_vel(x): # not using an int, see if it works!
        y = math.sqrt(49 - x**2)
        return y

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
    
    
    ball_x_vel = random.randint(-5, -1)
    if random_up_or_down == 0:
        ball_y_vel = get_ball_y_vel(ball_x_vel)
    elif random_up_or_down == 1:
        ball_y_vel = get_ball_y_vel(ball_x_vel) * -1
    

    while run:
    
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

        if right_score ==5:
            pygame.display.update()
            WIN.blit(right_wins_label, (180, HEIGHT/2))
            pygame.display.update()
            pygame.time.delay(5000)
            break
        
        if left_score == 5:
            pygame.display.update()
            WIN.blit(left_wins_label, (180, HEIGHT/2))
            pygame.display.update()
            pygame.time.delay(5000)
            break

        if pygame.Rect.colliderect(ball, right_player):         
        
            ball_x_vel = 0
            ball_x_vel = -5
            
        if pygame.Rect.colliderect(ball, left_player):                
            ball_x_vel = 0
            ball_x_vel = 5
            
        if ball_y_position <= 0:
            ball_y_vel *= -1
        if ball_y_position >= HEIGHT:
            ball_y_vel *= -1

        if ball_x_position <= 0:
            right_score += 1
           
            
            if serve_counter % 2 == 0:
                ball_x_vel = -5
            else:
                ball_x_vel = 5
            serve_counter += 1
            ball_x_position = (WIDTH/2 - 7)
            ball_y_position = random.randint(0, HEIGHT)
            ball_x_position += ball_x_vel
            ball_y_position += ball_y_vel
                   
               
        if ball_x_position >= WIDTH:
            left_score += 1
           
            
            if serve_counter % 2 == 0:
                ball_x_vel = -5
            else:
                ball_x_vel = 5
            serve_counter += 1
            ball_x_position = (WIDTH/2 - 7)
            ball_y_position = random.randint(0, HEIGHT)
            ball_x_position += ball_x_vel
            ball_y_position += ball_y_vel
            
            
        pygame.display.update()
    
    
        
    pygame.quit()


if __name__ == "__main__":
    main()
