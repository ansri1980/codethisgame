import pygame
from pygame import *

#initalise pygame
pygame.init()

#----------------------------------------------------------------
# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 1100, 600
WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)

# Define tile parameters
WIDTH = 100
HEIGHT = WIDTH
TILE_RES = (WIDTH, HEIGHT)

# Define colors
WHITE = (255,255,255)
RED = (255,0,0)
BROWN = (162,82,45)
#-----------------------------------------------------------------
# Load assets

# Create window
GAME_WINDOW = display.set_mode(WINDOW_RES)

display.set_caption('Attack of the Vampire Pizzas!')

# Setup the background image
background_img = image.load('assets/restaurant.jpg')
background_surf = Surface.convert_alpha(background_img)

BACKGROUND = transform.scale(background_surf, WINDOW_RES)


# Setup the enemy image
# Load the image into the program
pizza_img = image.load('assets/vampire.png')
pizza_surf = Surface.convert_alpha(pizza_img)

VAMPIRE_PIZZA_SCALE_W, VAMPIRE_PIZZA_SCALE_H = 100, 100
VAMPIRE_PIZZ_RES = (VAMPIRE_PIZZA_SCALE_W, VAMPIRE_PIZZA_SCALE_H)
VAMPIRE_PIZZA = transform.scale(pizza_surf, VAMPIRE_PIZZ_RES)

#--------------------------------------------------------------------
# Initialise and draw background grid

tile_color = WHITE

for row in range(6):
	for column in range(11):
		draw.rect(BACKGROUND, tile_color, (WIDTH*column,HEIGHT*row, WIDTH, HEIGHT), 1)

VAMPIRE_PIZZA_BLIT_LOC = (900, 400)

GAME_WINDOW.blit(BACKGROUND, (0,0))
GAME_WINDOW.blit(VAMPIRE_PIZZA, VAMPIRE_PIZZA_BLIT_LOC)

# Add a giant pepperoni
draw.circle(GAME_WINDOW, RED, (925,425), 25, 0)

# Put pizza in the box
draw.rect(GAME_WINDOW, BROWN, (890,395,130,110), 5)
# Give it a lid
draw.rect(GAME_WINDOW, BROWN, (890,295,130,110), 0)
#-----------------------------------------------------------------
# Game Loop

game_running = True

while game_running:
#Check for events
	for event in pygame.event.get():

		if event.type == QUIT:
			game_running = False
	display.update()

#End of main game loop
#-------------------------------------------------------------------
#Clean up game
pygame.quit()