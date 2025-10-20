
import pygame, pygame_widgets, os, time, subprocess, sys
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox
from pygame_widgets.progressbar import ProgressBar
# seteo inicial
pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))  # seteo tamaño pantalla
# colores
WHITE = (245, 246, 252)
BLACK = (30, 30, 35)
GRAY = (100, 105, 115)
GREEN = (70, 190, 120)
RED = (230, 90, 90)
BLUE = (90, 150, 240)
YELLOW = (245, 210, 80)
PURPLE = (160, 120, 220)
DARK = (24, 26, 32)
ACCENT = (90, 200, 255)
pygame.display.set_caption("Cuida a tu salame")
pygame.display.set_icon(pygame.image.load("salame.png").convert_alpha())
font = pygame.font.Font("monogram-extended.ttf", 36)
client = ""
#--------------------------------seteo daño salud--------------------------------------------------------------
with open("lasttime.txt", "r") as f:
    last_time = f.read().strip()
current_time = time.monotonic()
if last_time:
    last_time = float(last_time) 
else:
    last_time = current_time
elapsed_time = current_time - last_time
health_decrease = int(elapsed_time // 3600) * 5  
with open("health.txt", "r") as f:
    if os.path.getsize("health.txt") > 0:
        current_health = int(f.read().strip())
    else:
        current_health = 100
current_health -= health_decrease
if current_health < 0:
    current_health = 0
money_value = 0
with open("money.txt", "r") as m:
    money_value_str = m.readline().strip()
    if money_value_str:
        money_value = int(money_value_str) 
    else:
        money_value = 0
#-------------------acceder a una imagen --------------------------------------------------------------------
def get_path(filename):
    path = f"salame/files_main/{filename}"
    path = os.path.abspath(path)
    return path
#-------------------funcion renderizar plata-------------------------
def render_money():
    global money_value
    text_surface = font.render(str(money_value), True, BLACK)
    rect = text_surface.get_rect()
    rect.topleft = (55, 15)
    screen.blit(text_surface, rect)
#---------------------------------------------------------------clases salame y comida-----------------------------------------------------
class Salame:
    def __init__(self, current_health=current_health):
        self.health = current_health
        self.happiness = 100
        self.image = pygame.image.load("salame.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (400, 400))
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# instancia salame
salame = Salame()

class Food:
    def __init__(self, name, image_name, health, value, rect=pygame.Rect(358, 515, 85, 85)):
        self.name = name
        self.image_name = image_name
        self.health = health
        self.value = value
        self.image = pygame.image.load(image_name).convert_alpha()
        self.image = pygame.transform.scale(self.image, (85, 85))
        self.rect = rect

    def draw(self):
        pos = (self.rect.x, self.rect.y, self.rect.width, self.rect.height)

        if not hasattr(self, 'button') or getattr(self, 'button_pos', None) != pos:
            if hasattr(self, 'button'):
                try:
                    self.button = None
                except Exception:
                    pass
            self.button = Button(
                screen,
                int(self.rect.x),
                int(self.rect.y),
                int(self.rect.width),
                int(self.rect.height),
                image=self.image,
                onClick=self.feed_or_buy
            )
            self.button_pos = pos
        else:
            self.button.show()

    def feed_or_buy(self):
        global button_flag_state, button_flag_type, bought_food, salame, buymenu, money_value
        if buymenu:
            if money_value >= self.value:
                if len(bought_food) < 10:
                    money_value -= self.value
                    new_rect = pygame.Rect(0, 0, 85, 85)
                    new_rect.midbottom = (width // 2, height)
                    bought_item = Food(self.name, self.image_name, self.health, self.value, new_rect)
                    bought_food.append(bought_item)
                else:
                    button_flag_state = True
                    button_flag_type = "max food"
            else:
                button_flag_state = True
                button_flag_type = "no money"
    
        elif current_background == cocina:
            salame.health = salame.health + self.health
            if salame.health > 100:
                salame.health = 100
            bought_food.remove(self)
            with open('food_bought.txt', 'w') as f:
                for i in bought_food:
                    f.write(f"{i.name} | {i.image_name} | {i.health} | {i.value}\n")

    def hide(self):
        self.button.hide()

#------------------------------------------------------------renders sin función--------------------------------------------------------

# flechas generales de todos los back (salvo los flags)
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

# flechas inferiores para el menú de comida comprada (sólo en el fondo azul)
arrowleft_bottom = pygame.transform.scale(arrowleft, (40, 40))
arrowleft_bottom_rect = arrowleft_bottom.get_rect()
arrowleft_bottom_rect.midbottom = (width // 2 - 100, height)
arrowright_bottom = pygame.transform.scale(arrowright, (40, 40))
arrowright_bottom_rect = arrowright_bottom.get_rect()
arrowright_bottom_rect.midbottom = (width // 2 + 100, height)
no_food_text = font.render("No tienes comida comprada", True, BLACK)
no_food_rect = no_food_text.get_rect()
no_food_rect.midbottom = (width // 2, height)

# todo lo de info
info_text = font.render("Presiona <i> para info", True, BLACK)
info_rect = info_text.get_rect()
info_rect.topleft = (475, 10)
i_text = font.render("iahygfjhjsgjhb", True, BLACK)
i_rect = i_text.get_rect()
i_rect.center = (width // 2, height // 2)

#lo de plata
money_image = pygame.image.load("coin.png").convert_alpha()
money_image = pygame.transform.scale(money_image, (40, 40))
money_image_rect = money_image.get_rect()
money_image_rect.topleft = (10, 10)
#fondos
cocina = pygame.image.load(get_path('cocina.png')).convert()
cocina = pygame.transform.scale(cocina, (width, height))
fondo_general = pygame.image.load(get_path('fondo.png')).convert()
fondo_general = pygame.transform.scale(fondo_general, (width, height))

#------------------------------------------------------------para nivel de energía------------------------------------------------------
def progress():
    return float(salame.health/100)
health_bar = ProgressBar(
    screen,
    200,                
    15,       
    180,               
    30,                
    progress=progress,
    completedColour=PURPLE,
    incompletedColour=GRAY,
    )
health_bar.show()

#------------------------------------------------------------------------------------------------------------------------------
# para manejar fondos
backgrounds = [cocina, fondo_general, fondo_general]
index = 0

# flags
show_info = False
buymenu = False

# para manejar la comida comprada
food_index = 0
bought_food = []

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
            name, image_name, health, value = line.strip().split(" | ")
            foods_on_page.append(Food(name, get_path(image_name), int(health), int(value)))
    return foods_on_page
#------------------------------------------------------------interacción con salame------------------------------------------------------
#para hablarle al salame
salame_reply = ""
def ask_salame():
    global salame_reply
    if 'salame_wait' not in locals():
        salame_wait = False
    if salame_wait == True:
        pass
    else:
        salame_wait = True
        textbox_text = textbox.getText()
        textbox.setText("El salamín está pensando... no escribas nada")
        try:
            salame_reply = subprocess.run(['python', 'mainai.py'], input=textbox_text, timeout=30, capture_output=True, text=True, check=True)
        except subprocess.TimeoutExpired:
            salame_reply = 'Tu salame quiere dormir!'
            return
        except subprocess.CalledProcessError:
            salame_reply = 'El salame va a guardar sus secretos'
        else:
            salame_reply = salame_reply.stdout
            salame_wait = False
            return
        finally:
            textbox.setText("")

   
textbox = TextBox(
    screen,
    50,                
    height - 80,       
    700,               
    60,                
    fontSize=28,
    font=font,
    borderColour=BLUE,
    textColour=BLACK,
    onSubmit=ask_salame,
    radius=10,
    borderThickness=3
)
textbox.hide()

#--------------------------------------------------botones de juegos-----------------------------
class GameButton:
    def __init__(self, name, script_path, rect, image=None):
        self.name = name
        self.rect = rect
        self.script_path = os.path.abspath(script_path)
        self.button = self.button = Button(
                screen,
                int(self.rect.x),
                int(self.rect.y),
                int(self.rect.width),
                int(self.rect.height),
                text=str(self.name),  
                fontSize=30,
                onClick=self.run
            )
    def run(self):
        command = [sys.executable, self.script_path]
        if sys.platform == "win32":
            DETACHED_PROCESS = 0x00000008
            CREATE_NEW_PROCESS_GROUP = 0x00000200
            subprocess.Popen(
                command,
                creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                close_fds=True,
            )
            running = False

        else:
            subprocess.Popen(
                command,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True,  
                close_fds=True,
            )
            running = False

    def hide(self):
        self.button.hide()
    def show(self):
        self.button.show()

lluvia_comida = GameButton("Lluvia de comida", r"Mini_Juego_LLC\LluviaComida.py", pygame.Rect(90, 140, 120, 90))
blackjack = GameButton("Blackjack", r"Mini_Juego_LLC\LluviaComida.py", pygame.Rect(90, 350, 120, 90))
pong =  GameButton("Poung", r"Mini_Juego_LLC\LluviaComida.py", pygame.Rect(590, 140, 120, 90))
buckshot = GameButton("Buckshot",r"Mini_Juego_LLC\LluviaComida.py", pygame.Rect(590, 350, 120, 90))
        

#left_mid_rect = pygame.Rect(90, 245, 120, 90)
#right_mid_rect = pygame.Rect(590, 245, 120, 90)
        
#------------------------------------------------------------manejo de botones------------------------------------------------------
general_buttons = []
button_flag_state = False
button_flag_type = ""
button_flag = None

def flag_button(text):
    global button_flag_state, button_flag
    button_flag_state = True
    text_rect = font.render(text, True, BLACK)
    text_rect = text_rect.get_rect()
    text_rect.center = (width // 2, height // 2)
    button_flag = Button(
                screen,
                text_rect.x,
                text_rect.y,
                text_rect.width + 20,
                text_rect.height + 100,
                text=text,
                font=font,
                fontSize=30,
                margin=10,
                inactiveColour=PURPLE,
                hoverColour=ACCENT,
                pressedColour=RED,
                onClick=kill_button_flag
                )
    
def kill_button_flag():
    global button_flag_state, button_flag, salame_reply
    button_flag.hide()
    button_flag = None
    button_flag_state = False
    if salame_reply:
        salame_reply = ''

def clear_buttons():
    for i in general_buttons:
        for widget in i:
            widget.hide()
        general_buttons.clear()

#------------------------------------------------------------bucle principal------------------------------------------------------

running = True
while running:
    clear_buttons()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            with open("lasttime.txt", "w") as f:
                f.write(str(time.monotonic()))
            with open("health.txt", "w") as f:
                f.write(str(salame.health))
            with open("food_bought.txt", "w") as f:
                for i in bought_food:
                    f.write(f"{i.name} | {i.image_name} | {i.health} | {i.value}\n")
            with open('money.txt', 'w') as f:
                f.write(str(money_value))
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                index = (index - 1) % len(backgrounds)
            elif event.key == pygame.K_RIGHT:
                index = (index + 1) % len(backgrounds)
            elif event.key == pygame.K_i:
                show_info = not show_info
            elif event.key == pygame.K_b:
                if index == 0:
                    buymenu = not buymenu
            elif event.key == pygame.K_a:
                if buymenu:
                    current_page = (current_page - 1) % total_pages
                elif index == 0 and bought_food:
                    food_index = (food_index - 1) % len(bought_food)
            elif event.key == pygame.K_d:
                if buymenu:
                    current_page = (current_page + 1) % total_pages
                elif index == 0 and bought_food:
                    food_index = (food_index + 1) % len(bought_food)

    current_background = backgrounds[index]

    if button_flag_state and button_flag is not None:
        pygame_widgets.update(events)
        pygame.display.update()
        continue
    elif show_info:
        screen.fill(WHITE)
        screen.blit(i_text, i_rect)
        pygame.display.update() 
        continue
    else:
        screen.blit(current_background, (0, 0))
        salame.draw(screen)
        screen.blit(arrowright, arrowright_back_rect)
        screen.blit(arrowleft, arrowleft_back_rect)
        health_bar.show()
        screen.blit(info_text, info_rect)
        render_money()
        screen.blit(money_image, money_image_rect)

        if current_background == cocina:  
            if buymenu:
                screen.fill(WHITE)
                health_bar.hide()
                page_foods = read_page(current_page)
                general_buttons.append(page_foods)
                height_offset = 0
                for current_food in page_foods:
                    current_food.rect.topleft = (10, 2 + height_offset)
                    text = font.render(f"{current_food.name} | Salud: {current_food.health} | Precio: {current_food.value}", True, BLACK)
                    current_food.draw()
                    screen.blit(text, (100, 22 + height_offset))
                    height_offset += 85
                if button_flag_state:
                    if button_flag is None:
                        if button_flag_type == "no money":
                            flag_button("No tienes suficiente dinero")
                        elif button_flag_type == "max food":
                            flag_button("No puedes comprar más comida")
            else:         
                if bought_food:
                    screen.blit(arrowright_bottom, arrowright_bottom_rect)
                    screen.blit(arrowleft_bottom, arrowleft_bottom_rect)
                    general_buttons.append([bought_food[food_index]])
                    bought_food[food_index].draw()
                elif os.path.getsize("food_bought.txt") > 1:
                            with open("food_bought.txt", "r") as f:
                                for i in f:
                                    name, image_name, health, value = i.strip().split(" | ")
                                    bought_food.append(Food(name, image_name, int(health), int(value)))
                else:
                    screen.blit(no_food_text, no_food_rect)

        if current_background == fondo_general and index == 1:
            textbox.show()
            if salame_reply:
                flag_button(salame_reply)
        else:
            textbox.hide()
        
        if current_background == fondo_general and index == 2:
            buckshot.show()
            blackjack.show()
            lluvia_comida.show()
            pong.show()
        else:
            buckshot.hide()
            blackjack.hide()
            lluvia_comida.hide()
            pong.hide()


        pygame_widgets.update(events)
        pygame.display.update()