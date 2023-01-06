
import pygame 
from pygame.locals import *






# Initialise screen
pygame.init()
home_screen_size = width,height =1300,1000
screen = pygame.display.set_mode((home_screen_size) , RESIZABLE)
pygame.display.set_caption('zobizob')


#variable pour passer page 2
ENTER_GAME = False

homepage_background = pygame.image.load("images\homepage.png")
homepage_background = pygame.transform.scale(homepage_background,home_screen_size)

pygame.font.init()
texte_color = (255,255,255)
font = pygame.font.Font('font\Pixeled.ttf',50)
hometexte = font.render("Zobizob",1, texte_color)
textpos = hometexte.get_rect()
textpos = x, y = home_screen_size[0] /3, home_screen_size[1] * 0.65

homepage_background.blit(hometexte, (textpos))


#class qui cree les btn
class btn():
    def __init__(self, x,y, image):
        
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x , y)
        self.IsClicked = False
        
    def draw(self):
        action = False
        
        #mouse position
        mouse_pos = pygame.mouse.get_pos()
        
        #chek click 
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.IsClicked == False:
                self.IsClicked = True
                action = True
               
                
        if pygame.mouse.get_pressed()[0] == 0:
		       self.IsClicked = False
        
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
        return action

#enter button        
homebtnfct = btn(home_screen_size[0] /3, home_screen_size[1] * 0.65, hometexte)
        


# Blit everything to the screen
screen.blit(homepage_background, (0, 0))
pygame.display.flip()

# Event loop
continuer = 1
while continuer:
    
    if homebtnfct.draw() == True :
        print("lunch game")
        import register
        
        
        
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
              print("entergame")
              ENTER_GAME = True  
        if event.type == QUIT:
            continuer = 0
    screen.blit(homepage_background, (0, 0))
    pygame.display.flip()


