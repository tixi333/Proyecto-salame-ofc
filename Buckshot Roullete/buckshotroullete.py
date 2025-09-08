import pygame

height = 600
width = 800
black = (0,0,0)
grey = (128,128,128)
pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Buckshot Roullete")
font = pygame.font.Font("monogram-extended.ttf", 40) 

text_enter = font.render("Press enter to start", True, grey)

class Button:
    def __init__(self):
        pass
    def handle_event(self):
        pass
    def draw_button(self):
        pass

running = True
actual_screen = "main_screen"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if actual_screen:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    actual_screen = "menu_screen"
    if actual_screen == "main_screen":
        screen.fill(black)
        screen.blit(text_enter,(250,500))
    elif actual_screen == "menu_screen":
        screen.fill(grey)
    pygame.display.flip()

pygame.quit()