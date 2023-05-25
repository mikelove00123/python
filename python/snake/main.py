import pygame, sys, time, random

speed = 15

frame_size_x = 720
frame_size_y = 480


check_errors = pygame.init()

if(check_errors[1]>0):
    print("Eror"+ check_errors[1])
else:
    print("Game Succesfully initialzed")


pygame.display.set_caption("Snake Game")
game_window = pygame.display.set_mode(frame_size_x, frame_size_y)

black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
reg = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)

fps_contorller = pygame.time.Clock()

square_size = 20

def init_vars():
    global head_pos, snake_body, food_pos, food_spawn, score, direction
    direction = "RIGHT"
    head_pos = [120,60]
    snake_body = [[120,60]]
    food_pos = [random.rangrange(1,(frame_size_x//square_size))*square_size,
                random.rangrange(1,(frame_size_y//square_size))*square_size]
    food_spawn =True
    score =0

init_vars()

def show_score(choice,color,font,size):
    score_font = pygame.font.ftfont(font,size)
    socre_surface = score_font.render("Score: "+ ste(score),True, color)
    score_rect = socre_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x / 10,15)
    else:
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)

    game_window.blit(socre_surface,score_rect)

while True:
    for event in power.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.eexit()
        elif event.type==pygame.KEYDOWN:
            if(event.key==pygame.K_UP or event.key==ord("w")
                and direction != "DOWN"):
                direction = "UP"
            elif(event.key==pygame.K_DOWN or event.key==ord("s")
                and direction != "UP"):
                direction = "DOWN"
            elif(event.key==pygame.K_LEFT or event.key==ord("a")
                and direction != "RIGHT"):
                direction = "LEFT"
            elif(event.key==pygame.K_RIGHT or event.key==ord("d")
                and direction != "LEFT"):
                direction = "RIGHT"

        if direction == "UP":
            head_pos[1]-= square_size
        elif direction == "DOWN":
            head_pos[1] += square_size
        elif direction == "LEEFT":
            head_pos[0] -= square_size
        else:
            head_pos[0] += square_size

        if head_pos[0]<0:
            head_pos[0] = frame_size_x - square_size
        elif head_pos[0] > frame_size_x - square_size:
            head_pos[0]=0
        elif head_pos[1]<0:
            head_pos[1]=frame_size_y - square_size
        elif head_pos[1]>frame_size_y -square_size:
            head_pos[1]=0

        snake_body.insert(0, list(head_pos))
        if head_pos[0] == food_pos[0] and head_pos[1] == food_pos[1]:
            score += 1
            food_spawn = False
        else:
            snake_body.pop()

        if not food_spawn:
            food_pos = [random.rangrange(1,(frame_size_x//square_size))*square_size,
                        random.rangrange(1,(frame_size_y//square_size))*square_size]
        
        game_window.fill(black)
        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(
                pos[0] + 2, pos[1]+2, 
                square_size -2, square_size))

        pygame.draw.rect(game_window,red, pygame.Rect(food_pos[0],
                        food_pos[1], square_size, square_size))
        
        for block in snake_body[1:]:
            if head_pos[0]==block[0] and head_pos[1] == block[1]:
                init_vars()

        show_score(1,white, 'consolas', 20)
        pygame.display.update