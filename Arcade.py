import pygame
import sys
from Game1 import snakeGameLoop
from Game2 import breakoutGameLoop
from Game3 import pongGameLoop

pygame.init()

green = [0,255,0]
black = [0,0,0]
white = [255,255,255]
red = [255,0,0]
blue = [0,0,255]
window_width = 800
window_height = 600

fps = 60
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Akshay's Arcade")


exit = False

while not exit:
	gameDisplay.fill(red)

	font = pygame.font.Font(None,70)
	text = font.render("Welcome to Akshay's Arcade!",1,white)
	gameDisplay.blit(text,(55,200))
	pygame.display.flip()

	font = pygame.font.Font(None, 30)
	text = font.render("(Press corresponding number on the keyboard)",1,green)
	gameDisplay.blit(text,(250,440))
	pygame.display.flip()

	font = pygame.font.Font(None, 50)
	text = font.render("Select one option:",1,green)
	gameDisplay.blit(text,(70,280))
	pygame.display.flip()

	font = pygame.font.Font(None, 30)
	text = font.render("1. Snake",1,green)
	gameDisplay.blit(text,(70,320))
	pygame.display.flip()

	font = pygame.font.Font(None, 30)
	text = font.render("2. Breakout",1,green)
	gameDisplay.blit(text,(70,360))
	pygame.display.flip()

	font = pygame.font.Font(None, 30)
	text = font.render("3. Pong",1,green)
	gameDisplay.blit(text,(70,400))
	pygame.display.flip()

	font = pygame.font.Font(None, 30)
	text = font.render("4. Exit",1,green)
	gameDisplay.blit(text,(70,440))
	pygame.display.flip()


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_1:
				snakeGameLoop()
			elif event.key == pygame.K_2:
				breakoutGameLoop()
			elif event.key == pygame.K_3:
				pongGameLoop()
			elif event.key == pygame.K_4:
				exit = True

	clock.tick(1)

pygame.quit()