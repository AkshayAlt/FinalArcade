import os, sys
import pygame
import random
import time

pygame.init()

green = [0,255,0]
black = [100,0,0]
white = [255,255,255]
red = [255,0,0]
blue = [0,0,255]
window_width = 800
window_height = 600

gameDisplay = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Snake")

def gquit():
	pygame.quit()
	sys.exit(0)

clock = pygame.time.Clock()
FPS = 5
blockSize = 20
noPixel = 0

font = pygame.font.SysFont(None, 25, bold=True)

def drawGrid():
	sizeGrd = window_width // blockSize

def snake(blockSize, snakeList):
	for size in snakeList:
		pygame.draw.rect(gameDisplay,black,[size[0]+5,size[1],blockSize,blockSize],2)

def msg_display(msg,color):
	screen_text = font.render(msg,True,color)
	gameDisplay.blit(screen_text,[window_width//2,window_height//2])

def score_display(score):
	scorems = "Score: "+str(score)
	score_text = font.render(scorems,True,red)
	gameDisplay.blit(score_text,[15,window_height-15])

def snakeGameLoop():
	gameExit = False
	gameOver = False

	leadX = window_width/2
	leadY = window_height/2

	pixelchangeX = 0
	pixelchangeY = 0

	snakelist = []
	snakelength = 1
	score = 0

	randappleX = round(random.randrange(0, window_width-blockSize)/10.0)*10.0
	randappleY = round(random.randrange(0, window_height-blockSize)/10.0)*10.0

	while(not gameExit):
		while(gameOver == True):
			gameDisplay.fill(white)
			msg_display("Hit space to play and esc to quit",red)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameOver = False
					gameExit = True

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						snakeGameLoop()
					if event.key == pygame.K_ESCAPE:
						gameExit = True
						gameOver = False

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True

			if event.type == pygame.KEYDOWN:
				left = event.key == pygame.K_a
				right = event.key == pygame.K_d
				up = event.key == pygame.K_w
				down = event.key == pygame.K_s

				if left:
					pixelchangeX = -blockSize
					pixelchangeY = noPixel
				elif right:
					pixelchangeX = blockSize
					pixelchangeY = noPixel
				elif up:
					pixelchangeY = -blockSize
					pixelchangeX = noPixel
				elif down:
					pixelchangeY = blockSize
					pixelchangeX = noPixel

			if leadX >= window_width or leadX < 0 or leadY >= window_height or leadY < 0:
				gameOver = True

		leadX += pixelchangeX
		leadY += pixelchangeY

		gameDisplay.fill(white)


		AppleThickness = 20

		print([int(randappleX),int(randappleY),AppleThickness,AppleThickness])
		pygame.draw.rect(gameDisplay,red,[randappleX,randappleY,AppleThickness,AppleThickness])

		asp = []
		asp.append(leadX)
		asp.append(leadY)
		snakelist.append(asp)

		if len(snakelist) > snakelength:
			del snakelist[0]

		for seg in snakelist[:-1]:
			if seg == asp:
				gameOver = True

		snake(blockSize,snakelist)
		score_display(score)

		pygame.display.update()

		if leadX >= randappleX and leadX <= randappleX+AppleThickness:
			if leadY >= randappleY and leadY <= randappleY+AppleThickness:
				randappleX = round(random.randrange(0,window_width-blockSize)/10.0)*10.0
				randappleY = round(random.randrange(0,window_height-blockSize)/10.0)*10.0
				snakelength += 1
				score += 1

		clock.tick(FPS)
	pygame.quit()
	gquit()
