import pygame
from paddle import Paddle
from const import *
from ball import Ball

# pygame components
clock  = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE) 
quit   = False
font   = None

# game components
## right paddle
paddle_right        = Paddle(WHITE, 10, 100)
paddle_right.rect.x = 20
paddle_right.rect.y = 200

## left paddle
paddle_left        = Paddle(WHITE, 10, 100)
paddle_left.rect.x = 670
paddle_left.rect.y = 200

## ball
ball        = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

## list of all sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(paddle_left)
all_sprites.add(paddle_right)
all_sprites.add(ball)

## scores
score_left  = 0
score_right = 0

# initialize
def init():
    pygame.init()
    pygame.display.set_caption("Pong!")

def init_screen():
    global font
    
    font = pygame.font.Font(None, 60)
    screen.fill(BLACK)

    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    pygame.display.flip()
    clock.tick(60)

def reset():
    ball.rect.x = 345
    ball.rect.y = 195
    ball.reset()

    paddle_left.rect.x = 670
    paddle_left.rect.y = 200
    paddle_right.rect.x = 20
    paddle_right.rect.y = 200


# main loops
def main():
    init()
    init_screen()
    # main loop
    while not quit:
        graphics_loop(screen)
        input_loop(pygame.key.get_pressed())
        physics_loop()
        event_loop(pygame.event.get())
    print("quit")
    pygame.quit()

def event_loop(events):
    for e in events:
        # quit
        if e.type == pygame.QUIT:
            global quit
            quit = True
        
def input_loop(keys):
    if keys[pygame.K_r]:
        reset()
    if keys[pygame.K_UP]:
        paddle_left.move_up(SPEED)
    elif keys[pygame.K_DOWN]:
        paddle_left.move_down(SPEED)
    if keys[pygame.K_w]:
        paddle_right.move_up(SPEED)
    elif keys[pygame.K_s]:
        paddle_right.move_down(SPEED)
    if keys[pygame.K_a]:
        ball.update()

def physics_loop():
    global score_left, score_right

    ball.update()
    
    if ball.rect.x >= 690:
        score_left += 1
        reset()
    elif ball.rect.x <= 0:
        score_right += 1
        reset()
    # ball bounces off wall
    if ball.rect.x >= 690 or ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y >= 490 or ball.rect.y <= 0:
        ball.velocity[1] = -ball.velocity[1]


    if pygame.sprite.collide_mask(ball, paddle_left) or pygame.sprite.collide_mask(ball, paddle_right):
        ball.bounce()

def graphics_loop(screen):
    # reset screen
    screen.fill(BLACK)
    # draw the field
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    # draw the sprites
    all_sprites.draw(screen)

    global font
    text = font.render(str(score_left), 1, WHITE)
    screen.blit(text, (250, 10))
    text = font.render(str(score_right), 1, WHITE)
    screen.blit(text, (420, 10))

    # update screen
    pygame.display.flip()
    clock.tick(60)

if __name__ == "__main__":
    main()
