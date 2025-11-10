import pygame
import random

#load_resources()

def run_game(screen):
    ronda = 1
    
    print("Game is running")
    while ronda == 1:
        ronda = ronda_1()
    
    while ronda == 2:
        ronda = ronda_2()
    
    while ronda == 3:
        ronda = ronda_3()

    
def ronda_1(turno = "player", perder_vida = False):
    print("Ronda 1")
    ronda = 1
    
    ronda_1 = {"parte 1": {"vida_player": 2,
                       "vida_enemy": 2,
                       "balas":2,
                       "balas_vivas":1,
                       "bala_fogueo":0},
           
           "parte 2": {"balas":6,
                       "balas_vivas":3,
                       "bala_fogueo":3},
           }
    parte_actual = "parte 1"
    if parte_actual == "parte 1":
        vidas_player = ronda_1["parte 1"]["vida_player"]
        vidas_enemy = ronda_1["parte 1"]["vida_enemy"]
        
        cartucho = [1] * ronda_1["parte 1"]["balas_vivas"] + [0] * ronda_1["parte 1"]["bala_fogueo"]
        random.shuffle(cartucho)
    else:
        cartucho = [1] * ronda_1["parte 2"]["balas_vivas"] + [0] * ronda_1["parte 2"]["bala_fogueo"]
        random.shuffle(cartucho)
    
    if perder_vida == True:
        parte_actual = "parte 2"
    else:
        parte_actual = "parte 1"
    while vidas_player > 0 and vidas_enemy > 0:
        if turno == "player":
            turno, vidas_enemy, vidas_player, cartucho, perder_vida = turno_player(ronda,turno, cartucho, vidas_player, vidas_enemy)
        else:
            turno, vidas_player, vidas_enemy, cartucho, perder_vida = turno_enemy(ronda, turno, cartucho, vidas_player, vidas_enemy)
        
        if vidas_player == 0:
            winner_ronda1 = "enemy"
            ronda = 2
            return ronda
        elif vidas_enemy == 0:
            winner_ronda1 = "player"
            ronda = 2
            return ronda, winner_ronda1
    
def ronda_2():
    pass

def ronda_3():
    pass

def turno_player(ronda,turno, cartucho, vida_player, vida_enemy):
    while ronda == 1:
        accion = input("1. Enemy 2. Yourself: ")
        if accion == "1":
            bala_disparada = cartucho.pop()
            if bala_disparada == 1:
                print("You shot the enemy!")
                vida_enemy -= 1
                turno = "player"
                perder_vida = True
            else:
                print("Click! No bullet fired.")
                vida_enemy -= 0
                turno = "enemy"
                perder_vida = False
    
        elif accion == "2":
            bala_disparada = cartucho.pop()
            if bala_disparada == 1:
                print("You shot yourself!")
                vida_player -= 1
                turno = "enemy"
                perder_vida = True
            else:
                print("Click! No bullet fired.")
                vida_player -= 0
                turno = "player"
                perder_vida = False
        return turno, vida_enemy, vida_player, cartucho, perder_vida
        

def turno_enemy(ronda,turno, cartucho, vida_player, vida_enemy):
    
    while ronda == 1:
        accion = random.choice(["1","2"])
        if accion == "1":
            bala_disparada = cartucho.pop()
            if bala_disparada == 1:
                print("Enemy shot you!")
                vida_player -= 1
                next_turno = "enemy"
                perder_vida = True
            else:
                print("Click! No bullet fired.")
                vida_player -= 0
                next_turno = "player"
                perder_vida = False
    
        elif accion == "2":
            bala_disparada = cartucho.pop()
            if bala_disparada == 1:
                print("Enemy shot themselves!")
                vida_enemy -= 1
                next_turno = "player"
                perder_vida = True
            else:
                print("Click! No bullet fired.")
                vida_enemy -= 0
                next_turno = "enemy"
                perder_vida = False
                
    return next_turno,vida_enemy, vida_player, cartucho, perder_vida

def actualizar_estado():
    pass

def loop():
    pass