import random
import pygame
import os
import sys

pygame.init()

ANCHO, ALTO = 1000, 600
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 128, 0)
FUENTE = pygame.font.SysFont("arial", 24)
RUTA_CARTAS = "Blackjack/cartas"

VALORES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'j': 10, 'q': 10, 'k': 10, 'a': 11
}
PALOS = ['p', 'c', 'd', 't'] 

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Blackjack con Pygame")
pygame.display.set_icon(pygame.image.load("salame.png").convert_alpha())

cartel_base = pygame.image.load(os.path.join("Blackjack/cartas", "cartel.png"))
cartel_base = pygame.transform.scale(cartel_base, (153,90))

def cargar_imagen(nombre):
    ruta = os.path.join(RUTA_CARTAS, nombre + ".png")
    imagen = pygame.image.load(ruta)
    return pygame.transform.scale(imagen, (80, 120))

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
        ventana.blit(cartel_base, (783, y_pos-48)) 
        txt = FUENTE.render(linea, True, BLANCO)
        ventana.blit(txt, (800, y_pos - 10))


def main():
    clock = pygame.time.Clock()
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
                        main()  # Reiniciar juego

                        

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
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()

