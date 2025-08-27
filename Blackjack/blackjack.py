import random

palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
valores = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

def crear_baraja():
    baraja = []
    for palo in palos:
        for valor in valores:
            baraja.append((valor, palo))
    random.shuffle(baraja)
    return baraja

def calcular_puntos(mano):
    total = 0
    ases = 0
    for carta in mano:
        valor = carta[0]
        total += valores[valor]
        if valor == 'A':
            ases += 1

    while total > 21 and ases:
        total -= 10
        ases -= 1

    return total

def mostrar_mano(mano, nombre='Jugador'):
    cartas = [f"{v} de {p}" for v, p in mano]
    print(f"{nombre}: {', '.join(cartas)} | Total: {calcular_puntos(mano)}")

def jugar_blackjack():
    baraja = crear_baraja()

    jugador = [baraja.pop(), baraja.pop()]
    dealer = [baraja.pop(), baraja.pop()]

    mostrar_mano(jugador, "Jugador")
    print(f"Dealer: {dealer[0][0]} de {dealer[0][1]}, ???")

    while True:
        eleccion = input("¿Quieres otra carta? (s/n): ").lower()
        if eleccion == 's':
            jugador.append(baraja.pop())
            mostrar_mano(jugador, "Jugador")
            if calcular_puntos(jugador) > 21:
                print("¡Te pasaste! Pierdes.")
                return
        else:
            break

    print("\nTurno del dealer:")
    mostrar_mano(dealer, "Dealer")
    while calcular_puntos(dealer) < 17:
        dealer.append(baraja.pop())
        mostrar_mano(dealer, "Dealer")

    puntos_jugador = calcular_puntos(jugador)
    puntos_dealer = calcular_puntos(dealer)

    if puntos_dealer > 21 or puntos_jugador > puntos_dealer:
        print("¡Ganaste!")
    elif puntos_jugador == puntos_dealer:
        print("Empate.")
    else:
        print("Perdiste.")

jugar_blackjack()
