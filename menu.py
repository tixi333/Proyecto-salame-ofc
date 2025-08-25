import pygame

def main():
    crear_pantalla()

def crear_pantalla(): # + menu (despues lo saco)
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Cuida a tu salame")
    
    height= 600
    width = 800 # medidas
    
    color = (255,255,255) ## Color font
    
    font = pygame.font.Font("monogram-extended.ttf", 100) #carga font
    
    screen = pygame.display.set_mode((width, height)) 
    
    ###text_surface_salame = font.render('Cuida a tu salamín', True, color) #texto salame
    
    back = pygame.image.load("menu.jpg").convert() #carga fondo
    back_scale = pygame.transform.scale(back, (width, height)) #convierte sus medidas a las de la pantalla

    title = pygame.image.load("play1.png")
    title_scale = pygame.transform.scale(title,(500,300))
    title_scale_rect = title_scale.get_rect(center= (width//2, 100))

    play1 = pygame.image.load("play1.png") #carga boton start
    play1_scale = pygame.transform.scale(play1, (200, 200)) #cambia sus medidas
    play1_scale_rect = play1_scale.get_rect(center=(width//2, height//2)) #rect del boton

    options1 = pygame.image.load("play1.png")
    options1_scale = pygame.transform.scale(options1,(200,200))
    options1_scale_rect = options1_scale.get_rect(center =(width//2, 500))

    credits1 = pygame.image.load("play1.png")
    credits1_scale = pygame.transform.scale(credits1,(200,200))
    credits1_scale_rect = options1_scale.get_rect(center= (width//2, 400))
    
    #general cross
    cross = pygame.image.load("cross.jpg")
    cross_scale=pygame.transform.scale(cross,(200,200))
    cros_scale_rect = cross_scale.get_rect(center= (width/2, 400))

    ####### credits screen

    credit_F = pygame.image.load("cross.jpg")
    credit_F_scale = pygame.transform.scale(credit_F, (200,200))
    credit_FS_rect = credit_F_scale.get_rect(center= (width//2,400))

    ###### option screen

    option_F = pygame.image.load("cross.jpg")
    optionsF_scale = pygame.transform.scale(option_F, (200,200))
    optionsF_scale_rect = optionsF_scale.get_rect(center = (width//2,400))


    run = True

    while run: #bucle principal
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and play1_scale_rect.collidepoint(event.pos):
                    print("play")
                elif event.button == 1 and options1_scale_rect.collidepoint(event.pos):
                    print("options")
                elif event.button == 1 and credits1_scale_rect.collidepoint(event.pos):
                    print("creditos")
    
        screen.blit(back_scale, (0, 0))
        screen.blit(title_scale,title_scale_rect)
        screen.blit(play1_scale, (play1_scale_rect))
        screen.blit(options1_scale, options1_scale_rect)
        screen.blit(credits1_scale, credits1_scale_rect)


        pygame.draw.line(screen, color,
                        (title_scale_rect.left, title_scale_rect.bottom),
                        (title_scale_rect.right, title_scale_rect.bottom)
                        ,5)

        pygame.display.flip()

pygame.quit()


main()