import pygame

def main():
    crear_pantalla()

def crear_pantalla(): # + menu (despues lo saco)
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Cuida a tu salame")
    height= 600
    width = 800
    color = (255,255,255)
    font = pygame.font.Font("monogram-extended.ttf", 100)
    screen = pygame.display.set_mode((width, height))
    text_surface_salame = font.render('Cuida a tu salamín', True, color) #texto salame
    text_surface_play = font.render('Jugar',True,color) #texto play
    text_surface_options = font.render('Opciones',True,color) #texto options
    text_surface_credits = font.render('Creditos',True,color) #text credits

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        back = pygame.image.load("menu.jpg").convert()
        back_scale = pygame.transform.scale(back, (width, height))
        text_rect_salame = text_surface_salame.get_rect(center=(width//2, 100))
        text_rect_play = text_surface_play.get_rect(center=(width//2, 250))
        text_rect_options = text_surface_options.get_rect(center=(width//2, 350))
        text_rect_credits = text_surface_credits.get_rect(center=(width//2, 450))
    
        screen.blit(back_scale, (0, 0))
        screen.blit(text_surface_salame, text_rect_salame)
        screen.blit(text_surface_play, text_rect_play)
        screen.blit(text_surface_options, text_rect_options)
        screen.blit(text_surface_credits, text_rect_credits)


        pygame.draw.line(screen, color,
                        (text_rect_salame.left, text_rect_salame.bottom),
                        (text_rect_salame.right, text_rect_salame.bottom)
                        ,5)

        pygame.display.flip()

pygame.quit()


main()