import pygame

height = 600
width = 800
white = (255,255,255)
black = (0,0,0)
grey = (128,128,128)
red = (139,0,0)

pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Buckshot Roullete")  

fontr = pygame.font.Font("EBGaramond-VariableFont_wght.ttf", 100)
#----------------- FONT
font = pygame.font.Font("monogram-extended.ttf", 40) 
font2 = pygame.font.Font("monogram-extended.ttf", 50)
#----------------------- menu

title_game = fontr.render("Buckshot",True,grey)
title_game2 = fontr.render("Roulette",True,grey)

#----------------- play screen text (provisorio)
text_play = font.render("Play", True, grey)

#------------------ options screen text 
text_options = font.render("Options", True, grey)

text_easy = font.render("Easy mode description", True, grey)
text_normal = font.render("Normal mode description", True, grey)
text_hard = font.render("Hard mode description", True, grey)
text_volumen = font.render("Volumen",True, grey)
text_options_difficulty = font.render("Modo de dificultad",True,grey)

#----------------- return text
text_general_return = font.render("Press return to go back", True,grey)
text_enter = font.render("Press enter to start", True, grey)

#- ---------------- menu buttons
text_play = font2.render("Play",True, red)
text_play2 = font2.render("Play", True, grey)

text_options = font2.render("Options", True, red)
text_options2 = font2.render("Options", True, grey)

# ------------------- load images background gif ----------------------
zero = pygame.image.load("0.png").convert()
zero_scale = pygame.transform.scale(zero,(width,height))

one = pygame.image.load("1.png").convert()
one_scale = pygame.transform.scale(one,(width,height))

two= pygame.image.load("2.png").convert()
two_scale = pygame.transform.scale(two,(width,height))

three = pygame.image.load("3.png").convert()
three_scale = pygame.transform.scale(three,(width,height))

four = pygame.image.load("4.png").convert()
four_scale = pygame.transform.scale(four,(width,height))

five = pygame.image.load("5.png").convert()
five_scale = pygame.transform.scale(five,(width,height))

six = pygame.image.load("6.png").convert()
six_scale = pygame.transform.scale(six,(width,height))

seven = pygame.image.load("7.png").convert()
seven_scale = pygame.transform.scale(seven,(width,height))

eight = pygame.image.load("8.png").convert()
eight_scale = pygame.transform.scale(eight,(width,height))

nine = pygame.image.load("9.png").convert()
nine_scale = pygame.transform.scale(nine,(width,height))

ten = pygame.image.load("10.png").convert()
ten_scale = pygame.transform.scale(ten,(width,height))

eleven = pygame.image.load("11.png").convert()
eleven_scale = pygame.transform.scale(eleven,(width,height))

twelve = pygame.image.load("12.png").convert()
twelve_scale = pygame.transform.scale(twelve,(width,height))

thirteen = pygame.image.load("13.png").convert()
thirteen_scale = pygame.transform.scale(thirteen,(width,height))

fourteen = pygame.image.load("14.png").convert()
fourteen_scale = pygame.transform.scale(fourteen,(width,height))

fifteen = pygame.image.load("15.png").convert()
fifteen_scale = pygame.transform.scale(fifteen,(width,height))

sixteen = pygame.image.load("16.png").convert()
sixteen_scale = pygame.transform.scale(sixteen,(width,height))

seventeen = pygame.image.load("17.png").convert()
seventeen_scale = pygame.transform.scale(seventeen,(width,height))

eighteen = pygame.image.load("18.png").convert()
eighteen_scale = pygame.transform.scale(eighteen,(width,height))

nineteen = pygame.image.load("19.png").convert()
nineteen_scale = pygame.transform.scale(nineteen,(width,height))

#------------------------------ play - cambiar
#play1 = pygame.image.load("playbr1.png").convert()
#play2 = pygame.image.load("playbr2.png").convert()

#play1_scale = pygame.transform.scale(play1, (175,75))
#play2_scale = pygame.transform.scale(play2, (175,75))

#------------------------------ options - cambiar
#options1 = pygame.image.load("options br1.png").convert()
#options2 = pygame.image.load("options br2.png").convert()

#options1_scale = pygame.transform.scale(options1,(175,75))
#options2_scale = pygame.transform.scale(options2,(175,75))

# ---------------------------
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

            pygame.draw.polygon(surface, (grey), [
                (self.rect.left - 5, self.rect.centery),
                (self.rect.left - 25, self.rect.centery - 15),
                (self.rect.left - 25, self.rect.centery + 15 )
            ])

    def handle_event(self,event):
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

class BloodDrop:
    def __init__(self, x, y, radius=8, speed=1):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.reset_y = y

    def update(self, height):
        self.y += self.speed
        if self.y > height:
            self.y = self.reset_y

    def draw(self, surface):
        pygame.draw.circle(surface, red, (self.x, int(self.y)), self.radius)
        pygame.draw.polygon(surface, red, [
            (self.x - self.radius//2, int(self.y)),
            (self.x + self.radius//2, int(self.y)),
            (self.x, int(self.y) - self.radius*2)
        ])


blood_drop = BloodDrop(250, y=200, radius=8, speed=0.2)
#---------- functions

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

#----------- button
buttons = [
    Button(text_play,text_play2,100,250, show_play_screen),
    Button(text_options,text_options2,100,400,show_options_screen)
    ]
    #Button(hard1_scale,hard2_scale, width//2,400, show_options_mode)
    #Button(easy1_scale,easy2_scale, widht//2,400, show_options_mode)
    #Button(normal1_scale,normal2_scale,width//2,400, show_options_mode)
    #Button(play1_scale,play2_scale,100,250, show_play_screen),
    #Button(options1_scale,options2_scale,100,400, show_options_screen)
    # añadir a buttons cuando esten cargadas las imagenes
#------------- background images

background_frames = [
    zero_scale, one_scale, two_scale, three_scale, four_scale, five_scale,
    six_scale, seven_scale, eight_scale, nine_scale, ten_scale, eleven_scale,
    twelve_scale, thirteen_scale, fourteen_scale, fifteen_scale, sixteen_scale,
    seventeen_scale, eighteen_scale, nineteen_scale
]
frame_index = 0
frame_delay = 100
last_update = pygame.time.get_ticks()

running = True
actual_screen = "main_screen"
#--------------- bucle
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
                if event.key == pygame.K_BACKSPACE:
                    actual_screen = "main_screen"
            for button in buttons:
                button.handle_event(event)


        elif actual_screen == "options_screen":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    actual_screen = "menu_screen"
            for button in buttons:
                    button.handle_event(event)
            
        elif actual_screen == "easy_mode_screen" or actual_screen == "normal_mode_screen" or actual_screen == "hard_mode_screen":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    actual_screen = "options_screen"

        elif actual_screen == "play_screen":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    actual_screen = "menu_screen" #provisorio
        
    if actual_screen == "main_screen":
        screen.fill(black)
        current_time = pygame.time.get_ticks()
        if current_time - last_update > frame_delay:
            frame_index = (frame_index + 1) % len(background_frames)
            last_update = current_time      
        screen.blit(background_frames[frame_index], (0, 0))
        screen.blit(text_enter,(250,500))
        screen.blit(title_game,(240,0))
        screen.blit(title_game2,(250,100))
        blood_drop.update(height)
        blood_drop.draw(screen)

    elif actual_screen == "menu_screen":
        #background -----------------------
        screen.fill(black)
        screen.blit(zero_scale, (0,0))
        current_time = pygame.time.get_ticks()

        if current_time - last_update > frame_delay:
            frame_index = (frame_index + 1) % len(background_frames)
            last_update = current_time      
        screen.blit(background_frames[frame_index], (0, 0))
        # ---------------------------------------------
        for button in buttons:
            button.draw_button(screen)  

    elif actual_screen == "play_screen":   #screen
        screen.fill(black)
        screen.blit(text_play,(0,0))
    elif actual_screen == "options_screen":   #screen
        screen.fill(black)
        screen.blit(text_options_difficulty, (0,0))
        screen.blit(text_volumen, (0,0))
        screen.blit(text_options, (0,0))
    
    elif actual_screen == "easy_mode":   #options
        screen.fill(black)
        screen.blit(text_easy(0,0))
        screen.blit(text_general_return(0,0))

    elif actual_screen == "normal_mode": #options
        screen.fill(black)
        screen.blit(text_normal(0,0))
        screen.blit(text_general_return(0,0))

    elif actual_screen == "hard_mode": #options
        screen.fill(black)
        screen.blit(text_hard(0,0))
        screen.blit(text_general_return(0,0))

    pygame.display.flip()

pygame.quit()