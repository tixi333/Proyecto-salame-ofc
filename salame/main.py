import pygame

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


#ubicar y definir salame
sal = pygame.image.load("salame.png").convert_alpha() 
sal = pygame.transform.scale(sal, (400, 400))
sal_rect = sal.get_rect(center=(width // 2, height // 2))

#flecha derecha
arrowright = pygame.image.load("arrowright.png").convert_alpha()
arrowright = pygame.transform.scale(arrowright, (100, 100))
arrowright_rect = arrowright.get_rect()
arrowright_rect.centery = sal_rect.centery
arrowright_rect.left = sal_rect.right + 50

#flecha izquierda
arrowleft = pygame.image.load("arrowleft.png").convert_alpha()
arrowleft = pygame.transform.scale(arrowleft, (100, 100))
arrowleft_rect = arrowleft.get_rect()
arrowleft_rect.centery = sal_rect.centery
arrowleft_rect.right = sal_rect.left - 50

#especifico info
info_text = font.render("Presiona <i> para info", True, BLACK)
info_rect = info_text.get_rect()
info_rect.midtop = (width // 2, 0)



backgrounds = [YELLOW, BLUE, GREEN]
index = 0

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
                pass


    screen.fill(backgrounds[index])

    screen.blit(sal, sal_rect)
    screen.blit(arrowright, arrowright_rect)
    screen.blit(arrowleft, arrowleft_rect)
    screen.blit(info_text, info_rect)
    pygame.display.flip()



