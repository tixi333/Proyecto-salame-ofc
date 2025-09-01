import pygame 

pygame.init()
pygame.font.init()
pygame.display.set_caption("Cuida a tu salame")
height= 600
width = 800 
screen = pygame.display.set_mode((width, height))

play1 = pygame.image.load("play1.png")
play1_scale = pygame.transform.scale(play1, (100, 100))

play2 = pygame.image.load("play1.png")
play2_scale = pygame.transform.scale(play1, (100, 100))

class Button:
    def __init__(self,x,y,width,height,image1,image2,text,state):
        self.image1 = image1
        self.image2 = image2
        self.x = x
        self.y = y
        self.text = text   
        self.state = state
        self.rect = self.image1.get_rect(center=(width//2,350))
        self.width = width
        self.height = height

    def event(self,event,state):
        pass

    def draw(self,surface):

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.state = True
        if self.state == False:
            surface.blit(self.image1,self.rect)
            for i in range(1):
                print(self.state)
        else:
            surface.blit(self.image2,self.rect)
            for i in range(1):
                print(self.state)

button_play= Button(width//2,height//2,100,100,play1_scale,play2_scale,"Play",True)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and button_play.rect.collidepoint(event.pos):
                button_play.state = not button_play.state
                print(button_play.state)
        button_play.draw(screen)
        pygame.display.flip()


pygame.quit()
