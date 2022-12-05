import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
screen.fill((0, 0, 0))
font = pygame.font.Font(None, 40)
blue = pygame.Color('dodgerblue')

# The clock is used to limit the frame rate
# and returns the time since last tick.
clock = pygame.time.Clock()
timer = 10  # Decrease this to count down.
dt = 0  # Delta time (time since last tick).



done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    timer -= dt
    if timer <= 0:
        txt = font.render('Game Over!', True, blue)
        timer = 10  # Reset it to 10 or do something else.
    else:
        txt = font.render(str(round(timer, 2)), True, blue)
        #print(timer)

    screen.fill((0, 0, 0))
    screen.blit(txt, (300, 0))
    pygame.display.flip()
    dt = clock.tick(30) / 1000  # / 1000 to convert to seconds.
