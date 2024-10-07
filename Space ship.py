import pygame

screen = pygame.display.set_mode((700,700))
pygame.display.set_caption('Welcome to war!!')

space = pygame.image.load('images/background1.png')
redship1 = pygame.image.load('images/spaceship2.png')
yellowship2 = pygame.image.load('images/Spaceship1.png')

space = pygame.transform.scale(space,(700,700))
redship1 = pygame.transform.scale(redship1,(100,100))
redship1 = pygame.transform.rotate(redship1,90)

yellowship2 = pygame.transform.scale(yellowship2,(100,100))
yellowship2 = pygame.transform.rotate(yellowship2,270)

border = pygame.Rect(350,0,10,700)

def draw():
    screen.blit(space, (0,0))
    screen.blit(redship1, (red.x ,red.y))
    screen.blit(yellowship2,(yellow.x,yellow.y))
    pygame.draw.rect(screen,'black',border)
    pygame.display.update()

def red_movement():
    keys = pygame.key.get_pressed()
    if keys [pygame.K_w] and red.y > 0:     
        red.y = red.y - 4                                   
    if keys[pygame.K_s] and red.y < 600:
        red.y = red.y +4
    if keys[pygame.K_d] and red.x < 260:
        red.x = red.x +4
    if keys[pygame.K_a] and red.x > 0:
        red.x = red.x -4
    
def yellow_movement():






red = pygame.Rect(0,300,50,50)
yellow = pygame.Rect(0,300,50,50)
clock = pygame.time.Clock()

while True:
    clock.tick(60)

    draw()
    red_movement()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
