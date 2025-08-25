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
    
    text_surface_salame = font.render('Cuida a tu salamín', True, color) #texto salame
    text_surface_options = font.render('Opciones',True,color) #texto options
    text_surface_credits = font.render('Creditos',True,color) #text credits
    
    back = pygame.image.load("menu.jpg").convert() #carga fondo
    back_scale = pygame.transform.scale(back, (width, height)) #convierte sus medidas a las de la pantalla
    
    text_rect_salame = text_surface_salame.get_rect(center=(width//2, 100)) #rect del texto
    text_rect_options = text_surface_options.get_rect(center=(width//2, 350)) #rect del texto options
    text_rect_credits = text_surface_credits.get_rect(center=(width//2, 450)) #rect del texto credits
        
    play1 = pygame.image.load("play1.png") #carga boton start
    play1_scale = pygame.transform.scale(play1, (200, 100)) #cambia sus medidas
    play1_width = play1_scale.get_width() #saca el ancho de la imagen
    play1_height = play1_scale.get_height() #saca el alto de la imagen
    x_start = (width - play1_width) // 2 #sirve para cambiar su ubicacion despues
    y_start = (height - play1_height) // 2 #lo mismo de arriba
    play1_scale_rect = play1_scale.get_rect(center=(width//2, height//2)) #rect del boton


    run = True

    while run: #bucle principal
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and play1_scale_rect.collidepoint(event.pos):
                    print("prueba")
    
        screen.blit(back_scale, (0, 0))
        screen.blit(play1_scale, (play1_scale_rect))
        screen.blit(text_surface_salame, text_rect_salame)
        screen.blit(text_surface_options, text_rect_options)
        screen.blit(text_surface_credits, text_rect_credits)


        pygame.draw.line(screen, color,
                        (text_rect_salame.left, text_rect_salame.bottom),
                        (text_rect_salame.right, text_rect_salame.bottom)
                        ,5)

        pygame.display.flip()

pygame.quit()


main()