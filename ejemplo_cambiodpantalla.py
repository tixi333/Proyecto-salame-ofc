import pygame

pygame.init()
pygame.font.init()
pygame.display.set_caption("Prueba cambio de pantalla")
white = (255,255,255)
black =(0,0,0)
width, height = 600 , 800
font = pygame.font.Font("monogram-extended.ttf", 100)

text_play = font.render("play screen", True, white)
play_rect = text_play.get_rect(center = (width //2 , height //2))

text_options = font.render("options screen", True, white)
options_rect = text_options.get_rect(center = (width //2, height //2))

text_credits = font.render("credits screen",True, white)
credits_rect = credits.get_rect(center = (width //2 , height//2 ))

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