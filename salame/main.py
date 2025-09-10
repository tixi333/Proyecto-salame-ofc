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

#clases salame y comida

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
        if not hasattr(self, 'button'):
            self.button = Button(
                screen,
                self.rect.x,
                self.rect.y,
                self.rect.width,
                self.rect.height,
                image=self.image,
                onClick=self.feed_or_buy     
            )
        else:
            self.button.show()
    def feed_or_buy(self):
        if buymenu:
            with open("money.txt", "r") as f:
                money = int(f.read().strip())
            if money >= self.value:
                money -= self.value
                with open("money.txt", "w") as f:
                    f.write(str(money))
                with open("food_bought.txt", "a") as f:
                    f.write(f"{self.name} | {self.image} | {self.health} | {self.value}\n")
            else:
                no_money_flag == True

        elif current_background == BLUE:    
            salame.health = salame.health + self.health
            if salame.health > 100:
                salame.health = 100
    def hide(self):
        self.button.hide()
       

#flechas generales de todos los back (salvo los flags)
arrowright = pygame.image.load("arrowright.png").convert_alpha()
arrowright = pygame.transform.scale(arrowright, (100, 100))
arrowright_back_rect = arrowright.get_rect()
arrowright_back_rect.center = (width // 2, height // 2)
arrowright_back_rect.left = arrowright_back_rect.right + 200
arrowleft = pygame.image.load("arrowleft.png").convert_alpha()
arrowleft = pygame.transform.scale(arrowleft, (100, 100))
arrowleft_back_rect = arrowleft.get_rect()
arrowleft_back_rect.center = (width // 2, height // 2)
arrowleft_back_rect.right = arrowleft_back_rect.left - 200

#flechas inferiores para el menú de comida comprada (sólo en el fondo azul)
arrowleft_bottom = pygame.transform.scale(arrowleft, (40, 40))
arrowleft_bottom_rect = arrowleft_bottom.get_rect()
arrowleft_bottom_rect.midbottom = (width // 2 - 150, height)
arrowright_bottom = pygame.transform.scale(arrowright, (40, 40))
arrowright_bottom_rect = arrowright_bottom.get_rect()
arrowright_bottom_rect.midbottom = (width // 2 + 150, height)
no_food_text = font.render("No tienes comida comprada", True, BLACK)
no_food_rect = no_food_text.get_rect()
no_food_rect.midbottom = (width // 2, height) 

#todo lo de info
info_text = font.render("Presiona <i> para info", True, BLACK)
info_rect = info_text.get_rect()
info_rect.midtop = (width // 2, 0)
i_text = font.render("iahygfjhjsgjhb", True, BLACK)
i_rect = i_text.get_rect()
i_rect.center = (width // 2, height // 2)


#para manejar fondos
backgrounds = [YELLOW, BLUE, GREEN]
index = 0

#flags
show_info = False
buymenu = False
no_money_flag = False



#para manejar la comida comprada
food_index = 0
bought_food = []


#instancia salame
salame = salame()

#para poder manejar los botones
buttons = []
def clear_buttons():
    for i in buttons:
        for widget in i:
            widget.hide()
        buttons.clear()
        
#esto es para definir items por página del menú de compra
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



running = True
while running:
    clear_buttons()
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
                elif backgrounds[index] == BLUE:
                    food_index = (food_index - 1) % len(bought_food) 
            elif event.key == pygame.K_d:
                if buymenu:
                    current_page = (current_page + 1) % total_pages
                elif backgrounds[index] == BLUE:
                    food_index = (food_index + 1) % len(bought_food) 

    current_background = backgrounds[index]        

    if show_info:
        screen.fill(WHITE)
        screen.blit(i_text, i_rect)
    else:
        screen.fill(backgrounds[index])
        salame.draw(screen)
        screen.blit(arrowright, arrowright_back_rect)
        screen.blit(arrowleft, arrowleft_back_rect)
        screen.blit(info_text, info_rect)
        
        if current_background == BLUE:
            if buymenu:
                screen.fill(WHITE)
                page_foods = read_page(current_page)
                buttons.append(page_foods)
                height_offset = 0
                for current_food in page_foods:
                    current_food.rect.topleft = (10, 2 + height_offset)
                    text = font.render(f"{current_food.name} | Salud: {current_food.health} | Precio: {current_food.value}", True, BLACK)
                    current_food.draw()
                    screen.blit(text, (100, 22 + height_offset))
                    height_offset += 85
                if no_money_flag:
                    no_money = Button(
                    screen,
                    width // 2 - 100,
                    height // 2 - 25,
                    300,
                    50,
                    text="No tienes dinero",
                    fontSize=30,
                    margin=10,
                    inactiveColour=RED,
                    hoverColour=ACCENT,
                    pressedColour=DARK,
                    onClick=lambda: globals().update(no_money_flag=False)
                    )
                    buttons.append([no_money])         
            else:
                with open("food_bought.txt", "r") as f:
                    for i in f:
                        name, image, health, value = i.strip().split(" | ")
                        bought_food.append(food(name, image, int(health), int(value)))
                if bought_food:
                    screen.blit(arrowright_bottom, arrowright_bottom_rect)
                    screen.blit(arrowleft_bottom, arrowleft_bottom_rect)
                    bought_food[food_index].rect.midbottom = (width // 2, height)          
                    buttons.append([bought_food[food_index]])
                    bought_food[food_index].draw()
                else:
                    screen.blit(no_food_text, no_food_rect)
                    
            
    pygame_widgets.update(event)
    pygame.display.update()
    




