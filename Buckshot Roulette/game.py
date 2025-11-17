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

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        current_time = pygame.time.get_ticks()
        if current_time - last_update > frame_delay:
            frame_index = (frame_index + 1) % len(resources["idle_sprites"])
            last_update = current_time      
            
        # --- LÓGICA ---
        estado = actualizar_logica()  # llama a tus rondas
        # ejemplo: estado = ronda_1()

        # --- DIBUJO ---
        screen.fill((0, 0, 0))  # fondo
        dibujar_estado(screen,estado ,resources,frame_index)

        pygame.display.flip()
        
def loading_screen(screen,resources,frame_index):
    """Pantalla negra de carga durante 3 segundos con fade-in al juego."""
    BLACK = (0, 0, 0)
    DURATION = 3000  # 3 segundos
    start = pygame.time.get_ticks()

    # --- Pantalla negra 3 segundos ---
    while pygame.time.get_ticks() - start < DURATION:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        screen.fill(BLACK)
        pygame.display.flip()

    # --- Fade-in del fondo ---
    fade_surface = pygame.Surface(screen.get_size())
    fade_surface.fill(BLACK)

    for alpha in range(255, -1, -2):  # suavidad del fade
        screen.blit(resources["idle_sprites"][frame_index], (300, 175))
        screen.blit(resources["background_g"], (0, 0))
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(25) # velocidad del fade

    return True

def actualizar_logica():
    pass

def dibujar_estado(screen, estado,resources,frame_index):
    screen.blit(resources["background_g"], (0, 0))
    screen.blit(resources["idle_sprites"][frame_index], (300, 175))

