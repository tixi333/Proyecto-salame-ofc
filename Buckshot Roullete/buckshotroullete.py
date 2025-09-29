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

text_easy_d2 = font.render("Easy mode description", True, grey)
text_normal_d2 = font.render("Normal mode description", True, grey)
text_hard_d2 = font.render("Hard mode description", True, grey)

text_easy_d = font.render("Easy mode description", True, red)
text_normal_d = font.render("Normal mode description", True, red)
text_hard_d = font.render("Hard mode description", True, red)

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

text_how2play = font2.render("How to play", True, red)
text_how2play2 = font2.render("How to play", True, grey)

#------------------ difficulty buttons

text_select= font.render("Select difficulty", True, grey)
text_easy = font.render("Easy", True, red)
text_easy2 = font.render("Easy", True, grey)

text_normal = font.render("Normal", True, red)
text_normal2 = font.render("Normal", True, grey)

text_hard = font.render("Hard", True, red)
text_hard2 = font.render("Hard", True, grey)

# ------------------- load images background gif ----------------------
zero = pygame.image.load("Buckshot Roullete/background_buckshot_roullete/0.png").convert()
zero_scale = pygame.transform.scale(zero,(width,height))

one = pygame.image.load("Buckshot Roullete/background_buckshot_roullete/1.png").convert()
one_scale = pygame.transform.scale(one,(width,height))

two= pygame.image.load("Buckshot Roullete/background_buckshot_roullete/2.png").convert()
two_scale = pygame.transform.scale(two,(width,height))

three = pygame.image.load("Buckshot Roullete/background_buckshot_roullete/3.png").convert()
three_scale = pygame.transform.scale(three,(width,height))

four = pygame.image.load("Buckshot Roullete/background_buckshot_roullete/4.png").convert()
four_scale = pygame.transform.scale(four,(width,height))

five = pygame.image.load("Buckshot Roullete/background_buckshot_roullete/5.png").convert()
five_scale = pygame.transform.scale(five,(width,height))

six = pygame.image.load("Buckshot Roullete/background_buckshot_roullete/6.png").convert()
six_scale = pygame.transform.scale(six,(width,height))

seven = pygame.image.load("Buckshot Roullete/background_buckshot_roullete/7.png").convert()
seven_scale = pygame.transform.scale(seven,(width,height))

eight = pygame.image.load("Buckshot Roullete/background_buckshot_roullete/8.png").convert()
eight_scale = pygame.transform.scale(eight,(width,height))

nine = pygame.image.load("Buckshot Roullete/background_buckshot_roullete/9.png").convert()
nine_scale = pygame.transform.scale(nine,(width,height))

ten = pygame.image.load("Buckshot Roullete/background_buckshot_roullete/10.png").convert()
ten_scale = pygame.transform.scale(ten,(width,height))

eleven = pygame.image.load("Buckshot Roullete/background_buckshot_roullete/11.png").convert()
eleven_scale = pygame.transform.scale(eleven,(width,height))

twelve = pygame.image.load("Buckshot Roullete/background_buckshot_roullete/12.png").convert()
twelve_scale = pygame.transform.scale(twelve,(width,height))

thirteen = pygame.image.load("Buckshot Roullete/background_buckshot_roullete/13.png").convert()
thirteen_scale = pygame.transform.scale(thirteen,(width,height))

fourteen = pygame.image.load("Buckshot Roullete/background_buckshot_roullete/14.png").convert()
fourteen_scale = pygame.transform.scale(fourteen,(width,height))

fifteen = pygame.image.load("Buckshot Roullete/background_buckshot_roullete/15.png").convert()
fifteen_scale = pygame.transform.scale(fifteen,(width,height))

sixteen = pygame.image.load("Buckshot Roullete/background_buckshot_roullete/16.png").convert()
sixteen_scale = pygame.transform.scale(sixteen,(width,height))

seventeen = pygame.image.load("Buckshot Roullete/background_buckshot_roullete/17.png").convert()
seventeen_scale = pygame.transform.scale(seventeen,(width,height))

eighteen = pygame.image.load("Buckshot Roullete/background_buckshot_roullete/18.png").convert()
eighteen_scale = pygame.transform.scale(eighteen,(width,height))

nineteen = pygame.image.load("Buckshot Roullete/background_buckshot_roullete/19.png").convert()
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
    def __init__(self,image1,image2,x,y,action,):
        self.image1 = image1
        self.image2 = image2
        self.image = self.image1
        self.x = x
        self.y = y
        self.action = action
        self.rect = self.image1.get_rect(center = (self.x,self.y))
        self.hovered= False
        #self.color1 = color1
        #self.color = color2

    def draw_button(self, surface):
        surface.blit(self.image, self.rect)
        if self.hovered== True:

            pygame.draw.circle(surface, grey, (self.rect.left - 10, self.rect.centery ), 5)

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
                
class Button_activate:
    def __init__(self,color1,color2,x,y,width,height):
        self.color1 = color1
        self.color2 = color2
        self.state = False
        self.rect = pygame.Rect(x,y,width,height)

    def draw_button(self,surface):
        if self.state == True:
            self.actual_color = self.color2
        else:
            self.actual_color = self.color1
        
        pygame.draw.rect(surface, self.actual_color, self.rect)

    def handle_event(self,button_activate, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if button_activate:
                    for button in button_activate:
                        button.state = False
                self.state = True
                return True
        return False
    

button_activate = [
    Button_activate(red,grey,150, 255, 30, 30),
    Button_activate(red, grey, 150, 305, 30, 30),  
    Button_activate(red, grey, 150, 355, 30, 30)
]
#---------- functions

def show_play_screen():
    global actual_screen
    actual_screen = "play_screen"

def show_options_screen():
    global actual_screen
    actual_screen = "options_screen"

def show_how2play_screen():
    global actual_screen
    actual_screen = "how2play_screen"

def show_options_easy():
    global actual_screen
    actual_screen == "easy_mode_screen"

def show_options_normal():
    global actual_screen
    actual_screen == "normal_mode_screen"

def show_options_hard():
    global actual_screen
    actual_screen == "hard_mode_screen"

def show_current_difficulty(difficulty):
    global current_difficulty
    current_difficulty = difficulty

#----------- button
buttons_menu = [
    Button(text_play,text_play2,90,250, show_play_screen),
    Button(text_options,text_options2,115,300,show_options_screen),
    Button(text_how2play,text_how2play2,155,350,show_how2play_screen),
    ]

buttons_options = [
    Button(text_easy,text_easy2,60,265, show_current_difficulty("easy")),
    Button(text_normal,text_normal2,60,315, show_current_difficulty("normal")),
    Button(text_hard,text_hard2,60,365, show_current_difficulty("hard")),
    Button(text_easy_d,text_easy_d2,400,265, show_options_easy),
    Button(text_normal_d,text_normal_d2,400,315, show_options_normal),
    Button(text_hard_d,text_hard_d2,400,365, show_options_hard),
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
current_difficulty = "normal"
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
            for button in buttons_menu:
                button.handle_event(event)


        elif actual_screen == "options_screen":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    actual_screen = "menu_screen"
            for button in buttons_options:
                b_selected = False

                button.handle_event(event)

        elif actual_screen == "how2play_screen":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    actual_screen = "menu_screen"
            
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
        for button in buttons_menu:
            button.draw_button(screen)  

    elif actual_screen == "play_screen":   #screen
        screen.fill(black)
        screen.blit(text_play,(0,0))
    elif actual_screen == "options_screen":   #screen
        screen.fill(black)
        screen.blit(text_options_difficulty, (50,200))
        screen.blit(text_volumen, (50,100))
        screen.blit(text_options, (200,20))

        pygame.draw.line(screen, grey, (50,150), (700,150), 2)
        pygame.draw.line(screen, grey, (50,240), (700,240), 2)
        pygame.draw.line(screen, grey, (50,400), (700,400), 2)

        for button in buttons_options:
            button.draw_button(screen)
    
    elif actual_screen == "how2play_screen":   #screen
        screen.fill(black)
        screen.blit(text_general_return,(0,0))
    
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