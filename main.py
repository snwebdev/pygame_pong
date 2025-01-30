# this is the main file

import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

my_bat_length = 100
my_bat_width = 20
my_bat_x = 80
my_bat_y = (screen.get_height() - my_bat_length) / 2

his_bat_length = 100
his_bat_width = 20
his_bat_x = screen.get_width() - my_bat_width - my_bat_x
his_bat_y = (screen.get_height() - his_bat_length) / 2

ball_length = 20
ball_width = 20
ball_x = (screen.get_width() - ball_width) /2
ball_y = (screen.get_height() - ball_length) / 2
ball_speed = 2
ball_dx = 1
ball_dy = 0

serve = "him"
my_score = 0
his_score = 0

def point_to_me():
    my_score += 1
    print("my score =", my_score)
    
def point_to_him():
    his_score += 1
    print("his score =", his_score)



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("black")
    
    pygame.draw.rect(screen, "white", [my_bat_x, my_bat_y, my_bat_width, my_bat_length], 0)
    pygame.draw.rect(screen, "white", [his_bat_x, his_bat_y, his_bat_width, his_bat_length], 0)
    pygame.draw.rect(screen, "white", [ball_x, ball_y, ball_width, ball_length], 0)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        my_bat_y -= 300 *dt
    if keys[pygame.K_s]:
        my_bat_y += 300 *dt
    # if keys[pygame.K_a]:
    #     player_pos.x -= 300 *dt
    # if keys[pygame.K_d]:
    #     player_pos.x += 300 *dt
    
    ball_x = ball_x + (ball_dx * ball_speed)
    ball_y = ball_y + (ball_dy * ball_speed)
    
    if ball_x + ball_width >= his_bat_x:
        if ball_y >= his_bat_y and ball_y <= his_bat_y + his_bat_length:
            ball_dx *= -1
            
    if ball_x <= my_bat_x + my_bat_width:
        if ball_y >= my_bat_y and ball_y <= my_bat_y + my_bat_length:
            ball_dx *= -1
            
    if ball_x > screen.get_width():
       point_to_me()  
    if ball_x + ball_width < 0:
       point_to_him()   
    
        
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000
    
    
    
pygame.quit()
 

          
        