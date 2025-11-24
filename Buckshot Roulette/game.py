import pygame
import random
from setup import init_pygame

init_pygame()

class GameState:
    def __init__(self):
        self.ronda = 1
        self.max_rondas = 5
        self.estado = "inicio"   # inicio / en_ronda / resultado / terminado
        
    def comenzar_ronda(self):
        if self.ronda == 1:
            self.estado = "ronda_1"
        elif self.ronda == 2:
            self.estado = "ronda_2"
        elif self.ronda == 3:
            self.estado = "ronda_3"

        self.round_start_time = pygame.time.get_ticks()
        self.circle_on = True
        
    def siguiente_ronda(self):
        if self.ronda < self.max_rondas:
            self.ronda += 1
            self.estado = "en_ronda"
        else:
            self.estado = "terminado"
            
def draw_text_input(screen, font, text, input_box, color):
   
    txt_surface = font.render(text, True, (255, 255, 255))
    input_box.w = max(300, txt_surface.get_width() + 10)
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 10))
    pygame.draw.rect(screen, color, input_box, 3)

def handle_text_input(event, text, active):

    if event.type == pygame.KEYDOWN and active:
        if event.key == pygame.K_BACKSPACE:
            return text[:-1]
        elif event.key == pygame.K_RETURN:
            print("Nombre escrito:", text)
            return text, True
        else:
            return text + event.unicode, False

    return text, False

def run_game(screen,resources):
    game_state = GameState()
    font = pygame.font.Font(None, 40)

    # Caja de texto
    input_box = pygame.Rect(150, 150, 300, 50)
    color_inactive = pygame.Color('gray')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ""
    
    if not loading_screen(screen,resources,frame_index=0):
        return False
    
    frame_index = 0
    frame_delay = 150
    last_update = pygame.time.get_ticks() 
    running = True
    gr_x = -200
    finished = False
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos) and not finished:
                    active = True
                else:
                    active = False
                color = color_active if active else color_inactive

            
            text, submit = handle_text_input(event, text, active)
            
            if submit :
                active = False
                finished = True
                
        current_time = pygame.time.get_ticks()
        if current_time - last_update > frame_delay:
            frame_index = (frame_index + 1) % len(resources["idle_sprites"])
            last_update = current_time      
            
        game_state = actualizar_logica(game_state, finished)
        
        screen.fill((0, 0, 0))  # fondo
        if gr_x < 100:       
            gr_x += 1
        
        
        dibujar_estado(screen, game_state ,resources,frame_index,gr_x,finished)
        if not finished:
            input_box.x = gr_x + resources["gr"].get_width() + 20
            input_box.y = 400

            draw_text_input(screen, font, text, input_box, color)
       
        pygame.display.flip()

        
def loading_screen(screen,resources,frame_index):
    
    BLACK = (0, 0, 0)
    DURATION = 3000  # 3 segundos
    start = pygame.time.get_ticks()
    
    
    while pygame.time.get_ticks() - start < DURATION:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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

def actualizar_logica(game_state, finished):
    if finished and game_state.estado == "inicio":
            game_state.comenzar_ronda()
            
            game_state.round_start_time = pygame.time.get_ticks()
            game_state.blink_duration = 2000  # 2 segundos
            game_state.blink_speed = 200      # cada 200 ms cambia
            game_state.circle_on = True
            
    elif game_state.estado in ("ronda_1", "ronda_2", "ronda_3"):
        elapsed = pygame.time.get_ticks() - game_state.round_start_time
        
        if elapsed < game_state.blink_duration:
            # cada 200 ms alterna
            if (elapsed // game_state.blink_speed) % 2 == 0:
                game_state.circle_on = True
            else:
                game_state.circle_on = False
        else:
            game_state.circle_on = False  # termina el parpadeo

    return game_state

def dibujar_estado(screen, game_state,resources,frame_index,gr_x,finished):
    screen.blit(resources["background_g"], (0, 0))
    screen.blit(resources["idle_sprites"][frame_index], (300, 175))
    if not finished:
        screen.blit(resources["gr"], (gr_x, 400))
    
    if game_state.estado in ("ronda_1", "ronda_2", "ronda_3"):
        if game_state.circle_on:
            num_circles = 3
            circle_radius = 10
            gap = 20
            total_width = num_circles * circle_radius*2 + (num_circles-1)*gap
            start_x = (800 - total_width) // 2 + circle_radius
            y = 25  # altura

            # Dibujar los 3 círculos vacíos
            for i in range(3):
                pygame.draw.circle(
                    screen,
                    (255, 255, 255),
                    (start_x + i * (circle_radius*2 + gap), y),
                    circle_radius,
                    2  # borde
                )
            
            # Si el primero está parpadeando: rellenarlo
            if game_state.circle_on:
                if game_state.estado == "ronda_1":
                    count = 1
                elif game_state.estado == "ronda_2":
                    count = 2
                else:
                    count = 3
                for i in range(count):
                    pygame.draw.circle(screen, (255, 255, 255), (start_x + i * (circle_radius*2 + gap), y), circle_radius -2)
        else:
            if game_state.estado == "ronda_1":
                screen.blit(resources["bala_n"], (375, 300))
                screen.blit(resources["bala_v"], (425, 300))