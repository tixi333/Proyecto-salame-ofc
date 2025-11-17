import pygame
import math
import sys

pygame.init()

# --- CONFIGURACIÓN ---
WIDTH, HEIGHT = 900, 550
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fútbol Flick - Menú + IA + Torneo")

CLOCK = pygame.time.Clock()
FRICTION = 0.985

# --- COLORES ---
WHITE = (255, 255, 255)
BLUE  = (80, 140, 255)
GREEN = (40, 140, 40)
GRAY = (220, 220, 220)
BLACK = (0, 0, 0)
RED_COLOR = (240, 70, 80)
YELLOW = (255, 255, 0)
TRANSPARENT_WHITE = (255,255,255,120)

font_big = pygame.font.SysFont(None, 70)
font_med = pygame.font.SysFont(None, 40)

# --- IMAGEN DEL EQUIPO ROJO ---
salame_img = pygame.image.load("salame.png").convert_alpha()
salame_img = pygame.transform.scale(salame_img, (45, 45))


# ================================================================
#                        CLASE DE PIEZA
# ================================================================
class Piece:
    def __init__(self, x, y, team, is_image=False, radius=22):
        self.x = float(x)
        self.y = float(y)
        self.vx = 0.0
        self.vy = 0.0
        self.team = team
        self.is_image = is_image
        self.radius = radius

    def update(self):
        self.x += self.vx
        self.y += self.vy

        # fricción
        self.vx *= FRICTION
        self.vy *= FRICTION

        if abs(self.vx) < 0.02: self.vx = 0
        if abs(self.vy) < 0.02: self.vy = 0

        # bordes
        if self.x - self.radius < 0:
            self.x = self.radius
            self.vx *= -0.7
        if self.x + self.radius > WIDTH:
            self.x = WIDTH - self.radius
            self.vx *= -0.7
        if self.y - self.radius < 0:
            self.y = self.radius
            self.vy *= -0.7
        if self.y + self.radius > HEIGHT:
            self.y = HEIGHT - self.radius
            self.vy *= -0.7

    def draw(self, surface):
        if self.is_image:
            # fondo rojo
            pygame.draw.circle(surface, RED_COLOR, (int(self.x), int(self.y)), self.radius)
            pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), self.radius, 2)
            # salame
            rect = salame_img.get_rect(center=(int(self.x), int(self.y)))
            surface.blit(salame_img, rect)
        else:
            pygame.draw.circle(surface, BLUE, (int(self.x), int(self.y)), self.radius)
            pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), self.radius, 2)

    def speed(self):
        return math.hypot(self.vx, self.vy)


# ================================================================
#                        FUNCIONES AUXILIARES
# ================================================================
def collide(a, b):
    dx = b.x - a.x
    dy = b.y - a.y
    dist = math.hypot(dx, dy)
    overlap = a.radius + b.radius - dist

    if overlap > 0 and dist != 0:
        nx = dx / dist
        ny = dy / dist

        a.x -= nx * overlap / 2
        a.y -= ny * overlap / 2
        b.x += nx * overlap / 2
        b.y += ny * overlap / 2

        va = a.vx * nx + a.vy * ny
        vb = b.vx * nx + b.vy * ny

        a.vx += (vb - va) * nx
        a.vy += (vb - va) * ny
        b.vx += (va - vb) * nx
        b.vy += (va - vb) * ny


def draw_dotted_line(surface, start, end, color, dot_distance=12, max_dots=7):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    dist = math.hypot(dx, dy)
    if dist == 0: return
    nx = dx / dist
    ny = dy / dist
    for i in range(1, max_dots + 1):
        alpha = max(50, 255 - i*30)
        dot_color = (color[0], color[1], color[2], alpha)
        pygame.draw.circle(surface, dot_color, (int(start[0]+nx*dot_distance*i), int(start[1]+ny*dot_distance*i)), 5)


def all_stopped(pieces):
    return all(p.speed() < 0.1 for p in pieces)


def create_teams():
    red_team = [
        Piece(120, 180, "RED", True),
        Piece(120, HEIGHT//2, "RED", True),
        Piece(120, 370, "RED", True)
    ]
    blue_team = [
        Piece(WIDTH-120, 180, "BLUE"),
        Piece(WIDTH-120, HEIGHT//2, "BLUE"),
        Piece(WIDTH-120, 370, "BLUE")
    ]
    ball = Piece(WIDTH//2, HEIGHT//2, "BALL", radius=14)
    return red_team, blue_team, ball


def reset_positions(red, blue, ball):
    red_pos = [(120,180),(120,HEIGHT//2),(120,370)]
    blue_pos = [(WIDTH-120,180),(WIDTH-120,HEIGHT//2),(WIDTH-120,370)]

    for i,p in enumerate(red):
        p.x,p.y = red_pos[i]
        p.vx=p.vy=0

    for i,p in enumerate(blue):
        p.x,p.y = blue_pos[i]
        p.vx=p.vy=0

    ball.x, ball.y = WIDTH//2, HEIGHT//2
    ball.vx = ball.vy = 0


# ================================================================
#                          IA SIMPLE (más fuerte)
# ================================================================
def ai_turn(blue_team, ball):
    chosen = min(blue_team, key=lambda p: math.hypot(p.x - ball.x, p.y - ball.y))
    dx = ball.x - chosen.x
    dy = ball.y - chosen.y
    dist = math.hypot(dx, dy)
    if dist == 0:
        return
    dx /= dist
    dy /= dist
    power = 16
    chosen.vx = dx * power
    chosen.vy = dy * power


# ================================================================
#                          MENÚ TORNEO
# ================================================================
def tournament_menu():
    while True:
        screen.fill((20, 20, 20))

        t = font_big.render("TORNEO (Mejor de 3)", True, WHITE)
        screen.blit(t, (WIDTH//2 - t.get_width()//2, 70))

        btn1 = pygame.Rect(WIDTH//2-150, 230, 300, 70)
        btn_back = pygame.Rect(WIDTH//2-150, 330, 300, 70)

        pygame.draw.rect(screen, GRAY, btn1)
        pygame.draw.rect(screen, GRAY, btn_back)

        screen.blit(font_med.render("Jugar vs IA", True, BLACK), (btn1.x+80, btn1.y+20))
        screen.blit(font_med.render("Volver", True, BLACK), (btn_back.x+110, btn_back.y+20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = event.pos
                if btn1.collidepoint(mx,my):
                    run_tournament()
                if btn_back.collidepoint(mx,my):
                    return

        pygame.display.flip()
        CLOCK.tick(60)


def run_tournament():
    wins_player = 0
    wins_ai = 0
    round_number = 1

    while wins_player < 2 and wins_ai < 2:
        result = game_loop(vs_ai=True, return_winner=True)
        if result == "RED":
            wins_player += 1
        else:
            wins_ai += 1

        # Pantalla de resultado de ronda
        show_round_result(round_number, wins_player, wins_ai)
        round_number += 1

    winner = "¡GANASTE EL TORNEO!" if wins_player > wins_ai else "LA IA GANÓ"

    while True:
        screen.fill((30,30,30))
        txt = font_big.render(winner, True, WHITE)
        screen.blit(txt, (WIDTH//2 - txt.get_width()//2, HEIGHT//2 - 50))

        sub = font_med.render("Presiona ESC para volver al menú", True, WHITE)
        screen.blit(sub, (WIDTH//2 - sub.get_width()//2, HEIGHT//2 + 20))

        pygame.display.flip()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return

def show_round_result(round_number, wins_player, wins_ai):
    screen.fill((40,40,40))
    txt = font_big.render(f"Ronda {round_number} Finalizada", True, YELLOW)
    screen.blit(txt, (WIDTH//2 - txt.get_width()//2, HEIGHT//2 - 80))
    score_txt = font_med.render(f"Jugador: {wins_player} | IA: {wins_ai}", True, WHITE)
    screen.blit(score_txt, (WIDTH//2 - score_txt.get_width()//2, HEIGHT//2 - 20))
    pygame.display.flip()
    pygame.time.delay(1500)


# ================================================================
#                          MENÚ PRINCIPAL
# ================================================================
def main_menu():
    while True:
        screen.fill((20, 20, 20))

        title = font_big.render("FÚTBOL FLICK", True, WHITE)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 80))

        btn1 = pygame.Rect(WIDTH//2-150, 220, 300, 70)
        btn2 = pygame.Rect(WIDTH//2-150, 320, 300, 70)
        btn3 = pygame.Rect(WIDTH//2-150, 420, 300, 70)

        for b in (btn1, btn2, btn3):
            pygame.draw.rect(screen, GRAY, b)

        screen.blit(font_med.render("Jugador vs Jugador", True, BLACK), (btn1.x+35, btn1.y+20))
        screen.blit(font_med.render("Jugador vs IA", True, BLACK), (btn2.x+80, btn2.y+20))
        screen.blit(font_med.render("Modo Torneo", True, BLACK), (btn3.x+85, btn3.y+20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = event.pos
                if btn1.collidepoint(mx,my):
                    game_loop(vs_ai=False)
                if btn2.collidepoint(mx,my):
                    game_loop(vs_ai=True)
                if btn3.collidepoint(mx,my):
                    tournament_menu()

        pygame.display.flip()
        CLOCK.tick(60)


# ================================================================
#                         JUEGO PRINCIPAL
# ================================================================
def game_loop(vs_ai=False, return_winner=False):

    red_team, blue_team, ball = create_teams()
    pieces = red_team + blue_team + [ball]

    score_red = 0
    score_blue = 0
    current_team = "RED"
    dragging = False
    active_piece = None
    drag_start = None
    drag_power = 0

    goal_left = pygame.Rect(0, HEIGHT//2 - 60, 10, 120)
    goal_right = pygame.Rect(WIDTH - 10, HEIGHT//2 - 60, 10, 120)

    while True:
        CLOCK.tick(60)
        screen.fill(GREEN)

        # --- EVENTOS ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and all_stopped(pieces):
                if vs_ai and current_team == "BLUE":
                    pass
                else:
                    mx, my = event.pos
                    team_list = red_team if current_team == "RED" else blue_team
                    for p in team_list:
                        if math.hypot(mx - p.x, my - p.y) <= p.radius:
                            dragging = True
                            active_piece = p
                            drag_start = (mx, my)
                            drag_power = 0
                            break

            if event.type == pygame.MOUSEBUTTONUP and dragging:
                mx, my = event.pos
                dx = drag_start[0] - mx
                dy = drag_start[1] - my
                power = 0.12
                active_piece.vx = dx * power
                active_piece.vy = dy * power
                dragging = False
                active_piece = None
                drag_power = 0
                current_team = "BLUE" if current_team == "RED" else "RED"

        # --- IA ---
        if vs_ai and current_team == "BLUE" and all_stopped(pieces):
            pygame.time.delay(400)
            ai_turn(blue_team, ball)
            current_team = "RED"

        # --- FÍSICA ---
        for p in pieces:
            p.update()
        for i in range(len(pieces)):
            for j in range(i + 1, len(pieces)):
                collide(pieces[i], pieces[j])

        # --- GOL ---
        if goal_left.collidepoint(ball.x - ball.radius, ball.y):
            score_blue += 1
            if return_winner: return "BLUE"
            reset_positions(red_team, blue_team, ball)

        if goal_right.collidepoint(ball.x + ball.radius, ball.y):
            score_red += 1
            if return_winner: return "RED"
            reset_positions(red_team, blue_team, ball)

        # --- DIBUJO ---
        pygame.draw.line(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 4)
        pygame.draw.circle(screen, WHITE, (WIDTH//2, HEIGHT//2), 80, 3)
        pygame.draw.rect(screen, WHITE, goal_left)
        pygame.draw.rect(screen, WHITE, goal_right)

        for p in pieces:
            p.draw(screen)

        # --- LÍNEA DE TIRO Y POTENCIA ---
        if dragging:
            mx,my = pygame.mouse.get_pos()
            dx = drag_start[0] - mx
            dy = drag_start[1] - my
            drag_power = min(math.hypot(dx, dy), 200)

            # línea con degradado
            aim_x = active_piece.x - dx
            aim_y = active_piece.y - dy
            draw_dotted_line(screen, (active_piece.x, active_piece.y), (aim_x, aim_y), WHITE)

            # barra de potencia
            bar_w = 150
            bar_h = 15
            bar_x = active_piece.x - bar_w//2
            bar_y = active_piece.y - active_piece.radius - 25
            pygame.draw.rect(screen, GRAY, (bar_x, bar_y, bar_w, bar_h))
            pygame.draw.rect(screen, YELLOW, (bar_x, bar_y, bar_w*drag_power/200, bar_h))

        # --- SCORE ---
        txt = font_med.render(f"Rojo {score_red} - {score_blue} Azul | Turno: {current_team}", True, WHITE)
        screen.blit(txt, (WIDTH//2 - txt.get_width()//2, 10))

        pygame.display.flip()

        if pygame.key.get_pressed()[pygame.K_ESCAPE] and not return_winner:
            return


# ================================================================
#                        INICIAR PROGRAMA
# ================================================================
main_menu()
