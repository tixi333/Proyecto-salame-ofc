import pygame

height= 600
width = 800

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((width, height)) 
pygame.display.set_caption("Cuida a tu salame")
    
black = (0,0,0)
white = (255,255,255) 
grey = (128,128,128)
font = pygame.font.Font("monogram-extended.ttf", 100) 

font = pygame.font.Font("monogram-extended.ttf", 50) 
text_play = font.render("play screen", True, grey)
text_options = font.render("options screen", True, grey)

text_exit = font.render("ESC go back to menu", True, grey)
text_exit = font.render("ESC - (go back)", True, grey)

back = pygame.image.load("menu.jpg").convert()
back_scale = pygame.transform.scale(back, (width, height)) 

title = pygame.image.load("title.png").convert_alpha()
title_scale = pygame.transform.scale(title,(500,100))
title_scale_rect = title_scale.get_rect(center= (width//2, 100))

back_buttons = pygame.image.load("frame3.png").convert()
back_buttons_scale = pygame.transform.scale(back_buttons,(width, height))
back_buttons_scale_rect = back_buttons_scale.get_rect(center= (width//2, height//2))

## ---------------- Text
            #      Credits       #
t_credits1 = font.render("Game developed by:", True, grey)
t_credits2 = font.render("- Ticiana Ramirez", True, grey)
t_credits3 = font.render("- Benjamin Ramirez", True, grey)
t_credits4 = font.render("- Mercedes Kuroki", True, grey)
## ---------------- Class Button

class Button:
    def __init__(self,image1,image2,x,y,action):
        self.image1 = image1
        self.image2 = image2
        self.image = self.image1
        self.x = x
        self.y = y
        self.action = action
        self.rect = self.image1.get_rect(center = (self.x,self.y))
        self.hovered= False
    def draw_button(self,surface):
        surface.blit(self.image, self.rect)
        if self.hovered:
            pygame.draw.polygon(surface, (50, 50, 50), [
                (self.rect.left - 5, self.rect.centery),
                (self.rect.left - 25, self.rect.centery - 15),
                (self.rect.left - 25, self.rect.centery + 15 )
            ])
    
    def event(self,event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.image = self.image2
                self.hovered = True
            else:
                self.image = self.image1
                self.hovered = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()
                
## --------- functions for each button

def show_play_screen():
    global actual_screen
    actual_screen = "play_screen"

def show_options_screen():
    global actual_screen
    actual_screen = "options_screen"

def show_credits_screen():
    global actual_screen
    actual_screen = "credits_screen"

## -------------  Button set

play1 = pygame.image.load("PLAY1 r.png").convert()
play2 = pygame.image.load("PLAY2 r.png").convert()

play1_scale = pygame.transform.scale(play1, (175,75))
play2_scale = pygame.transform.scale(play2, (175,75))

options1 = pygame.image.load("OPTIONS1 r.png").convert()
options2 = pygame.image.load("OPTIONS2 r.png").convert()

options1_scale = pygame.transform.scale(options1,(175,75))
options2_scale = pygame.transform.scale(options2,(175,75))

credits1 = pygame.image.load("CREDITS1 r.png").convert()
credits2 = pygame.image.load("CREDITS2 R.png").convert()

credits1_scale = pygame.transform.scale(credits1,(175,75))
credits2_scale = pygame.transform.scale(credits2,(175,75))


buttons = [
    Button(play1_scale,play2_scale,width//2,250, show_play_screen),
    Button(options1_scale,options2_scale,width//2,400, show_options_screen),
    Button(credits1_scale,credits2_scale,width//2,550, show_credits_screen)
    ]

## ------------------------ Bucle
running = True
actual_screen = "menu"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                actual_screen = "menu"
    if actual_screen == "menu":
        for button in buttons:
            button.event(event)
    
    
    if actual_screen == "menu":
        screen.blit(back_scale,(0,0))
        screen.blit(title_scale,title_scale_rect)
        for button in buttons:
            button.draw_button(screen)
            
    elif actual_screen == "play_screen":
        screen.blit(back_buttons_scale,(0,0))
        screen.blit(text_play,(100,100))
        screen.blit(text_exit,(300,500))
        
    elif actual_screen== "options_screen":
        screen.blit(back_buttons_scale,(0,0))
        screen.blit(text_options,(100,100))
        screen.blit(text_exit,(300,500))
    elif actual_screen == "credits_screen":
        screen.blit(back_buttons_scale,(0,0))
        screen.blit(t_credits1, (250,100))
        screen.blit(t_credits2, (250,150))
        screen.blit(t_credits3, (250,200))
        screen.blit(t_credits4,(250,250))
        screen.blit(text_exit,(300,500))
    pygame.display.flip()

pygame.quit()