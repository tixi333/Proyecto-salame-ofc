import pygame, pygame_widgets
from pygame_widgets.button import Button

#seteo inicial
pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height)) #seteo tamaño pantalla
#colores
WHITE=(245,246,252); BLACK=(30,30,35); GRAY=(100,105,115)
GREEN=(70,190,120); RED=(230,90,90); BLUE=(90,150,240)
YELLOW=(245,210,80); PURPLE=(160,120,220); DARK=(24,26,32)
ACCENT=(90,200,255)
pygame.display.set_caption("Cuida a tu salame")
pygame.display.set_icon(pygame.image.load("salame.png").convert_alpha())
font = pygame.font.Font("monogram-extended.ttf", 36)


class salame:
    def __init__(self):
        self.health = 100
        self.happiness = 100
        self.image = pygame.image.load("salame.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (400, 400))
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class food:
    def __init__(self, name, image_path, health, value):
        self.name = name
        self.health = health
        self.value = value
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (85, 85))
        self.rect = self.image.get_rect()
    def draw(self):
        self.button = Button(
            screen,
            self.rect.x,
            self.rect.y,
            self.rect.width,
            self.rect.height,
            image=self.image
        )
    def feed(self):
        salame.health = salame.health + self.health
        if salame.health > 100:
            salame.health = 100




#flechas derechas
arrowright = pygame.image.load("arrowright.png").convert_alpha()
arrowright_bottom = pygame.transform.scale(arrowright, (40, 40))
arrowright = pygame.transform.scale(arrowright, (100, 100))
arrowright_back_rect = arrowright.get_rect()
arrowright_back_rect.center = (width // 2, height // 2)
arrowright_back_rect.left = arrowright_back_rect.right + 200
arrowright_bottom_rect = arrowright_bottom.get_rect()
arrowright_bottom_rect.midbottom = (width // 2 + 40, height)


#flechas izquierdas
arrowleft = pygame.image.load("arrowleft.png").convert_alpha()
arrowleft_bottom = pygame.transform.scale(arrowleft, (40, 40))
arrowleft = pygame.transform.scale(arrowleft, (100, 100))
arrowleft_back_rect = arrowleft.get_rect()
arrowleft_back_rect.center = (width // 2, height // 2)
arrowleft_back_rect.right = arrowleft_back_rect.left - 200
arrowleft_bottom_rect = arrowleft_bottom.get_rect()
arrowleft_bottom_rect.midbottom = (width // 2 - 40, height)

#básicamente, el texto de presiona i para info
info_text = font.render("Presiona <i> para info", True, BLACK)
info_rect = info_text.get_rect()
info_rect.midtop = (width // 2, 0)

#texto info 
i_text = font.render("iahygfjhjsgjhb", True, BLACK)
i_rect = i_text.get_rect()
i_rect.center = (width // 2, height // 2)
show_info = False

backgrounds = [YELLOW, BLUE, GREEN]
index = 0
buymenu = False
left = False
right = False
space = False

salame = salame()

total_lines = 49
total_pages = 7
ITEMS_PER_PAGE = 7
current_page = 0
last_page = 0
def read_page(page):
    start_line = page * ITEMS_PER_PAGE
    foods_on_page = []
    with open("food.txt", "r") as f:
        for i, line in enumerate(f):
            if i < start_line:
                continue
            if i >= start_line + ITEMS_PER_PAGE:
                break
            name, image, health, value = line.strip().split(" | ")
            foods_on_page.append(food(name, image, int(health), int(value)))
    return foods_on_page
    
def clear_buttons(buttons):
    for i in buttons:
        i = None
    buttons.clear()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                index = (index - 1) % len(backgrounds)
            elif event.key == pygame.K_RIGHT:
                index = (index + 1) % len(backgrounds)
            elif event.key == pygame.K_SPACE:
                space = not space
            elif event.key == pygame.K_i:
                show_info = not show_info
            elif event.key == pygame.K_b:
                buymenu = not buymenu
            elif event.key == pygame.K_a:
                if buymenu:
                    current_page = (current_page - 1) % total_pages
            elif event.key == pygame.K_d:
                if buymenu:
                    current_page = (current_page + 1) % total_pages
            

    if show_info:
        screen.fill(WHITE)
        screen.blit(i_text, i_rect)
    else:
        screen.fill(backgrounds[index])
        salame.draw(screen)
        screen.blit(arrowright, arrowright_back_rect)
        screen.blit(arrowleft, arrowleft_back_rect)
        screen.blit(info_text, info_rect)
        
        if backgrounds[index] == BLUE:
            if buymenu:
                screen.fill(WHITE)
                page_foods = read_page(current_page)
                height_offset = 0
                if current_page == last_page:
                    for current_food in page_foods:
                        current_food.rect.topleft = (10, 2 + height_offset)
                        text = font.render(f"{current_food.name} Salud: {current_food.health} Precio: {current_food.value}", True, BLACK)
                        current_food.draw()
                        screen.blit(text, (100, 22 + height_offset))
                        height_offset += 85
                else:
                    clear_buttons(page_foods)
                last_page = current_page

            else:

                screen.blit(arrowright_bottom, arrowright_bottom_rect)
                screen.blit(arrowleft_bottom, arrowleft_bottom_rect)


            
    pygame_widgets.update(event)
    pygame.display.update()




