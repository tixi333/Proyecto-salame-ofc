
import pygame, pygame_widgets, os, time, subprocess, sys, unicodedata
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
CREAM = (255, 251, 209)
pygame.display.set_caption("Cuida a tu salame")
pygame.display.set_icon(pygame.image.load("salame.png").convert_alpha())
font = pygame.font.Font("monogram-extended.ttf", 36)
#-------------------acceder a un archivo --------------------------------------------------------------------
def get_path(filename):
    path = f"salame/files_main/{filename}"
    path = os.path.abspath(path)
    return path
#--------------------------------seteo daño salud--------------------------------------------------------------
current_time = time.time()
try:
    with open(get_path("lasttime.txt"), "r") as f:
        last_time = f.readline().strip()
        last_time = float(last_time) 
except Exception:
    last_time = current_time
elapsed_time = current_time - last_time
health_decrease = int(elapsed_time // 3600) * 5
with open(get_path("health.txt"), "r") as f:
    current_health = f.readline().strip()
    current_health = int(current_health)
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

#-------------------funcion renderizar plata-------------------------
def render_money():
    global money_value
    text_surface = font.render(str(money_value), True, BLACK)
    rect = text_surface.get_rect()
    rect.topleft = (55, 15)
    screen.blit(text_surface, rect)
#---------------------------------------------------------------clases salame y comida-----------------------------------------------------
class Salame:
    def __init__(self, image, current_health=current_health):
        self.health = current_health
        self.happiness = 100
        self.image = pygame.image.load(get_path(image)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (400, 400))
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# instancia salame
salame = Salame("salame_normal.png")

class Food:
    def __init__(self, name, image_name, health, value, rect=None):
        self.name = name
        self.image_name = image_name
        self.health = health
        self.value = value
        self.image = pygame.image.load(get_path(image_name)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (85, 85))
        if rect == None:
            self.rect = pygame.Rect(0, 0, 85, 85)
            self.rect.midbottom = (width // 2, height)
        else:
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
        global button_flag_state, button_flag_type, bought_food, salame, buymenu, money_value, food_index
        if buymenu:
            if money_value >= self.value:
                if len(bought_food) < 5:
                    money_value -= self.value
                    bought_item = Food(self.name, self.image_name, self.health, self.value)
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
            if food_index >= len(bought_food):
                food_index = max(0, len(bought_food) - 1)

    def hide(self):
        self.button.hide()

#----------------------------seteo comida comprada---------------------------------
bought_food = []
if os.path.getsize(get_path("food_bought.txt")) > 1:
    with open(get_path("food_bought.txt"), "r") as f:
        for i in f:
            name, image_name, health, value = i.strip().split(" | ")
            bought_food.append(Food(name, image_name, int(health), int(value)))

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

#cuando un minijuego corre
minigame_text = font.render("Minijuego en curso...", True, WHITE)
minigame_rect = minigame_text.get_rect()
minigame_rect.center = (width // 2, height // 2)

#textbox
skin_text = font.render("¡Usa <a> y <d> para ponerle trajes al salame!", True, BLACK)
skin_text_rect = no_food_text.get_rect()
skin_text_rect.bottomleft = (100, height)
#-------------------------------botón de info--------------------------------
info_text = ''
def info_display():
    global show_info
    show_info = True

info_button = Button(
                screen,
                400, 
                10, 
                390, 
                46,
                font=font,
                text="Presiona acá para info",
                onClick=info_display,
                inactiveColour=PURPLE,
                hoverColour=ACCENT,
                pressedColour=GRAY
            )
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
    completedColour=GREEN,
    incompletedColour=GRAY,
    )
health_bar.show()

#------------------------------------------------------------------------------------------------------------------------------
# para manejar fondos
backgrounds = (cocina, fondo_general, fondo_general, fondo_general)
current_background = backgrounds[0]
index = 0
dif_background = True

show_info = False
buymenu = False

# trajes
current_skin = "salame_normal.png"
skin_index = 0
last_skin_index = 0

# para manejar la comida comprada
food_index = 0

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
            foods_on_page.append(Food(name, image_name, int(health), int(value)))
    return foods_on_page
#------------------------------------------------------------interacción con salame------------------------------------------------------
#para hablarle al salame
salame_reply = ""
salame_wait = False
salame_reply_rendered = ""
def normalize_unicode(text):
    normalized_text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
    return normalized_text
def ask_salame():
    global salame_reply, salame_wait, textbox
    textbox_text = textbox.getText()
    textbox_text = normalize_unicode(textbox_text)
    if salame_wait or not textbox_text.strip():
        return
    else:
        salame_wait = True
        textbox.setText("El salamín está pensando... no escribas nada")
        try:
            salame_reply = subprocess.run([sys.executable, get_path('mainai.py')], input=textbox_text, timeout=30, capture_output=True, text=True, check=True)
        except subprocess.TimeoutExpired:
            salame_reply = 'Tu salame quiere dormir!'
        except subprocess.CalledProcessError as e:
            print("❌ AI subprocess failed:")
            print("Return code:", e.returncode)
            print("STDERR:\n", e.stderr)
            salame_reply = 'El salame va a guardar sus secretos' 
        else:
            salame_reply = normalize_unicode(salame_reply.stdout)
        finally:
            textbox.setText("")
            salame_wait = False
            return

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
    def __init__(self, name, script_path, rect_value_1, rect_value_2, image="gamebutton.png"):
        self.name = name
        self.rect = pygame.Rect(rect_value_1, rect_value_2, 235, 75)
        self.script_path = os.path.abspath(script_path)
        self.image = pygame.image.load(get_path(image)).convert_alpha()
        self.button = self.button = Button(
                screen,
                int(self.rect.x),
                int(self.rect.y),
                int(self.rect.width),
                int(self.rect.height),
                text=str(self.name),
                font=font,
                fontSize=50,
                onClick=self.run,
                image=self.image
            )
    def run(self):
        global minigame_text, minigame_rect
        process = subprocess.Popen([sys.executable, self.script_path])
        screen.fill(DARK)
        screen.blit(minigame_text, minigame_rect)
        pygame.display.update()
        process.wait()

    def hide(self):
        self.button.hide()
    def show(self):
        self.button.show()

lluvia_comida = GameButton("Lluvia de comida", r"Mini_Juego_LLC\LluviaComida.py", 10, 140)
blackjack = GameButton("Blackjack", r"Blackjack\blackjack.py", 10, 400)
pong =  GameButton("Poung", r"PONG\PINGPOUNG.py", 555, 140)
buckshot = GameButton("Buckshot",r"Buckshot Roulette\buckshotroulette.py", 555, 400)
        

#left_mid_rect = pygame.Rect(90, 245, 120, 90)
#right_mid_rect = pygame.Rect(590, 245, 120, 90)
        
#------------------------------------------------------------manejo de botones------------------------------------------------------
general_buttons = []
button_flag = None
button_flag_state = False
button_flag_text = ""
flag_cooldown = 0

def flag_button(text):
    global button_flag, button_flag_state, button_flag_text, flag_cooldown
    if button_flag_state and button_flag_text == text:
        return  
    kill_button_flag()  

    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(width // 2, height // 2))

    button_flag = Button(
        screen,
        text_rect.x - 10,
        text_rect.y - 10,
        text_rect.width + 20,
        text_rect.height + 20,
        text=text,
        font=font,
        fontSize=25,
        margin=10,
        inactiveColour=PURPLE,
        hoverColour=RED,
        pressedColour=RED,
        onClick=kill_button_flag
    )

    button_flag_state = True
    button_flag_text = text
    flag_cooldown = time.time()  


def kill_button_flag():
    global button_flag, button_flag_state, button_flag_text, salame_reply, salame_reply_rendered
    if button_flag:
        button_flag.hide()
        button_flag = None
    button_flag_state = False
    button_flag_text = ""
    salame_reply = ""
    salame_reply_rendered = False

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
            with open(get_path("lasttime.txt"), "w") as f:
                f.write(str(time.time()))
            with open(get_path("health.txt"), "w") as f:
                f.write(str(salame.health))
            with open(get_path("food_bought.txt"), "w") as f:
                for i in bought_food:
                    f.write(f"{i.name} | {i.image_name} | {i.health} | {i.value}\n")
            with open('money.txt', 'w') as f:
                f.write(str(money_value))
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                index = (index - 1) % len(backgrounds)
                dif_background = True
            elif event.key == pygame.K_RIGHT:
                index = (index + 1) % len(backgrounds)
                dif_background = True
            elif event.key == pygame.K_RETURN:
                if show_info:
                    info_text = ''
                    show_info = not show_info
            elif event.key == pygame.K_b:
                if index == 0:
                    buymenu = not buymenu
            elif event.key == pygame.K_a:
                if buymenu:
                    current_page = (current_page - 1) % total_pages
                elif index == 0 and bought_food:
                    food_index = (food_index - 1) % len(bought_food)
                elif current_background == fondo_general and index == 3:
                    skin_index = (skin_index - 1) % 7
            elif event.key == pygame.K_d:
                if buymenu:
                    current_page = (current_page + 1) % total_pages
                elif index == 0 and bought_food:
                    food_index = (food_index + 1) % len(bought_food)
                elif current_background == fondo_general and index == 3:
                    skin_index = (skin_index + 1) % 7

    current_background = backgrounds[index]
    if dif_background:
        textbox.hide()
        buckshot.hide()
        blackjack.hide()
        lluvia_comida.hide()
        pong.hide()
        dif_background = False

    if button_flag_state and button_flag is not None:
        pygame_widgets.update(events)
        pygame.display.update()
        continue
    elif show_info:
        screen.fill(WHITE)
        if not info_text:
            match index:
                case 0:
                    info_text = "info_food.txt"
                case 1:
                    info_text = "info_textbox.txt"
                case 2:
                    info_text = "info_games.txt"
                case 3:
                    info_text = "info_skins.txt"

            with open(get_path(info_text), "r", encoding="utf-8") as f:
                info_text = f.read()
                info_text = info_text.splitlines()

        height_offset = 10
        for line in info_text:
            rendered_line = font.render(line, True, BLACK)
            line_rect = rendered_line.get_rect()
            line_rect.topleft = (10, height_offset)
            screen.blit(rendered_line, line_rect)
            height_offset += line_rect.height + 5
        pygame.display.update() 
        continue
    else:
        screen.blit(current_background, (0, 0))
        salame.draw(screen)
        screen.blit(arrowright, arrowright_back_rect)
        screen.blit(arrowleft, arrowleft_back_rect)
        health_bar.show()
        render_money()
        screen.blit(money_image, money_image_rect)

        match index:
            case 0:  
                if buymenu:
                    screen.fill(WHITE)
                    health_bar.hide()
                    info_button.hide()
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
                        if food_index < 0 or food_index >= len(bought_food):
                            food_index = 0
                        general_buttons.append([bought_food[food_index]])
                        bought_food[food_index].draw()
                    else:
                        food_index = 0  
                        screen.blit(no_food_text, no_food_rect)

            case 1:
                textbox.show()
                if salame_reply and not salame_reply_rendered:
                    flag_button(salame_reply)
                    salame_reply_rendered = True

            case 2:
                buckshot.show()
                blackjack.show()
                lluvia_comida.show()
                pong.show()

            case 3:
                screen.blit(skin_text, skin_text_rect)
                if last_skin_index != skin_index:
                    with open(get_path("skins.txt"), "r") as f:
                        for index_skin, skin in enumerate(f):
                            if index_skin == skin_index:
                                current_skin = skin.strip()
                    salame.image = pygame.image.load(get_path(current_skin)).convert_alpha()
                    salame.image = pygame.transform.scale(salame.image, (400, 400))
                    last_skin_index = skin_index

        pygame_widgets.update(events)
        pygame.display.update()