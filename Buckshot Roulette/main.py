import pygame
import random
from setup import init_pygame
from resources import load_resources
from game import run_game

init_pygame()
resources = load_resources()


screen = pygame.display.set_mode((resources["width"],resources["height"]))
pygame.display.set_caption("Buckshot Roullete")  

actual_screen = "main_screen"

class Button:
    def __init__(self,image1,image2,x,y,action,function,text):
        self.image1 = image1
        self.image2 = image2
        self.image = self.image1 
        self.x = x
        self.y = y
        self.action = action
        self.rect = self.image1.get_rect(center = (self.x,self.y))
        self.hovered= False
        self.function = function
        self.text = text

    def draw_button(self, surface):
        surface.blit(self.image, self.rect)
        if self.hovered== True:
            if self.function == "menu":
                pygame.draw.circle(surface, resources["colors"][1], (self.rect.left - 10, self.rect.centery ), 5)
            if self.text != False:
                surface.blit(self.text, (50, 500))

    def handle_event(self,event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.image = self.image2
                self.hovered = True
            else:
                self.image = self.image1
                self.hovered = False
        if self.text == False:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.action()
                
class Activate:
    def __init__(self,color1,color2,x,y,width,height,current_mode):
        self.color1 = color1
        self.color2 = color2
        self.state = False
        self.rect = pygame.Rect(x,y,width,height)
        self.current = current_mode
    def draw_button(self,surface):
        if self.state == True:
            self.actual_color = self.color2
        else:
            self.actual_color = self.color1
        
        pygame.draw.rect(surface, self.actual_color, self.rect)
        if self.state == True:
            screen.blit(self.current, (350,200))

    def handle_event(self,button_activate,event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                for button in button_activate:
                    button.state = False
                self.state = True
            else:
                self.state = False

def play_screen ():
    global actual_screen
    actual_screen = "play_screen"

def options ():
    global actual_screen
    actual_screen = "options_screen"

def how2play():
    global actual_screen
    actual_screen = "how2play_screen"

def options_easy():
    global actual_screen
    actual_screen = "easy"

def options_normal():
    global actual_screen
    actual_screen = "normal"

def options_hard():
    global actual_screen
    actual_screen = "hard"

button_activate = [
    Activate(resources["colors"][0],resources["colors"][1],150, 255, 30, 30,resources["options"]["current_mode_easy"]),
    Activate(resources["colors"][0],resources["colors"][1], 150, 305, 30, 30,resources["options"]["current_mode_normal"]),
    Activate(resources["colors"][0],resources["colors"][1], 150, 355, 30, 30,resources["options"]["current_mode_hard"])
]

buttons_menu = [
    Button(resources["menu"]["text_play"][0],resources["menu"]["text_play"][1],90,250, play_screen,"menu",False),
    Button(resources["menu"]["text_options"][0],resources["menu"]["text_options"][1],115,300,options,"menu",False),
    Button(resources["menu"]["text_how2play"][0],resources["menu"]["text_how2play"][1],155,350,how2play,"menu",False)
    ]

buttons_options = [
    Button(resources["options"]["desc_easy"][0],resources["options"]["desc_easy"][1],400,265, options_easy, "options",resources["options"]["description_easy_g"]),
    Button(resources["options"]["desc_normal"][0],resources["options"]["desc_normal"][1],400,315, options_normal, "options",resources["options"]["description_normal_g"]),
    Button(resources["options"]["desc_hard"][0],resources["options"]["desc_hard"][1],400,365, options_hard, "options",resources["options"]["description_hard_g"]),
    ]

frame_index = 0
frame_delay = 100
last_update = pygame.time.get_ticks()


def draw(last_update,frame_index):
    if actual_screen == "main_screen":
        screen.fill(resources["colors"][3])
        current_time = pygame.time.get_ticks()
        if current_time - last_update > frame_delay:
            frame_index = (frame_index + 1) % len(resources["background"])
            last_update = current_time      
        screen.blit(resources["background"][frame_index], (0, 0))
        screen.blit(resources["general"][1],(250,500))
        screen.blit(resources["title"][0],(240,0))
        screen.blit(resources["title"][1],(250,100))

    elif actual_screen == "menu_screen":
        #background -----------------------
        screen.fill(resources["colors"][3])
        current_time = pygame.time.get_ticks()

        if current_time - last_update > frame_delay:
            frame_index = (frame_index + 1) % len(resources["background"])
            last_update = current_time      
        screen.blit(resources["background"][frame_index], (0, 0))
        # ---------------------------------------------
        for button in buttons_menu:
            button.draw_button(screen)  

    elif actual_screen == "play_screen":   #screen
        screen.fill(resources["colors"][3])
        run_game(screen)
    
    elif actual_screen == "options_screen":   #screen
        screen.fill(resources["colors"][3])
        screen.blit(resources["difficulty"], (50,200))
        screen.blit(resources["volumen"], (50,100))
        screen.blit(resources["options_text"], (200,20))
        screen.blit(resources["options"]["difficulty"][0],(50,250))
        screen.blit(resources["options"]["difficulty"][1],(50,300))
        screen.blit(resources["options"]["difficulty"][2],(50,350))
        pygame.draw.line(screen, resources["colors"][1], (50,150), (700,150), 2)
        pygame.draw.line(screen, resources["colors"][1], (50,240), (700,240), 2)
        pygame.draw.line(screen, resources["colors"][1], (50,400), (700,400), 2)

        for button in buttons_options:
            button.draw_button(screen)
        
        for button in button_activate:
            button.draw_button(screen)
    
    elif actual_screen == "how2play_screen":  
        screen.fill(resources["colors"][3])
        screen.blit(resources["general"][0],(0,0))

    pygame.display.flip()
    return last_update, frame_index

play_started = False
running = True

while running:
    last_update, frame_index = draw(last_update, frame_index)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if actual_screen == "main_screen":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    actual_screen = "menu_screen"
        
        elif actual_screen == "menu_screen":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    actual_screen = "main_screen"
            for button in buttons_menu:
                button.handle_event(event)


        elif actual_screen == "options_screen":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    actual_screen = "menu_screen"
            for button in buttons_options:
                b_selected = False

                button.handle_event(event)

            for button in button_activate:
                button.handle_event(button_activate, event)

        elif actual_screen == "how2play_screen":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    actual_screen = "menu_screen"
            
        elif actual_screen == "easy_mode_screen" or actual_screen == "normal_mode_screen" or actual_screen == "hard_mode_screen":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    actual_screen = "options_screen"

    draw(last_update,frame_index)
    pygame.display.flip()

pygame.quit()