import pygame
import random

# Import pygame.locals for easier access to key coordinates

# Updated to conform to flake8 and black standards

from pygame.locals import (

    K_UP,

    K_DOWN,

    K_LEFT,

    K_RIGHT,

    K_ESCAPE,

    KEYDOWN,

    QUIT,

)


# Define constants for the screen width and height

SCREEN_WIDTH = 800

SCREEN_HEIGHT = 600


class Enemy(pygame.sprite.Sprite):

    def __init__(self):

        super(Enemy, self).__init__()

        self.surf = pygame.Surface((20, 10))

        self.surf.fill((255, 255, 255))

        self.rect = self.surf.get_rect(

            center=(

                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),

                random.randint(0, SCREEN_HEIGHT),

            )

        )

        self.speed = random.randint(5, 20)


    # Move the sprite based on speed

    # Remove the sprite when it passes the left edge of the screen

    def update(self):

        self.rect.move_ip(-self.speed, 0)

        if self.rect.right < 0:

            self.kill()


# Define a player object by extending pygame.sprite.Sprite

# The surface drawn on the screen is now an attribute of 'player'

class Player(pygame.sprite.Sprite):

    def __init__(self):

        super(Player, self).__init__()

        self.surf = pygame.Surface((75, 25))

        self.surf.fill((255, 255, 255))

        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
            
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
    
            if self.rect.top <= 0:
    
                self.rect.top = 0
    
            if self.rect.bottom >= SCREEN_HEIGHT:
    
                self.rect.bottom = SCREEN_HEIGHT


# Initialize pygame

pygame.init()

pressed_keys = pygame.key.get_pressed()
# Create the screen object

# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Instantiate player. Right now, this is just a rectangle.
# Create a custom event for adding a new enemy

ADDENEMY = pygame.USEREVENT + 1

pygame.time.set_timer(ADDENEMY, 250)
player = Player()

# Create groups to hold enemy sprites and all sprites

# - enemies is used for collision detection and position updates

# - all_sprites is used for rendering

enemies = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()

all_sprites.add(player)
running = True


while running:

    # for loop through the event queue

    for event in pygame.event.get():

        # Check for KEYDOWN event

        if event.type == KEYDOWN:

            # If the Esc key is pressed, then exit the main loop

            if event.key == K_ESCAPE:

                running = False

        # Check for QUIT event. If QUIT, then set running to false.

        elif event.type == QUIT:

            running = False
        
        elif event.type == ADDENEMY:

            # Create the new enemy and add it to sprite groups

            new_enemy = Enemy()

            enemies.add(new_enemy)

            all_sprites.add(new_enemy)


    # Fill the screen with black

    
    screen.fill((0, 0, 0))
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Draw the player on the screen
    

    

    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys)
    enemies.update()
   
    screen.blit(player.surf, player.rect)

    # Update the display

    pygame.display.flip()