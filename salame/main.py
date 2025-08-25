import pygame

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height)) #seteo tamaño pantalla
WHITE=(245,246,252); BLACK=(30,30,35); GRAY=(100,105,115)
GREEN=(70,190,120); RED=(230,90,90); BLUE=(90,150,240)
YELLOW=(245,210,80); PURPLE=(160,120,220); DARK=(24,26,32)
ACCENT=(90,200,255)
pygame.display.set_caption("Cuida a tu salame")

#fondo
background = pygame.image.load("menu.jpg").convert()
background = pygame.transform.scale(background, (width, height))

#ubicar y definir salame
sal = pygame.image.load("salame.png").convert_alpha() 
sal = pygame.transform.scale(sal, (400, 400))
sal_rect = sal.get_rect(center=(width // 2, height // 2))

#flecha derecha
arrowright = pygame.image.load("arrowright.png").convert_alpha() 
arrowright = pygame.transform.scale(arrowright, (100, 100))
arrowright_rect = sal.get_rect()
arrowright_rect.topleft = (400, 700)

#flecha izquierda
arrowleft = pygame.image.load("arrowleft.png").convert_alpha() 
arrowleft = pygame.transform.scale(arrowleft, (100, 100))
arrowleft_rect = sal.get_rect()
arrowleft_rect.topleft = (400, 100)


running = True
while running:
    screen.fill(BLUE) 
    screen.blit(sal, sal_rect) 
    screen.blit(arrowright, arrowright_rect)
    screen.blit(arrowleft, arrowright_rect) 
    pygame.display.flip()



