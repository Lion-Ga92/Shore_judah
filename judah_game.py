import pygame
from pygame import surface
from random import randint
from pygame.constants import KEYDOWN
from pygame.image import load
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    QUIT
)

# Init the sound player 
pygame.mixer.init()

# Init pygame
pygame.init()

#SET SCREEN SIZE
SCREEN_WIDTH = 620
SCREEN_HEIGHT = 900

#CREATE A SCREEN
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# ADD A BG Image as map
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

bg_map = Background("Shore_judah.png", (0, 20))

class LootScreen(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

loot = LootScreen("Loots-1.png", (0, 646))

class Trees(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((35, 93))
        self.surf = pygame.image.load("tree.png").convert()
        self.surf.set_colorkey((250, 211, 107))
        self.rect = self.surf.get_rect(center=(
            randint(50, 600),
            randint(50, 600)
        ))


class Rocks(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((35, 93))
        self.surf = pygame.image.load("Rock1.png").convert()
        self.surf.set_colorkey((250, 211, 107))
        self.rect = self.surf.get_rect(center=(
            randint(50, 600),
            randint(50, 600)
        ))

class Loadbar(pygame.sprite.Sprite):
    def __init__(self, Location1):
        super(Loadbar, self).__init__()
        self.load_images = []
        self.load_images.append(pygame.image.load("loading1.png"))
        self.load_images.append(pygame.image.load("loading1.png"))
        self.load_images.append(pygame.image.load("loading1.png"))
        self.load_images.append(pygame.image.load("loading2.png"))
        self.load_images.append(pygame.image.load("loading2.png"))
        self.load_images.append(pygame.image.load("loading2.png"))
        self.load_images.append(pygame.image.load("loading3.png"))
        self.load_images.append(pygame.image.load("loading3.png"))
        self.load_images.append(pygame.image.load("loading3.png"))
        self.load_images.append(pygame.image.load("loading4.png"))
        self.load_images.append(pygame.image.load("loading4.png"))
        self.load_images.append(pygame.image.load("loading4.png"))
        self.load_images.append(pygame.image.load("loading5.png"))
        self.load_images.append(pygame.image.load("loading5.png"))
        self.load_images.append(pygame.image.load("loading5.png"))
        self.load_images.append(pygame.image.load("loading6.png"))
        self.load_images.append(pygame.image.load("loading6.png"))
        self.load_images.append(pygame.image.load("loading6.png"))
        self.load_images.append(pygame.image.load("loading7.png"))
        self.load_images.append(pygame.image.load("loading7.png"))
        self.load_images.append(pygame.image.load("loading7.png"))

        self.index = 0
        self.image = self.load_images[self.index]

        self.rect = pygame.Rect(Location1)   #I NEED THESE VALUES 130, 680, 200, 600

    def updates(self):
        self.index += 1

        if self.index >= len(self.load_images):
            self.index = 0
        
        self.image = self.load_images[self.index]

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.images = []
        self.images.append(pygame.image.load("Walk(1).png"))
        self.images.append(pygame.image.load("Walk(1).png"))
        self.images.append(pygame.image.load("Walk(1).png"))
        self.images.append(pygame.image.load("Walk(2).png"))
        self.images.append(pygame.image.load("Walk(2).png"))
        self.images.append(pygame.image.load("Walk(2).png"))
        self.images.append(pygame.image.load("Walk(3).png"))
        self.images.append(pygame.image.load("Walk(4).png"))
        self.images.append(pygame.image.load("Walk(5).png"))
        self.images.append(pygame.image.load("Walk(6).png"))
        self.images.append(pygame.image.load("Walk(14).png"))
        self.images.append(pygame.image.load("Walk(15).png"))
        self.images.append(pygame.image.load("Walk(15).png"))
        self.images.append(pygame.image.load("Walk(15).png"))
        self.images.append(pygame.image.load("Walk(15).png"))
        self.images.append(pygame.image.load("Walk(15).png"))
        self.images.append(pygame.image.load("Walk(15).png"))
        self.images.append(pygame.image.load("Walk(15).png"))

        self.index = 0
        self.image = self.images[self.index]

        self.rect = pygame.Rect(50, 50, 30, 30)

    def update(self, pressed_keys):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]

        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen 
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 30:
            self.rect.top = 31
        if self.rect.bottom >= 645:
            self.rect.bottom = 645

        #trying to get the rect to stop around the trees and object
           
player = Player()
tree = Trees()
tree2 = Trees()
tree_3 = Trees()
tree_4 = Trees()
loading_scr = Loadbar((130, 680, 200, 600))
loading_scr1 = Loadbar((160, 760, 200, 600))

rock = Rocks()
rock2 = Rocks()
rock3 = Rocks()
         
rock_group = pygame.sprite.Group(rock, rock2, rock3)

load_group2 = pygame.sprite.Group(loading_scr1)
load_groupi = pygame.sprite.Group(loading_scr)
my_sprite = pygame.sprite.Group(player)
tree_group = pygame.sprite.Group(tree, tree2, tree_3, tree_4)

clock = pygame.time.Clock()

pygame.mixer.music.load("rock_beat.mp3")
pygame.mixer.music.play(loops=-1)

#main game loop
running = True 

while running:
    # look at every in the queue
    for event in pygame.event.get():
        #did user hit a key
        if event.type == KEYDOWN:
            #Was it Escape key
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button
        elif event.type == QUIT:
            running = False

    #get the pressed keys 
    pressed_keys = pygame.key.get_pressed()

    #update the player sprite based on the keys pressed 
    player.update(pressed_keys)

    screen.fill((40, 135, 230))

    # update the loadbar 
    loading_scr.updates()

    # Update the rocks bad:

    loading_scr1.updates()
    
    #Blit it it to the screen 
    screen.blit(bg_map.image, bg_map.rect)

    screen.blit(loot.image, loot.rect)

    my_sprite.draw(screen)

    for enti in rock_group:
        screen.blit(enti.surf, enti.rect)

    for entity in tree_group:
        screen.blit(entity.surf, entity.rect)


    # THESE BLIT ARE FOR THE LOADBARS 
    if pygame.sprite.spritecollideany(player, tree_group):
        for entity in load_groupi:
            screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(player, rock_group):
        for entit in load_group2:
            screen.blit(entit.image, entit.rect)

        
    pygame.display.flip()
    clock.tick(25)

# hehehehehehehehehehehehe