import pygame

pygame.init()


pygame.display.set_caption("7/10")
dirt = pygame.image.load('../images/tile_0034.png')
murk = pygame.image.load('../images/tile_0013.png')

dirt_rect = dirt.get_rect()
tile_size = dirt_rect.width

screen = pygame.display.set_mode((30*tile_size, 30*tile_size))
screen.fill((234, 0, 105))
screen_rect = screen.get_rect()
rows = screen_rect.height/tile_size
cols = screen_rect.width/tile_size

def draw_background():
    #Draw ocean on the screen
    for x in range(int(rows)):
        for y in range(int(cols)):
            screen.blit(dirt, (x*dirt_rect.height, y*dirt_rect.width))

while True:
    draw_background()
    pygame.display.flip()