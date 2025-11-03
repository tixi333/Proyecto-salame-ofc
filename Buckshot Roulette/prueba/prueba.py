

import pygame
import sys
import os
import random


pygame.init()
pygame.font.init()


ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Buckshot Roulette - Demo")
font = pygame.font.Font("monogram-extended.ttf", 30)

black = (0, 0, 0)
grey = (128, 128, 128)
red = (139, 0, 0)


mesa = pygame.image.load("Buckshot Roulette\\prueba\\mesa_bs.png")
mesa_scale = pygame.transform.scale(mesa, (800, 600))

inventory_dealer = pygame.image.load("Buckshot Roulette\\prueba\\inventory.png")
inventory_dealer = pygame.transform.scale(inventory_dealer, (228, 123))

inventory_player = pygame.image.load("Buckshot Roulette\\prueba\\inventory.png")
inventory_player = pygame.transform.scale(inventory_player, (228, 123))


actual_animation = "idle"


def cargar_frames(ruta_frames):
    frames = []
    for archivo in sorted(os.listdir(ruta_frames)):
        if archivo.endswith(".png"):
            imagen = pygame.image.load(os.path.join(ruta_frames, archivo)).convert_alpha()
            imagen = pygame.transform.scale(imagen, (200, 200))
            frames.append(imagen)
    return frames


def cambiar_animacion(nueva_animacion):
    global actual_animation, frames, indice_frame, ruta_frames
    if actual_animation != nueva_animacion:
        actual_animation = nueva_animacion
        ruta_frames = f"Buckshot Roulette\\prueba\\{nueva_animacion}"
        frames = cargar_frames(ruta_frames)
        indice_frame = 0


ruta_frames = "Buckshot Roulette\\prueba\\idle"
frames = cargar_frames(ruta_frames)


indice_frame = 0
velocidad_anim = 0.12
reloj = pygame.time.Clock()

current_life_dealer = 3
current_life_player = 3

text_current_life_dealer = font.render("Current life:", True, grey)
text_current_life_player = font.render("Current life:", True, grey)
text_3 = font.render("3", True, red)
text_2 = font.render("2", True, red)
text_1 = font.render("1", True, red)

text_dealer_dead = font.render("Dealer is dead", True, red)

inventory_on = False

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                current_life_dealer -= 1
                if current_life_dealer < 1:
                    current_life_dealer = 0

            if evento.key == pygame.K_e:
                inventory_on = not inventory_on

  
    pantalla.blit(mesa_scale, (0, 0))
    if current_life_dealer == 0:
        pantalla.fill(black)
        pantalla.blit(text_dealer_dead, (200, 200))
    if current_life_dealer == 1:
        cambiar_animacion("bleeding")
        pantalla.blit(text_1, (170, 120))
        
    elif current_life_dealer == 2:
        cambiar_animacion("idle")
        pantalla.blit(text_2, (170, 120))
    else:
        cambiar_animacion("idle")
        pantalla.blit(text_3, (170, 120))
 
    pantalla.blit(frames[int(indice_frame)], (300, 150))
    pantalla.blit(inventory_dealer, (0, 0))
    pantalla.blit(text_current_life_dealer, (20, 120))
    
    if inventory_on:
        pantalla.blit(inventory_player, (0, 480))
        pantalla.blit(text_current_life_player, (20, 450))
        if current_life_player == 1:
            pantalla.blit(text_1, (170, 450))
        elif current_life_player == 2:
            pantalla.blit(text_2, (170, 450))
        else:
            pantalla.blit(text_3, (170, 450))
    
    indice_frame += velocidad_anim
    if indice_frame >= len(frames):
        indice_frame = 0  
    
    pygame.display.flip()
    reloj.tick(60)
