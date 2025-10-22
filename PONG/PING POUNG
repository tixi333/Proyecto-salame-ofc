import os
import pygame

pygame.init()

def load_font(path_or_name, size):
    try:
        if os.path.isabs(path_or_name) or os.path.exists(path_or_name):
            return pygame.font.Font(path_or_name, size)
        rel = os.path.join(os.path.dirname(__file__), path_or_name)
        if os.path.exists(rel):
            return pygame.font.Font(rel, size)
        print(f"Advertencia: fuente '{path_or_name}' no encontrada. Usando fuente por defecto.")
        return pygame.font.Font(None, size)
    except Exception as e:
        print(f"Error cargando fuente '{path_or_name}': {e}. Usando fuente por defecto.")
        return pygame.font.Font(None, size)

font_menu = load_font('monogram-extended.ttf', 30)
font20 = load_font('freesansbold.ttf', 20)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Poung")

clock = pygame.time.Clock()
FPS = 30

def load_image(name):
    paths = [
        name,
        os.path.join(os.path.dirname(__file__), name)
    ]
    for p in paths:
        if os.path.exists(p):
            try:
                return pygame.image.load(p).convert_alpha()
            except Exception as e:
                print(f"Error cargando imagen '{p}': {e}")
                return None
    print(f"Advertencia: imagen '{name}' no encontrada en rutas esperadas.")
    return None

salame_image = load_image('salame_espacial.png')               
salame_marsiano_image = load_image('salame_marsiano.png')  

def show_start_screen():
    running = True
    while running:
        screen.fill(BLACK)
        title_text = font_menu.render("PING POUNG", True, WHITE)
        title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        screen.blit(title_text, title_rect)

        pvp_text = font_menu.render("Press 1 for Player vs Player", True, WHITE)
        pvp_rect = pvp_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(pvp_text, pvp_rect)

        pve_text = font_menu.render("Press 2 for Player vs Bot", True, WHITE)
        pve_rect = pve_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40))
        screen.blit(pve_text, pve_rect)

        esc_text = font20.render("[Esc] Menu", True, WHITE)
        screen.blit(esc_text, (10, HEIGHT - 30))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "PVP"
                elif event.key == pygame.K_2:
                    return "PVE"
    return None

class Striker:
    def __init__(self, posx, posy, width, height, speed, color, image=None):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.image = image
        if self.image:
            try:
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
            except Exception:
                pass
        self.geekRect = pygame.Rect(posx, posy, width, height)

    def display(self):
        if self.image:
            screen.blit(self.image, (self.posx, self.posy))
        else:
            pygame.draw.rect(screen, self.color, self.geekRect)

    def update(self, yFac):
        self.posy = self.posy + self.speed * yFac
        if self.posy <= 0:
            self.posy = 0
        elif self.posy + self.height >= HEIGHT:
            self.posy = HEIGHT - self.height
        self.geekRect = pygame.Rect(self.posx, self.posy, self.width, self.height)

    def displayScore(self, text, score, x, y, color):
        text = font20.render(text + str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)
        screen.blit(text, textRect)

    def getRect(self):
        return self.geekRect

class Bot:
    def __init__(self, posx, posy, width, height, speed, color, image=None):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.image = image
        if self.image:
            try:
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
            except Exception:
                pass
        self.geekRect = pygame.Rect(posx, posy, width, height)

    def display(self):
        if self.image:
            screen.blit(self.image, (self.posx, self.posy))
        else:
            pygame.draw.rect(screen, self.color, self.geekRect)

    def update(self, ball):
        target_pos = ball.posy - self.height / 2
        if abs(self.posy - target_pos) > 5:
            if self.posy < target_pos:
                self.posy += self.speed
            else:
                self.posy -= self.speed

        if self.posy <= 0:
            self.posy = 0
        elif self.posy + self.height >= HEIGHT:
            self.posy = HEIGHT - self.height

        self.geekRect = pygame.Rect(self.posx, self.posy, self.width, self.height)

    def getRect(self):
        return self.geekRect

    def displayScore(self, text, score, x, y, color):
        text = font20.render(text + str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)
        screen.blit(text, textRect)

class Ball:
    def __init__(self, posx, posy, radius, speed, color):
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.speed = speed
        self.color = color
        self.xFac = 1
        self.yFac = -1
        self.firstTime = 1
        self.ballRect = pygame.Rect(self.posx - self.radius, self.posy - self.radius, self.radius*2, self.radius*2)

    def display(self):
        pygame.draw.circle(screen, self.color, (int(self.posx), int(self.posy)), self.radius)
        self.ballRect = pygame.Rect(int(self.posx) - self.radius, int(self.posy) - self.radius, self.radius*2, self.radius*2)

    def update(self):
        self.posx += self.speed * self.xFac
        self.posy += self.speed * self.yFac

        if self.posy - self.radius <= 0 or self.posy + self.radius >= HEIGHT:
            self.yFac *= -1

        if self.posx - self.radius <= 0 and self.firstTime:
            self.firstTime = 0
            return 1
        elif self.posx + self.radius >= WIDTH and self.firstTime:
            self.firstTime = 0
            return -1
        else:
            return 0

    def reset(self):
        self.posx = WIDTH // 2
        self.posy = HEIGHT // 2
        self.xFac *= -1
        self.firstTime = 1

    def hit(self):
        self.xFac *= -1

    def getRect(self):
        return self.ballRect

def main():
    while True:
        mode = show_start_screen()
        if mode is None:
            break

        left_img_w, left_img_h = 100, 80
        right_img_w, right_img_h = 100, 80

        if salame_image:
            geek1 = Striker(20, 0, left_img_w, left_img_h, 10, GREEN, image=salame_image)
        else:
            geek1 = Striker(20, 0, 10, 100, 10, GREEN)
        if mode == "PVP":
            if salame_marsiano_image:
                geek2 = Striker(WIDTH - 20 - right_img_w, 0, right_img_w, right_img_h, 10, GREEN, image=salame_marsiano_image)
            else:
                geek2 = Striker(WIDTH - 30, 0, 10, 100, 10, GREEN)
        else:
            if salame_marsiano_image:
                geek2 = Bot(WIDTH - 20 - right_img_w, 0, right_img_w, right_img_h, 5, GREEN, image=salame_marsiano_image)
            else:
                geek2 = Bot(WIDTH - 30, 0, 10, 100, 5, GREEN)

        ball = Ball(WIDTH // 2, HEIGHT // 2, 7, 7, WHITE)
        listOfGeeks = [geek1, geek2]

        geek1Score, geek2Score = 0, 0
        geek1YFac, geek2YFac = 0, 0

        running = True
        while running:
            screen.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_UP:
                        geek2YFac = -1
                    if event.key == pygame.K_DOWN:
                        geek2YFac = 1
                    if event.key == pygame.K_w:
                        geek1YFac = -1
                    if event.key == pygame.K_s:
                        geek1YFac = 1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        geek2YFac = 0
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        geek1YFac = 0

            if mode == "PVE":
                diff = geek1Score - geek2Score
                base_speed = 5
                new_speed = base_speed + diff
                if new_speed < 1:
                    new_speed = 1
                elif new_speed > 10:
                    new_speed = 10
                geek2.speed = new_speed

            if mode == "PVP":
                geek2.update(geek2YFac)
            else:
                geek2.update(ball)

            for geek in listOfGeeks:
                if ball.getRect().colliderect(geek.getRect()):
                    ball.hit()

            geek1.update(geek1YFac)
            point = ball.update()

            if point == -1:
                geek1Score += 1
            elif point == 1:
                geek2Score += 1

            if point:
                ball.reset()

            geek1.display()
            geek2.display()
            ball.display()

            geek1.displayScore("Geek_1 : ", geek1Score, 100, 20, WHITE)
            geek2.displayScore("Geek_2 : ", geek2Score, WIDTH - 100, 20, WHITE)

            pygame.display.update()
            clock.tick(FPS)

if __name__ == "__main__":
    main()
    pygame.quit()