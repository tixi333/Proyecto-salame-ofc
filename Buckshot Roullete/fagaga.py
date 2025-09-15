import pygame
import sys
import random
import math
from datetime import datetime

# -----------------------
# Configuración general
# -----------------------
FPS = 60
WINDOW_SIZE = (1000, 700)
BG_COLOR = (28, 30, 34)
UI_PANEL_COLOR = (40, 44, 52)
TEXT_COLOR = (230, 230, 230)
ACCENT = (200, 60, 60)
SAFE_GREEN = (80, 180, 120)
WARNING_COLOR = (230, 180, 60)

pygame.init()
FONT = pygame.font.SysFont("dejavusans", 18)
FONT_BIG = pygame.font.SysFont("dejavusans", 28, bold=True)

# -----------------------
# Lógica del juego
# -----------------------
class GameState:
    def __init__(self, num_players=4, cylinder_size=6, live_count=1):
        self.num_players = max(2, int(num_players))
        self.cylinder_size = max(1, int(cylinder_size))
        self.live_count = min(max(0, int(live_count)), self.cylinder_size)

        colors = [
            (200, 80, 80),
            (80, 150, 240),
            (255, 200, 80),
            (150, 80, 200),
            (90, 200, 160),
            (230, 120, 200),
            (180, 120, 70),
            (120, 220, 200),
        ]
        self.players = []
        for i in range(self.num_players):
            p = {
                "id": i,
                "name": f"P{i+1}",
                "alive": True,
                "color": colors[i % len(colors)],
                "eliminated_round": None
            }
            self.players.append(p)

        self.current_player_idx = 0
        self.round_number = 0
        self.history = []
        self.winner = None
        self.reset_for_new_round()

    def reset_for_new_round(self):
        self.round_number += 1
        self.cylinder_positions = set(random.sample(range(self.cylinder_size), self.live_count))

    def spin_and_shoot(self, player_idx):
        pos = random.randrange(self.cylinder_size)
        hit = pos in self.cylinder_positions
        if hit:
            self.cylinder_positions.discard(pos)

        ts = datetime.now().isoformat(timespec="seconds")
        player = self.players[player_idx]
        ev = {"time": ts, "round": self.round_number, "player": player["name"], "position": pos, "hit": hit}
        self.history.append(ev)

        if hit:
            self.players[player_idx]["alive"] = False
            self.players[player_idx]["eliminated_round"] = self.round_number

        return hit, pos

    def next_alive_player_idx(self, start_from=None):
        alive_indices = [i for i, p in enumerate(self.players) if p["alive"]]
        if len(alive_indices) <= 1:
            return None
        start = (self.current_player_idx + 1) % len(self.players) if start_from is None else start_from % len(self.players)
        for offset in range(len(self.players)):
            idx = (start + offset) % len(self.players)
            if self.players[idx]["alive"]:
                return idx
        return None

    def alive_count(self):
        return sum(1 for p in self.players if p["alive"])

    def check_winner(self):
        alive = [p for p in self.players if p["alive"]]
        if len(alive) == 1:
            self.winner = alive[0]
            return self.winner
        if len(alive) == 0:
            self.winner = None
            return None
        return None

# -----------------------
# UI / Helpers
# -----------------------
def draw_text(surface, text, pos, font=FONT, color=TEXT_COLOR, center=False):
    surf = font.render(text, True, color)
    r = surf.get_rect()
    if center:
        r.center = pos
    else:
        r.topleft = pos
    surface.blit(surf, r)

def draw_character(surface, player, pos, size=80):
    """Dibuja un personaje humanoide simplificado."""
    x, y = pos
    head_radius = size // 6
    body_height = size // 2

    skin = (255, 224, 189)
    shirt = player["color"]
    pants = (50, 50, 80)

    # Cabeza
    pygame.draw.circle(surface, skin, (x, y - body_height - head_radius), head_radius)

    # Ojos
    eye_y = y - body_height - head_radius
    pygame.draw.circle(surface, (0, 0, 0), (x - 8, eye_y), 3)
    pygame.draw.circle(surface, (0, 0, 0), (x + 8, eye_y), 3)

    # Cuerpo
    body_top = (x, y - body_height)
    body_bottom = (x, y)
    pygame.draw.line(surface, shirt, body_top, body_bottom, 8)

    # Brazos
    arm_length = size // 2
    pygame.draw.line(surface, shirt, (x, y - body_height//2), (x - arm_length//2, y - body_height//4), 6)
    pygame.draw.line(surface, shirt, (x, y - body_height//2), (x + arm_length//2, y - body_height//4), 6)

    # Piernas
    leg_length = size // 2
    pygame.draw.line(surface, pants, body_bottom, (x - leg_length//2, y + leg_length), 6)
    pygame.draw.line(surface, pants, body_bottom, (x + leg_length//2, y + leg_length), 6)

    # Texto: nombre y estado
    status = "VIVO" if player["alive"] else f"ELIM."
    color_status = SAFE_GREEN if player["alive"] else ACCENT
    draw_text(surface, f"{player['name']} - {status}", (x - size//2, y + leg_length + 10), font=FONT, color=color_status)

def draw_cylinder(surface, center, radius, cylinder_size, live_positions):
    cx, cy = center
    pygame.draw.circle(surface, (60,60,60), center, radius)
    inner_r = radius - 18
    pygame.draw.circle(surface, (20,20,20), center, inner_r)
    for i in range(cylinder_size):
        ang = -math.pi/2 + i * (2*math.pi / cylinder_size)
        sx = cx + math.cos(ang) * (inner_r + 6)
        sy = cy + math.sin(ang) * (inner_r + 6)
        slot_rect = pygame.Rect(0,0,32,20)
        slot_rect.center = (sx, sy)
        color = (180,80,80) if i in live_positions else (80,80,80)
        pygame.draw.ellipse(surface, color, slot_rect)
        pygame.draw.ellipse(surface, (20,20,20), slot_rect, width=2)

# -----------------------
# Main loop & game flow
# -----------------------
def main():
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Buckshot Roulette - Pygame con personajes")
    clock = pygame.time.Clock()

    game = GameState(num_players=4, cylinder_size=6, live_count=2)

    spin_animation = {"active": False, "angle": 0.0, "speed": 0.0}
    shot_flash = {"active": False, "alpha": 0, "color": (255,255,255)}

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not spin_animation["active"]:
                    spin_animation["active"] = True
                    spin_animation["speed"] = random.uniform(12, 20)

        if spin_animation["active"]:
            spin_animation["angle"] += spin_animation["speed"] * dt
            spin_animation["speed"] *= 0.95
            if spin_animation["speed"] < 2.0:
                spin_animation["active"] = False
                hit, pos = game.spin_and_shoot(game.current_player_idx)
                shot_flash["active"] = True
                shot_flash["alpha"] = 220 if hit else 120
                shot_flash["color"] = ACCENT if hit else (200,200,200)

                winner = game.check_winner()
                if winner:
                    print(f"Ganador: {winner['name']}")
                else:
                    nxt = game.next_alive_player_idx()
                    if nxt is None:
                        game.reset_for_new_round()
                        nxt = game.next_alive_player_idx(start_from=0)
                        game.current_player_idx = nxt if nxt else 0
                    else:
                        game.current_player_idx = nxt

        if shot_flash["active"]:
            shot_flash["alpha"] -= 600 * dt
            if shot_flash["alpha"] <= 0:
                shot_flash["active"] = False

        # Dibujar pantalla
        screen.fill(BG_COLOR)
        draw_text(screen, f"Ronda {game.round_number} - Jugador actual: {game.players[game.current_player_idx]['name']}", (20,20), font=FONT_BIG)

        draw_cylinder(screen, (500, 250), 160, game.cylinder_size, game.cylinder_positions)

        # Dibujar personajes en fila abajo
        base_y = 550
        spacing = 200
        for i, p in enumerate(game.players):
            draw_character(screen, p, (150 + i*spacing, base_y), size=80)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
