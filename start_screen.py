"""
start_screen.py
A simple Pygame start screen that shows the title "POUNG" and two buttons: "Vs Máquina" and "Vs Jugador".
Clicking a button will call a placeholder function (start_vs_machine or start_vs_player) which currently shows a brief message and exits. Integrate these functions with the main game code as needed.

Run: pip install pygame
       python start_screen.py

"""

import sys
import pygame

WIDTH, HEIGHT = 800, 600
BG_COLOR = (30, 30, 40)
BUTTON_COLOR = (200, 200, 200)
BUTTON_HOVER = (255, 180, 0)
TEXT_COLOR = (20, 20, 30)
TITLE_COLOR = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("POUNG - Start Screen")

FONT_TITLE = pygame.font.SysFont(None, 100)
FONT_BUTTON = pygame.font.SysFont(None, 40)
FONT_MSG = pygame.font.SysFont(None, 48)

clock = pygame.time.Clock()


class Button:
    def __init__(self, rect, text, callback):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.callback = callback

    def draw(self, surf):
        mouse = pygame.mouse.get_pos()
        is_hover = self.rect.collidepoint(mouse)
        color = BUTTON_HOVER if is_hover else BUTTON_COLOR
        pygame.draw.rect(surf, color, self.rect, border_radius=8)
        txt = FONT_BUTTON.render(self.text, True, TEXT_COLOR)
        txt_rect = txt.get_rect(center=self.rect.center)
        surf.blit(txt, txt_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.callback()


def start_vs_machine():
    # Placeholder - replace with your game loop vs AI
    show_message_and_quit("Seleccionaste: Vs Máquina")


def start_vs_player():
    # Placeholder - replace with your two-player game loop
    show_message_and_quit("Seleccionaste: Vs Jugador")


def show_message_and_quit(message, delay_ms=1200):
    # Show a temporary message and quit (for demo purposes)
    t0 = pygame.time.get_ticks()
    while pygame.time.get_ticks() - t0 < delay_ms:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BG_COLOR)
        msg = FONT_MSG.render(message, True, TITLE_COLOR)
        screen.blit(msg, msg.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    sys.exit()


def main():
    btn_w, btn_h = 260, 70
    gap = 30
    total_h = btn_h * 2 + gap
    start_y = (HEIGHT - total_h) // 2 + 80

    btn_vs_machine = Button(
        rect=((WIDTH - btn_w) // 2, start_y, btn_w, btn_h),
        text="Vs Máquina",
        callback=start_vs_machine,
    )

    btn_vs_player = Button(
        rect=((WIDTH - btn_w) // 2, start_y + btn_h + gap, btn_w, btn_h),
        text="Vs Jugador",
        callback=start_vs_player,
    )

    buttons = [btn_vs_machine, btn_vs_player]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for b in buttons:
                b.handle_event(event)

        screen.fill(BG_COLOR)

        # Title
        title_surf = FONT_TITLE.render("POUNG", True, TITLE_COLOR)
        screen.blit(title_surf, title_surf.get_rect(center=(WIDTH // 2, HEIGHT // 4)))

        # Draw buttons
        for b in buttons:
            b.draw(screen)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()