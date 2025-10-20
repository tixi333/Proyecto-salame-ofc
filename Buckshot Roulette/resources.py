import pygame

def load_resources():
    width = 800
    height = 600

    white = (255,255,255)
    black = (0,0,0)
    grey = (128,128,128)
    red = (139,0,0)

    fontr = pygame.font.Font("EBGaramond-VariableFont_wght.ttf", 100) 
    #----------------- FONT
    font0 = pygame.font.Font("monogram-extended.ttf",20)
    font = pygame.font.Font("monogram-extended.ttf", 40) 
    font2 = pygame.font.Font("monogram-extended.ttf", 50)
    #----------------------- menu

    title_game = fontr.render("Buckshot",True,grey)
    title_game2 = fontr.render("Roulette",True,grey)

    #------------------ options screen text 
    text_volumen = font.render("Volumen",True, grey)
    text_options_difficulty = font.render("Modo de dificultad",True,grey)

    options = font.render("Options", True, grey)

    text_easy_d2 = font.render("Easy mode description", True, grey)
    text_normal_d2 = font.render("Normal mode description", True, grey)
    text_hard_d2 = font.render("Hard mode description", True, grey)

    text_easy_d = font.render("Easy mode description", True, red)
    text_normal_d = font.render("Normal mode description", True, red)
    text_hard_d = font.render("Hard mode description", True, red)

    text_volumen = font.render("Volumen",True, grey)
    text_options_difficulty = font.render("Modo de dificultad",True,grey)
    #------------------- current description
    c_easy = font.render("// Current mode: Easy", True, red)
    c_normal = font.render("// Current mode: Normal", True, red)
    c_hard = font.render("// Current mode: Hard", True, red)

    #----------------- difficulty description
    easy = font0.render("descripcion easy", True, grey)
    normal = font0.render("descripcion normal", True, grey)
    hard = font0.render("descripcion hard", True, grey)
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

    text_normal = font.render("Normal", True, red)

    text_hard = font.render("Hard", True, red)

    #------------------ items
   # lupa = pygame.image.load("Buckshot Roulette/items/lupa.png").convert()
    #adrenalina = pygame.image.load("Buckshot Roulette/items/adrenalina.png").convert()
    #burner_phone = pygame.image.load("Buckshot Roulette/items/burner_phone.png").convert()
    #cig = pygame.image.load("Buckshot Roulette/items/cig.png").convert()
   # cosa = pygame.image.load("Buckshot Roulette/items/eso.png").convert()
   # handsaw = pygame.image.load("Buckshot Roulette/items/handsaw.png").convert()

    background = []

    for i in range(20):
        ruta = f"Buckshot Roulette/background_buckshot_roulette/{i}.png"
        imagen = pygame.image.load(ruta)
        scale = pygame.transform.scale(imagen ,(width, height))
        background.append(scale)
        
    return    {
        "background" : background,
        "menu": {"text_play": [text_play, text_play2],
                 "text_options" : [text_options, text_options2],
                 "text_how2play" : [text_how2play, text_how2play2]
                 },
        "options" : { "text_select" : text_select,
                     "difficulty":[text_easy, text_normal, text_hard],
                     "current_mode_easy" : c_easy,
                     "current_mode_normal": c_normal,
                     "current_mode_hard" : c_hard,
                     "description_easy_g": easy,
                     "description_normal_g" : normal,
                     "description_hard_g" : hard,
                     "desc_easy" : [text_easy_d,text_easy_d2],
                     "desc_normal" : [text_normal_d, text_normal_d2],
                     "desc_hard" : [text_hard_d, text_hard_d2]
                     },
        #"items" : {lupa, adrenalina, cig, cosa, handsaw, burner_phone},
        "options_text" : options,
        "volumen" : text_volumen,
        "difficulty": text_options_difficulty,
        "general": [text_general_return, text_enter],
        "title" : [title_game, title_game2],
        "width": width,
        "height": height,
        "colors": [red,grey,white,black]
    }
