import pygame

height = 600
width = 800
white = (255,255,255)
black = (0,0,0)
grey = (128,128,128)
pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Buckshot Roullete")
font = pygame.font.Font("monogram-extended.ttf", 40) 


text_easy = font.render("Easy mode description", True, grey)
text_normal = font.render("Normal mode description", True, grey)
text_hard = font.render("Hard mode description", True, grey)

text_general_return = font.render("Press return to go back", True,grey)
text_volumen = font.render("Volumen",True, grey)
text_options_difficulty = font.render("Modo de dificultad",True,grey)
text_enter = font.render("Press enter to start", True, grey)
# ------------------- load images background gif ----------------------
zero = pygame.image.load("1.png").convert()
zero_scale = pygame.transform.scale(zero,(width,height))

one = pygame.image.load("1.png").convert()
one_scale = pygame.transform.scale(one,(width,height))

two= pygame.image.load("1.png").convert()
two_scale = pygame.transform.scale(two,(width,height))

three = pygame.image.load("1.png").convert()
three_scale = pygame.transform.scale(three,(width,height))

four = pygame.image.load("1.png").convert()
four_scale = pygame.transform.scale(four,(width,height))

five = pygame.image.load("1.png").convert()
five_scale = pygame.transform.scale(five,(width,height))

six = pygame.image.load("1.png").convert()
six_scale = pygame.transform.scale(one,(width,height))

seven = pygame.image.load("1.png").convert()
seven_scale = pygame.transform.scale(one,(width,height))

eight = pygame.image.load("1.png").convert()
eight_scale = pygame.transform.scale(one,(width,height))

nine = pygame.image.load("1.png").convert()
nine_scale = pygame.transform.scale(one,(width,height))

one = pygame.image.load("1.png").convert()
one_scale = pygame.transform.scale(one,(width,height))

one = pygame.image.load("1.png").convert()
one_scale = pygame.transform.scale(one,(width,height))

one = pygame.image.load("1.png").convert()
one_scale = pygame.transform.scale(one,(width,height))

one = pygame.image.load("1.png").convert()
one_scale = pygame.transform.scale(one,(width,height))

one = pygame.image.load("1.png").convert()
one_scale = pygame.transform.scale(one,(width,height))

one = pygame.image.load("1.png").convert()
one_scale = pygame.transform.scale(one,(width,height))

one = pygame.image.load("1.png").convert()
one_scale = pygame.transform.scale(one,(width,height))

one = pygame.image.load("1.png").convert()
one_scale = pygame.transform.scale(one,(width,height))

one = pygame.image.load("1.png").convert()
one_scale = pygame.transform.scale(one,(width,height))

one = pygame.image.load("1.png").convert()
one_scale = pygame.transform.scale(one,(width,height))

one = pygame.image.load("1.png").convert()
one_scale = pygame.transform.scale(one,(width,height))

#------------------------------ play - cambiar
play1 = pygame.image.load("PLAY1 r.png").convert()
play2 = pygame.image.load("PLAY2 r.png").convert()

play1_scale = pygame.transform.scale(play1, (175,75))
play2_scale = pygame.transform.scale(play2, (175,75))

#------------------------------ options - cambiar
options1 = pygame.image.load("OPTIONS1 r.png").convert()
options2 = pygame.image.load("OPTIONS2 r.png").convert()

options1_scale = pygame.transform.scale(options1,(175,75))
options2_scale = pygame.transform.scale(options2,(175,75))

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

    def draw_button(self, surface):
        surface.blit(self.image, self.rect)
        if self.hovered== True:
            pygame.draw.polygon(surface, (50, 50, 50), [
                (self.rect.left - 5, self.rect.centery),
                (self.rect.left - 25, self.rect.centery - 15),
                (self.rect.left - 25, self.rect.centery + 15 )
            ])

    def handle_event(self):
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

def show_play_screen():
    global actual_screen
    actual_screen = "play_screen"

def show_options_screen():
    global actual_screen
    actual_screen = "options_screen"

def show_options_easy():
    global actual_screen
    actual_screen == "easy_mode_screen"

def show_options_normal():
    global actual_screen
    actual_screen == "normal_mode_screen"

def show_options_hard():
    global actual_screen
    actual_screen == "hard_mode_screen"

buttons = [
    Button(play1_scale,play2_scale,width//2,250, show_play_screen),
    Button(options1_scale,options2_scale,width//2,400, show_options_screen)
    Button(hard1_scale,hard2_scale, width//2,400, show_options_mode)
    Button(easy1_scale,easy2_scale, widht//2,400, show_options_mode)
    Button(normal1_scale,normal2_scale,width//2,400, show_options_mode)
    ]

running = True
actual_screen = "main_screen"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if actual_screen == "main_screen":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    actual_screen = "menu_screen"
        
        elif actual_screen == "menu_screen":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    actual_screen = "main_screen"
        elif actual_screen == "options_screen":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    actual_screen = "menu_screen"
        elif actual_screen == "easy_mode_screen" or actual_screen == "normal_mode_screen" or actual_screen == "hard_mode_screen":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    actual_screen = "options_screen"
        
        
    if actual_screen == "main_screen":
        screen.fill(black)
        screen.blit(text_enter,(250,500))

    elif actual_screen == "menu_screen":
        screen.fill(black)
        screen.blit(zero_scale, (0,0))
    
    elif actual_screen == "play_screen":
        screen.fill(black)

    elif actual_screen == "options_screen":
        screen.fill(black)
        screen.blit(text_options_difficulty, (0,0))
        screen.blit(text_volumen, (0,0))
    
    elif actual_screen == "easy_mode":
        screen.fill(black)
        screen.blit(text_easy(0,0))
        screen.blit(text_general_return(0,0))

    elif actual_screen == "normal_mode":
        screen.fill(black)
        screen.blit(text_normal(0,0))
        screen.blit(text_general_return(0,0))

    elif actual_screen == "hard_mode":
        screen.fill(black)
        screen.blit(text_hard(0,0))
        screen.blit(text_general_return(0,0))

    pygame.display.flip()

pygame.quit()