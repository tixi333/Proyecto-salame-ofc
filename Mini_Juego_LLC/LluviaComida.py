import pygame
import sys
import random

pygame.init()

# Tamaño pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Salame")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

# Fuentes
fuente = pygame.font.SysFont("Arial", 30)
fuente_grande = pygame.font.SysFont("Arial", 60)

# Reloj
clock = pygame.time.Clock()
FPS = 60

# Jugador
jugador_img = pygame.image.load('salame.png').convert_alpha()
jugador_img = pygame.transform.scale(jugador_img, (75, 75))
jugador_rect = jugador_img.get_rect()
jugador_rect.topleft = (100, 100)

# Movimiento
velocidad_x = 0
velocidad_y = 0
gravedad = 0.5
salto = -10
en_suelo = False
velocidad_movimiento = 5

# Suelo
suelo = pygame.Rect(0, ALTO - 50, ANCHO, 50)

# Comidas buenas
comidas_imgs = [
    pygame.transform.scale(pygame.image.load(f"comida{i+1}.png").convert_alpha(), (40, 40))
    for i in range(4)
]

# Comida mala
comida_mala_img = pygame.transform.scale(pygame.image.load("comida_mala.png").convert_alpha(), (40, 40))

# Crear comidas
comidas = []
for img in comidas_imgs:
    x = random.randint(0, ANCHO - 40)
    y = random.randint(-600, -40)
    rect = img.get_rect(topleft=(x, y))
    comidas.append((img, rect))

# Comida mala
x = random.randint(0, ANCHO - 40)
y = random.randint(-600, -40)
comida_mala_rect = comida_mala_img.get_rect(topleft=(x, y))

velocidad_comida = 2

# Estado del juego
puntaje = 0
vidas = 3
game_over = False

# Función para mostrar texto centrado
def mostrar_texto_centrado(texto, fuente, color, pantalla, offset_y=0):
    texto_surface = fuente.render(texto, True, color)
    rect = texto_surface.get_rect(center=(ANCHO//2, ALTO//2 + offset_y))
    pantalla.blit(texto_surface, rect)

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game_over and evento.type == pygame.KEYDOWN:
            # Reiniciar juego al presionar una tecla
            jugador_rect.topleft = (100, 100)
            puntaje = 0
            vidas = 3
            game_over = False
            # Resetear posiciones de las comidas
            for i in range(len(comidas)):
                img, rect = comidas[i]
                rect.x = random.randint(0, ANCHO - 40)
                rect.y = random.randint(-600, -40)
                comidas[i] = (img, rect)
            comida_mala_rect.x = random.randint(0, ANCHO - 40)
            comida_mala_rect.y = random.randint(-600, -40)

    if not game_over:
        teclas = pygame.key.get_pressed()
        velocidad_x = 0

        if teclas[pygame.K_LEFT]:
            velocidad_x = -velocidad_movimiento
        if teclas[pygame.K_RIGHT]:
            velocidad_x = velocidad_movimiento
        if teclas[pygame.K_SPACE] and en_suelo:
            velocidad_y = salto
            en_suelo = False

        # Movimiento
        velocidad_y += gravedad
        jugador_rect.x += velocidad_x
        jugador_rect.y += velocidad_y

        # Colisión con suelo
        if jugador_rect.colliderect(suelo):
            jugador_rect.bottom = suelo.top
            velocidad_y = 0
            en_suelo = True
        else:
            en_suelo = False

        # Límites de pantalla
        if jugador_rect.left < 0:
            jugador_rect.left = 0
        if jugador_rect.right > ANCHO:
            jugador_rect.right = ANCHO
        if jugador_rect.top < 0:
            jugador_rect.top = 0
        if jugador_rect.bottom > ALTO:
            jugador_rect.bottom = ALTO
            velocidad_y = 0
            en_suelo = True

        # Mover comidas buenas
        for i in range(len(comidas)):
            img, rect = comidas[i]
            rect.y += velocidad_comida

            if rect.top > ALTO:
                rect.x = random.randint(0, ANCHO - 40)
                rect.y = random.randint(-600, -40)

            if rect.colliderect(jugador_rect):
                puntaje += 1
                rect.x = random.randint(0, ANCHO - 40)
                rect.y = random.randint(-600, -40)

            comidas[i] = (img, rect)

        # Mover comida mala
        comida_mala_rect.y += velocidad_comida
        if comida_mala_rect.top > ALTO:
            comida_mala_rect.x = random.randint(0, ANCHO - 40)
            comida_mala_rect.y = random.randint(-600, -40)

        if comida_mala_rect.colliderect(jugador_rect):
            vidas -= 1
            comida_mala_rect.x = random.randint(0, ANCHO - 40)
            comida_mala_rect.y = random.randint(-600, -40)

            if vidas <= 0:
                game_over = True

    # Dibujar
    pantalla.fill(BLANCO)
    pantalla.blit(jugador_img, jugador_rect)
    pygame.draw.rect(pantalla, (0, 200, 0), suelo)

    for img, rect in comidas:
        pantalla.blit(img, rect)

    pantalla.blit(comida_mala_img, comida_mala_rect)

    texto_puntaje = fuente.render(f"Puntos: {puntaje}", True, NEGRO)
    pantalla.blit(texto_puntaje, (ANCHO - 150, 10))

    texto_vidas = fuente.render(f"Vidas: {vidas}", True, ROJO)
    pantalla.blit(texto_vidas, (10, 10))

    if game_over:
        mostrar_texto_centrado("GAME OVER", fuente_grande, ROJO, pantalla)
        mostrar_texto_centrado(f"Puntaje final: {puntaje}", fuente, NEGRO, pantalla, offset_y=60)
        mostrar_texto_centrado("Presiona cualquier tecla para reiniciar", fuente, NEGRO, pantalla, offset_y=120)

    pygame.display.flip()
    clock.tick(FPS)
