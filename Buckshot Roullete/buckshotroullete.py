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
# ------------------- load images background gif ----------------------
zero = pygame.image.load("1.png").convert()
zero_scale = pygame.transform.scale(zero,(width,height))

one = pygame.image.load("1.png").convert()
one_scale = pygame.transform.scale(one,(width,height))

two= pygame.image.load("1.png").convert()
two_scale = pygame.transform.scale(two,(width,height))

three = pygame.image.load("1.png").convert()
three_scale = pygame.transform.scale(three,(width,height))

four = pygame.image.load("1.png").convert()
four_scale = pygame.transform.scale(four,(width,height))

five = pygame.image.load("1.png").convert()
five_scale = pygame.transform.scale(five,(width,height))

six = pygame.image.load("1.png").convert()
six_scale = pygame.transform.scale(one,(width,height))

seven = pygame.image.load("1.png").convert()
seven_scale = pygame.transform.scale(one,(width,height))

eight = pygame.image.load("1.png").convert()
eight_scale = pygame.transform.scale(one,(width,height))

nine = pygame.image.load("1.png").convert()
nine_scale = pygame.transform.scale(one,(width,height))

one = pygame.image.load("1.png").convert()
one_scale = pygame.transform.scale(one,(width,height))

one = pygame.image.load("1.png").convert()
one_scale = pygame.transform.scale(one,(width,height))

one = pygame.image.load("1.png").convert()
one_scale = pygame.transform.scale(one,(width,height))

one = pygame.image.load("1.png").convert()
one_scale = pygame.transform.scale(one,(width,height))

one = pygame.image.load("1.png").convert()
one_scale = pygame.transform.scale(one,(width,height))

one = pygame.image.load("1.png").convert()
one_scale = pygame.transform.scale(one,(width,height))

one = pygame.image.load("1.png").convert()
one_scale = pygame.transform.scale(one,(width,height))

one = pygame.image.load("1.png").convert()
one_scale = pygame.transform.scale(one,(width,height))

one = pygame.image.load("1.png").convert()
one_scale = pygame.transform.scale(one,(width,height))

one = pygame.image.load("1.png").convert()
one_scale = pygame.transform.scale(one,(width,height))

one = pygame.image.load("1.png").convert()
one_scale = pygame.transform.scale(one,(width,height))
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
        screen.blit(zero_scale, (0,0))
    pygame.display.flip()

pygame.quit()