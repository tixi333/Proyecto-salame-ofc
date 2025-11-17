import pygame
import random
from setup import init_pygame

init_pygame()


def run_game(screen,resources):
    
    if not loading_screen(screen,resources,frame_index=0):
        return
    
    frame_index = 0
    frame_delay = 150
    last_update = pygame.time.get_ticks() 
    running = True
    gr_x = -200
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        current_time = pygame.time.get_ticks()
        if current_time - last_update > frame_delay:
            frame_index = (frame_index + 1) % len(resources["idle_sprites"])
            last_update = current_time      
            
        estado = actualizar_logica()  # llama a las rondas
        
        screen.fill((0, 0, 0))  # fondo
        if gr_x < 100:       
            gr_x += 1
        dibujar_estado(screen,estado ,resources,frame_index,gr_x)
        
        pygame.display.flip()
        
def loading_screen(screen,resources,frame_index):
    
    BLACK = (0, 0, 0)
    DURATION = 3000  # 3 segundos
    start = pygame.time.get_ticks()
    
    
    while pygame.time.get_ticks() - start < DURATION:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        screen.fill(BLACK)
        pygame.display.flip()
    fade_surface = pygame.Surface(screen.get_size())
    fade_surface.fill(BLACK)

    frame_delay = 150
    last_update = pygame.time.get_ticks()
    frame_index_local = frame_index

    for alpha in range(255, -1, -4): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        current_time = pygame.time.get_ticks()
        if current_time - last_update > frame_delay:
            frame_index_local = (frame_index_local + 1) % len(resources["idle_sprites"])
            last_update = current_time

        screen.blit(resources["background_g"], (0, 0))

        screen.blit(resources["idle_sprites"][frame_index_local], (300, 175))

        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))

        pygame.display.flip()
        pygame.time.delay(20)
    
    

    return True

def actualizar_logica():
    pass

def dibujar_estado(screen, estado,resources,frame_index,gr_x):
    screen.blit(resources["background_g"], (0, 0))
    screen.blit(resources["idle_sprites"][frame_index], (300, 175))
    screen.blit(resources["gr"], (gr_x, 400))



#estado = 1(1p,turnos,2p) 2()
#fade_surface = pygame.Surface(screen.get_size())
 #   fade_surface.fill(BLACK)

  #  for alpha in range(255, -1, -2):  # suavidad del fade
   #     screen.blit(resources["idle_sprites"][frame_index], (300, 175))
    #    screen.blit(resources["background_g"], (0, 0))
     #   fade_surface.set_alpha(alpha)
      #  screen.blit(fade_surface, (0, 0))
       # pygame.display.flip()
        #pygame.time.delay(25) # velocidad del fade