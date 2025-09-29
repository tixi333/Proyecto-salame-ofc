import random
import pygame
import os
import sys

pygame.init()

ANCHO, ALTO = 1000, 600
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 128, 0)
FUENTE = pygame.font.Font("monogram-extended.ttf", 40)
RUTA_CARTAS = "Blackjack/cartas"

VALORES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'j': 10, 'q': 10, 'k': 10, 'a': 11
}
PALOS = ['p', 'c', 'd', 't'] 

personaje_img = pygame.image.load(os.path.join(RUTA_CARTAS, "salame_monio.png"))
personaje_img = pygame.transform.scale(personaje_img, (200, 200))
personaje_triste_img = pygame.image.load(os.path.join(RUTA_CARTAS, "salame_monio_triste.png"))
personaje_triste_img = pygame.transform.scale(personaje_triste_img, (200, 200))

def mostrar_personaje_dialogo(mensaje):
    personaje_x = ANCHO - 350  
    personaje_y = ALTO - 250   
    if "salame" in mensaje or "Perdiste" in mensaje:
        ventana.blit(personaje_triste_img, (personaje_x, personaje_y))
    else:
        ventana.blit(personaje_img, (personaje_x, personaje_y))

    fuente_grande = pygame.font.Font("monogram-extended.ttf", 40) 
    texto = fuente_grande.render(mensaje, True, NEGRO)

    padding = 20
    burbuja_ancho = texto.get_width() + padding
    burbuja_alto = texto.get_height() + padding
    burbuja = pygame.Surface((burbuja_ancho, burbuja_alto))
    burbuja.fill(BLANCO)

    burbuja_x = personaje_x - burbuja_ancho - 20
    burbuja_y = personaje_y + 60
    ventana.blit(burbuja, (burbuja_x, burbuja_y))
    ventana.blit(texto, (burbuja_x + 10, burbuja_y + 10))


ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Cuida a tu salame")
pygame.display.set_icon(pygame.image.load("salame.png").convert_alpha())

cartel_base = pygame.image.load(os.path.join("Blackjack/cartas", "cartel.png"))
cartel_base = pygame.transform.scale(cartel_base, (153,90))

def cargar_imagen(nombre):
    ruta = os.path.join(RUTA_CARTAS, nombre + ".png")
    imagen = pygame.image.load(ruta)
    return pygame.transform.scale(imagen, (80, 120))

def pantalla_inicio():
    mostrar_texto = True
    tiempo_parpadeo = 500 
    ultimo_cambio = pygame.time.get_ticks()

    while True:
        ventana.fill(VERDE)

        titulo = FUENTE.render("¡Cuida a tu salame! - Blackjack", True, BLANCO)
        ventana.blit(titulo, (ANCHO//2 - titulo.get_width()//2, ALTO//2 - 100))

        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - ultimo_cambio > tiempo_parpadeo:
            mostrar_texto = not mostrar_texto
            ultimo_cambio = tiempo_actual

        if mostrar_texto:
            subtitulo = FUENTE.render("Presiona [Enter] para comenzar", True, BLANCO)
            ventana.blit(subtitulo, (ANCHO//2 - subtitulo.get_width()//2, ALTO//2))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    return


def leer_dinero():
   with open("money.txt", "r") as archivo:
        return int(archivo.read())


def escribir_dinero(dinero):
    with open("money.txt", "w") as archivo:
        archivo.write(str(dinero))


def crear_baraja():
    baraja = []
    for palo in PALOS:
        for valor in VALORES.keys():
            carta = palo + valor
            baraja.append(carta)
    random.shuffle(baraja)
    return baraja


def calcular_puntos(mano):
    total = 0
    ases = 0
    for carta in mano:
        valor = carta[1:]
        total += VALORES[valor]
        if valor == 'a':
            ases += 1

    while total > 21 and ases:
        total -= 10
        ases -= 1
    return total

def mostrar_mano(mano, x, y, ocultar_segunda=False):
    for i, carta in enumerate(mano):
        if i == 1 and ocultar_segunda:
            imagen = cargar_imagen("back")
        else:
            imagen = cargar_imagen(carta)
        ventana.blit(imagen, (x + i * 90, y))

def mostrar_mensaje(texto):
    msg = FUENTE.render(texto, True, NEGRO)
    ventana.blit(msg, (ANCHO//2 - msg.get_width()//2, 20))

def mostrar_controles():
    instrucciones = [
        "[P] Pedir carta",
        "[S] Plantarse",
        "[R] Salir"
        ]
    for i, linea in enumerate(instrucciones):
        y_pos = 50 + i * 75  
        ventana.blit(cartel_base, (699, y_pos-48)) 
        txt = FUENTE.render(linea, True, BLANCO)
        ventana.blit(txt, (700, y_pos - 10))

def main():
    clock = pygame.time.Clock()
    dinero = leer_dinero()
    print(f"Tienes {dinero} en tu cuenta.")
    
    if dinero < 100:
        mostrar_mensaje("No tienes suficiente dinero para jugar.")
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()
    baraja = crear_baraja()
    jugador = [baraja.pop(), baraja.pop()]
    dealer = [baraja.pop(), baraja.pop()]
    en_juego = True
    turno = "jugador"
    resultado = ""

    while True:
        ventana.fill((0, 100, 0))  

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.KEYDOWN:
                if en_juego:
                    if evento.key == pygame.K_p:
                        jugador.append(baraja.pop())
                        if calcular_puntos(jugador) > 21:
                            resultado = "¡Te pasaste! Pierdes."
                            en_juego = False

                    elif evento.key == pygame.K_s:
                        turno = "dealer"
                        while calcular_puntos(dealer) < 17:
                            dealer.append(baraja.pop())
                        puntos_j = calcular_puntos(jugador)
                        puntos_d = calcular_puntos(dealer)
                        if puntos_d > 21 or puntos_j > puntos_d:
                            resultado = "¡Ganaste!"
                        elif puntos_j == puntos_d:
                            resultado = "Empate."
                        else:
                            resultado = "Perdiste."
                        en_juego = False

                else:
                    if evento.key == pygame.K_r:
                        main()
                        
        mostrar_mano(jugador, 50, 400)
        mostrar_mano(dealer, 50, 100, ocultar_segunda=en_juego)

        puntos_j = calcular_puntos(jugador)
        puntos_d = calcular_puntos(dealer) if not en_juego else "?"
        puntos_txt = FUENTE.render(f"Jugador: {puntos_j}    Dealer: {puntos_d}", True, BLANCO)
        ventana.blit(puntos_txt, (50, 300))

        if not en_juego:
            mostrar_mensaje(resultado)
            reinicio = FUENTE.render("Haz [R] para reiniciar", True, BLANCO)
            ventana.blit(reinicio, (ANCHO//2 - reinicio.get_width()//2, 60))
        mostrar_controles()

        if en_juego:
            mensaje_personaje = "¿Qué quieres hacer?"
        else:
            if resultado == "¡Ganaste!":
                mensaje_personaje = "¡Bien!"
            elif resultado == "Empate.":
                mensaje_personaje = "Okay... no está mal."
            elif resultado == "Perdiste.":
                mensaje_personaje = "Perdiste... sos un salame."
            else:
                mensaje_personaje = "Fin del juego."

        mostrar_personaje_dialogo(mensaje_personaje)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    pantalla_inicio()
    main()