import pygame
import sys
import random

ANCHO, ALTO = 800, 600
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
FPS = 60

def pantalla_inicio(pantalla, fuente, fuente_grande):
    pantalla.fill(BLANCO)
    titulo = fuente_grande.render("¡Luvia de comida!", True, ROJO)
    pantalla.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 150))
    instrucciones = [
        "Mueve con las flechas ← →",
        "Salta con ESPACIO",
        "Atrapa la comida buena para sumar puntos",
        "Evita la comida mala y no dejes caer la buena",
        "Presiona cualquier tecla para comenzar"
    ]
    for i, texto in enumerate(instrucciones):
        linea = fuente.render(texto, True, NEGRO)
        pantalla.blit(linea, (ANCHO // 2 - linea.get_width() // 2, 250 + i * 40))
    pygame.display.flip()
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                esperando = False

def inicializar():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Salame")
    fuente = pygame.font.SysFont("Arial", 30)
    fuente_grande = pygame.font.SysFont("Arial", 60)
    clock = pygame.time.Clock()
    return pantalla, fuente, fuente_grande, clock
def cargar_record(ruta="Mini_Juego_LLC/record.txt"):
    try:
        with open(ruta, "r") as archivo:
            return int(archivo.read())
    except (FileNotFoundError, ValueError):
            record=0
            return record
def guardar_record(puntaje, ruta="Mini_Juego_LLC/record.txt"):
    record = cargar_record(ruta)
    if puntaje > record:
        with open(ruta, "w") as archivo:
            archivo.write(str(puntaje))
    


def cargar_imagenes():
    jugador_img = pygame.image.load('Mini_juego_LLC/imagenes/salame.png').convert_alpha()
    jugador_img = pygame.transform.scale(jugador_img, (75, 75))
    comidas_imgs = [
        pygame.transform.scale(pygame.image.load(f"Mini_Juego_LLC/imagenes/comida{i+1}.png").convert_alpha(), (40, 40))
        for i in range(4)
    ]
    comida_mala_img = pygame.transform.scale(pygame.image.load("Mini_Juego_LLC/imagenes/comida_mala.png").convert_alpha(), (40, 40))
    return jugador_img, comidas_imgs, comida_mala_img

def crear_rectangulos(jugador_img, comidas_imgs, comida_mala_img):
    jugador_rect = jugador_img.get_rect()
    jugador_rect.topleft = (100, 100)
    comidas = []
    for img in comidas_imgs:
        x = random.randint(0, ANCHO - 40)
        y = random.randint(-600, -40)
        rect = img.get_rect(topleft=(x, y))
        comidas.append((img, rect))
    x = random.randint(0, ANCHO - 40)
    y = random.randint(-600, -40)
    comida_mala_rect = comida_mala_img.get_rect(topleft=(x, y))
    suelo = pygame.Rect(0, ALTO - 50, ANCHO, 50)
    return jugador_rect, comidas, comida_mala_rect, suelo

def mostrar_texto_centrado(texto, fuente, color, pantalla, offset_y=0):
    texto_surface = fuente.render(texto, True, color)
    rect = texto_surface.get_rect(center=(ANCHO//2, ALTO//2 + offset_y))
    pantalla.blit(texto_surface, rect)

def reiniciar(jugador_rect, comidas, comida_mala_rect):
    jugador_rect.topleft = (100, 100)
    for i in range(len(comidas)):
        img, rect = comidas[i]
        rect.x = random.randint(0, ANCHO - 40)
        rect.y = random.randint(-600, -40)
        comidas[i] = (img, rect)
    comida_mala_rect.x = random.randint(0, ANCHO - 40)
    comida_mala_rect.y = random.randint(-600, -40)
    return jugador_rect, comidas, comida_mala_rect

def manejar_eventos(game_over, jugador_rect, comidas, comida_mala_rect):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game_over and evento.type == pygame.KEYDOWN:
            return True
    return False

def actualizar_jugador(teclas, jugador_rect, velocidad_y, en_suelo, salto, gravedad, velocidad_movimiento, suelo):
    velocidad_x = 0
    if teclas[pygame.K_LEFT]:
        velocidad_x = -velocidad_movimiento
    if teclas[pygame.K_RIGHT]:
        velocidad_x = velocidad_movimiento
    if teclas[pygame.K_SPACE] and en_suelo:
        velocidad_y = salto
        en_suelo = False

    velocidad_y += gravedad
    jugador_rect.x += velocidad_x
    jugador_rect.y += velocidad_y

    if jugador_rect.colliderect(suelo):
        jugador_rect.bottom = suelo.top
        velocidad_y = 0
        en_suelo = True
    else:
        en_suelo = False

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

    return jugador_rect, velocidad_y, en_suelo

def actualizar_comidas(comidas, jugador_rect, velocidad_comida, puntaje, vidas):
    for i in range(len(comidas)):
        img, rect = comidas[i]
        rect.y += velocidad_comida
        if rect.top > ALTO:
            rect.x = random.randint(0, ANCHO - 40)
            rect.y = random.randint(-600, -40)
            vidas-=1
        if rect.colliderect(jugador_rect):
            puntaje += 1
            rect.x = random.randint(0, ANCHO - 40)
            rect.y = random.randint(-600, -40)
        comidas[i] = (img, rect)

    return comidas, puntaje, vidas

def actualizar_comida_mala(comida_mala_rect, jugador_rect, velocidad_comida, vidas):
    comida_mala_rect.y += velocidad_comida
    if comida_mala_rect.top > ALTO:
        comida_mala_rect.x = random.randint(0, ANCHO - 40)
        comida_mala_rect.y = random.randint(-600, -40)
    if comida_mala_rect.colliderect(jugador_rect):
        vidas -= 1
        comida_mala_rect.x = random.randint(0, ANCHO - 40)
        comida_mala_rect.y = random.randint(-600, -40)
    return comida_mala_rect, vidas

def dibujar(pantalla, jugador_img, jugador_rect, suelo, comidas, comida_mala_img, comida_mala_rect, fuente, fuente_grande, puntaje, vidas, game_over,record):
    pantalla.fill(BLANCO)
    pantalla.blit(jugador_img, jugador_rect)
    pygame.draw.rect(pantalla, (0, 200, 0), suelo)
    for img, rect in comidas:
        pantalla.blit(img, rect)
    pantalla.blit(comida_mala_img, comida_mala_rect)
    texto_record=fuente.render(f"Record: {record}", True, NEGRO)
    pantalla.blit(texto_record, (ANCHO // 2 - texto_record.get_width() // 2, 10))
    texto_puntaje = fuente.render(f"Puntos: {puntaje}", True, NEGRO)
    pantalla.blit(texto_puntaje, (ANCHO - 150, 10))
    texto_vidas = fuente.render(f"Vidas: {vidas}", True, ROJO)
    pantalla.blit(texto_vidas, (10, 10))
    if game_over:
        mostrar_texto_centrado("GAME OVER", fuente_grande, ROJO, pantalla)
        mostrar_texto_centrado(f"Puntaje final: {puntaje}", fuente, NEGRO, pantalla, offset_y=60)
        mostrar_texto_centrado("Presiona cualquier tecla para reiniciar", fuente, NEGRO, pantalla, offset_y=120)
    pygame.display.flip()

# --- Main ---
def main():
    pantalla, fuente, fuente_grande, clock = inicializar()
    jugador_img, comidas_imgs, comida_mala_img = cargar_imagenes()
    jugador_rect, comidas, comida_mala_rect, suelo = crear_rectangulos(jugador_img, comidas_imgs, comida_mala_img)
    pantalla_inicio(pantalla, fuente, fuente_grande)
    velocidad_y = 0
    gravedad = 0.5
    salto = -10
    en_suelo = False
    velocidad_movimiento = 5
    velocidad_comida = 2
    puntaje = 0
    vidas = 3
    game_over = False
    record= cargar_record()
    while True:
        reiniciar_juego = manejar_eventos(game_over, jugador_rect, comidas, comida_mala_rect)
        if reiniciar_juego:
            if puntaje > record:
                guardar_record(puntaje)
                record=puntaje
            jugador_rect, comidas, comida_mala_rect = reiniciar(jugador_rect, comidas, comida_mala_rect)
            puntaje = 0
            vidas = 3
            game_over = False

        if not game_over:
            teclas = pygame.key.get_pressed()
            jugador_rect, velocidad_y, en_suelo = actualizar_jugador(
                teclas, jugador_rect, velocidad_y, en_suelo, salto, gravedad, velocidad_movimiento, suelo
            )
            comidas, puntaje, vidas = actualizar_comidas(comidas, jugador_rect, velocidad_comida, puntaje, vidas)
            comida_mala_rect, vidas = actualizar_comida_mala(comida_mala_rect, jugador_rect, velocidad_comida, vidas)
            if vidas <= 0:
                game_over = True

        dibujar(pantalla, jugador_img, jugador_rect, suelo, comidas, comida_mala_img, comida_mala_rect,
        fuente, fuente_grande, puntaje, vidas, game_over, record)
        clock.tick(FPS)

if __name__ == "__main__":
    main()