import pygame, os

#seteo inicial
pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height)) #seteo tamaño pantalla
#colores
WHITE=(245,246,252); BLACK=(30,30,35); GRAY=(100,105,115)
GREEN=(70,190,120); RED=(230,90,90); BLUE=(90,150,240)
YELLOW=(245,210,80); PURPLE=(160,120,220); DARK=(24,26,32)
ACCENT=(90,200,255)
pygame.display.set_caption("Cuida a tu salame")
pygame.display.set_icon(pygame.image.load("salame.png").convert_alpha())
font = pygame.font.Font("monogram-extended.ttf", 36)


class salame:
    def __init__(self):
        self.health = 100
        self.happiness = 100
        self.image = pygame.image.load("salame.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (400, 400))
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class food:
    def __init__(self, name, health, image_path):
        self.name = name
        self.health = health
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (width // 2 , height)
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def feed(self):
        salame.health = salame.health + self.health
        if salame.health > 100:
            salame.health = 100
    


#flechas derechas
arrowright = pygame.image.load("arrowright.png").convert_alpha()
arrowright_bottom = pygame.transform.scale(arrowright, (40, 40))
arrowright = pygame.transform.scale(arrowright, (100, 100))
arrowright_back_rect = arrowright.get_rect()
arrowright_back_rect.center = (width // 2, height // 2)
arrowright_back_rect.left = arrowright_back_rect.right + 200
arrowright_bottom_rect = arrowright_bottom.get_rect()
arrowright_bottom_rect.midbottom = (width // 2 + 40, height)


#flechas izquierdas
arrowleft = pygame.image.load("arrowleft.png").convert_alpha()
arrowleft_bottom = pygame.transform.scale(arrowleft, (40, 40))
arrowleft = pygame.transform.scale(arrowleft, (100, 100))
arrowleft_back_rect = arrowleft.get_rect()
arrowleft_back_rect.center = (width // 2, height // 2)
arrowleft_back_rect.right = arrowleft_back_rect.left - 200
arrowleft_bottom_rect = arrowleft_bottom.get_rect()
arrowleft_bottom_rect.midbottom = (width // 2 - 40, height)

#básicamente, el texto de presiona i para info
info_text = font.render("Presiona <i> para info", True, BLACK)
info_rect = info_text.get_rect()
info_rect.midtop = (width // 2, 0)

#texto info 
i_text = font.render("iahygfjhjsgjhb", True, BLACK)
i_rect = i_text.get_rect()
i_rect.center = (width // 2, height // 2)
show_info = False

backgrounds = [YELLOW, BLUE, GREEN]
index = 0

salame = salame()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                index = (index - 1) % len(backgrounds)
            elif event.key == pygame.K_RIGHT:
                index = (index + 1) % len(backgrounds)
            elif event.key == pygame.K_i:
                show_info = not show_info
                       
    if show_info:
        screen.fill(WHITE)
        screen.blit(i_text, i_rect)
    else:
        screen.fill(backgrounds[index])
        salame.draw(screen)
        screen.blit(arrowright, arrowright_back_rect)
        screen.blit(arrowleft, arrowleft_back_rect)
        screen.blit(info_text, info_rect)
        if backgrounds[index] == BLUE:
            
            screen.blit(arrowright_bottom, arrowright_bottom_rect)
            screen.blit(arrowleft_bottom, arrowleft_bottom_rect)
            

    pygame.display.flip()



