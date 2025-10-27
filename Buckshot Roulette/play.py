import pygame
import random
from resources import load_resources

resources = load_resources()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (220, 60, 60)
BLUE = (60, 120, 220)
WIDTH, HEIGHT = 800, 
font = resources["font"]
class Dealer:
    def __init__(self):
        self.hp = 3
        self.state = "idle"
        self.timer = 0
        self.known_next_shell = None
        self.inventory = ["magnifying_glass", "cigarette", "saw", "handcuffs"]

        self.current_message = ""
        self.messages = [
            "Tu turno, jugador...",
            "Hmm... interesante...",
            "Veamos qué pasa...",
            "Bang o click..."
        ]

    def speak(self, msg=None):
        self.state = "talk"
        self.current_message = msg or random.choice(self.messages)
        self.timer = 120

    def update(self):
        if self.timer > 0:
            self.timer -= 1
        else:
            self.state = "idle"

    def draw(self, surface):

        color = RED if self.state == "talk" else WHITE
        pygame.draw.rect(surface, color, (WIDTH//2 - 75, HEIGHT//2 - 150, 150, 150))


        hp_text = font.render(f"HP: {self.hp}", True, WHITE)
        surface.blit(hp_text, (WIDTH//2 - hp_text.get_width()//2, HEIGHT//2 + 20))

 
        if self.current_message:
            msg = font.render(self.current_message, True, WHITE)
            surface.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT - 80))

        inv_text = font.render(f"Items: {', '.join(self.inventory) if self.inventory else 'Ninguno'}", True, (200, 200, 200))
        surface.blit(inv_text, (20, 20))

    def use_item(self, chamber, index):
        if not self.inventory:
            return None

        if "cigarette" in self.inventory and self.hp <= 1:
            self.hp += 1
            self.inventory.remove("cigarette")
            self.speak("Necesito un respiro...")
            return "cigarette"


        if "magnifying_glass" in self.inventory and self.known_next_shell is None:
            self.known_next_shell = chamber[index]
            self.inventory.remove("magnifying_glass")
            self.speak("Veamos qué hay en la recámara...")
            return "magnifying_glass"

        if "saw" in self.inventory and self.known_next_shell == 1:
            self.inventory.remove("saw")
            self.speak("Esto dolerá el doble...")
            return "saw"

        if "handcuffs" in self.inventory and self.known_next_shell == 0:
            self.inventory.remove("handcuffs")
            self.speak("Parece que tendrás que esperar tu turno...")
            return "handcuffs"

        return None

    def choose_target(self):
        
        if self.known_next_shell == 0:
            return "self"
        elif self.known_next_shell == 1:
            return "player"

        return random.choices(["player", "self"], weights=[0.7, 0.3])[0]

 def use_item(self, chamber, index):
        if not self.inventory:
            return None

        # 1️⃣ Curarse si está en peligro
        if "cigarette" in self.inventory and self.hp <= 1:
            self.hp += 1
            self.inventory.remove("cigarette")
            self.speak("Necesito un respiro...")
            return "cigarette"

        # 2️⃣ Usar lupa si no sabe qué sigue
        if "magnifying_glass" in self.inventory and self.known_next_shell is None:
            self.known_next_shell = chamber[index]
            self.inventory.remove("magnifying_glass")
            self.speak("Veamos qué hay en la recámara...")
            return "magnifying_glass"

        # 3️⃣ Usar sierra si sabe que viene una bala real
        if "saw" in self.inventory and self.known_next_shell == 1:
            self.inventory.remove("saw")
            self.speak("Esto dolerá el doble...")
            return "saw"

        # 4️⃣ Usar esposas si sabe que es bala falsa
        if "handcuffs" in self.inventory and self.known_next_shell == 0:
            self.inventory.remove("handcuffs")
            self.speak("Parece que tendrás que esperar tu turno...")
            return "handcuffs"

        return None

    def choose_target(self):
        # Si sabe la próxima bala
        if self.known_next_shell == 0:
            return "self"
        elif self.known_next_shell == 1:
            return "player"

        # Si no sabe, decide con probabilidad
        return random.choices(["player", "self"], weights=[0.7, 0.3])[0]


# --- CLASE JUGADOR SIMPLIFICADA ---
class Player:
    def __init__(self):
        self.hp = 3

    def draw(self, surface):
        pygame.draw.rect(surface, BLUE, (WIDTH//2 - 75, HEIGHT//2 + 50, 150, 150))
        hp_text = font.render(f"Jugador HP: {self.hp}", True, WHITE)
        surface.blit(hp_text, (WIDTH//2 - hp_text.get_width()//2, HEIGHT//2 + 210))


# --- INICIALIZACIÓN ---
dealer = Dealer()
player = Player()
turn = "dealer"

# Cámara con 1-2 balas reales al azar
real_bullets = random.randint(1, 2)
chamber = [1]*real_bullets + [0]*(6 - real_bullets)
random.shuffle(chamber)
index = 0

# --- LOOP PRINCIPAL ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Jugador pasa turno con ESPACIO (solo para probar)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if turn == "player":
                turn = "dealer"

    # --- Lógica del dealer ---
    if turn == "dealer":
        used_item = dealer.use_item(chamber, index)
        pygame.time.delay(1000)

        target = dealer.choose_target()
        dealer.speak(f"Apunto al {target}...")
        pygame.time.delay(1000)

        shell = chamber[index]
        index = (index + 1) % len(chamber)

        if shell == 1:
            if target == "player":
                player.hp -= 1
                dealer.speak("BANG! 💥 Directo al jugador.")
            else:
                dealer.hp -= 1
                dealer.speak("Click... mierda, era real.")
        else:
            dealer.speak("Click... sin bala.")

        dealer.known_next_shell = None
        turn = "player"

    # --- Actualización ---
    dealer.update()

    # --- Dibujo ---
    screen.fill(BLACK)
    dealer.draw(screen)
    player.draw(screen)

    # Texto de turno
    t = font.render(f"Turno: {turn.upper()}", True, WHITE)
    screen.blit(t, (WIDTH - 200, 20))

    pygame.display.flip()
    clock.tick(60)

    # --- Fin de juego ---
    if dealer.hp <= 0:
        print("💀 Dealer ha muerto. Ganó el jugador.")
        running = False
    elif player.hp <= 0:
        print("💀 El jugador ha muerto. Dealer gana.")
        running = False

pygame.quit()