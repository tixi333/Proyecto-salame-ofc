import pygame

pygame.init()
pygame.font.init()
pygame.display.set_caption("Prueba cambio de pantalla")
white = (255,255,255)
black =(0,0,0)
width, height = 600 , 800
font = pygame.font.Font("monogram-extended.ttf", 100)

text_play = font.render("play screen", True, white)

text_options = font.render("options screen", True, white)


text_credits = font.render("credits screen",True, white)


screen = pygame.display.set_caption(width,height)
screen.fill(black)

states = ["menu",
          "play",
          "options",
          "credits"]
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass

pygame.display.flip()