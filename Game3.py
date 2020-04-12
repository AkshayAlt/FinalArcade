import pygame
import os,sys
import time
from random import randint

black = (0,0,0)
white = (255,255,255)

class Ball(pygame.sprite.Sprite):
	def __init__(self,color,width,height):
		super().__init__()
		self.image = pygame.Surface([width,height])
		self.image.fill(black)
		self.image.set_colorkey(black)

		pygame.draw.rect(self.image, color, [0,0,width,height])

		self.velocity = [randint(4,8),randint(-8,8)]

		self.rect = self.image.get_rect()

	def update(self):
		self.rect.x += self.velocity[0]
		self.rect.y += self.velocity[1]

	def bounce(self):
		self.velocity[0] = -self.velocity[0]
		self.velocity[1] = randint(-8,8)

class Paddle(pygame.sprite.Sprite):
	def __init__(self,color,width,height):
		super().__init__()

		self.image = pygame.Surface([width,height])
		self.image.fill(black)
		self.image.set_colorkey(black)

		pygame.draw.rect(self.image,color,[0,0,width,height])

		self.rect = self.image.get_rect()

	def up(self, pixels):
		self.rect.y -= pixels
		if self.rect.y < 0:
			self.rect.y = 0

	def down(self,pixels):
		self.rect.y += pixels
		if self.rect.y > 400:
			self.rect.y = 400

pygame.init()

size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

def pongGameLoop():
	pygame.time.wait(1000)
	gameExit = False

	scorep1 = 0
	scorep2 = 0

	paddle1 = Paddle(white, 10, 100)
	paddle1.rect.x = 20
	paddle1.rect.y = 200

	paddle2 = Paddle(white, 10, 100)
	paddle2.rect.x = 770
	paddle2.rect.y = 200

	ball = Ball(white,10,10)
	ball.rect.x = 345
	ball.rect.y = 195

	all_stuff = pygame.sprite.Group()
	all_stuff.add(paddle1)
	all_stuff.add(paddle2)
	all_stuff.add(ball)

	clock = pygame.time.Clock()

	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					gameExit = True

		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			paddle1.up(5)
		if keys[pygame.K_s]:
			paddle1.down(5)
		if keys[pygame.K_UP]:
			paddle2.up(5)
		if keys[pygame.K_DOWN]:
			paddle2.down(5)

		all_stuff.update()

		if ball.rect.x >= 790:
			scorep1 += 1
			if scorep1 >= 10 and scorep1 > scorep2:
				font = pygame.font.Font(None,75)
				text = font.render("Pl wins!",1,white)
				screen.blit(text,(175,200))
				pygame.display.flip()
				pygame.time.wait(10000)
				scorep1 = 0
				scorep2 = 0
			ball.velocity[0] = - ball.velocity[0]
		if ball.rect.x <= 0:
			scorep2 += 1
			if scorep2 > 10 and scorep1 < scorep2:
				font = pygame.font.Font(None,75)
				text = font.render("P2 wins!",1,white)
				screen.blit(text,(400,200))
				pygame.display.flip()
				pygame.time.wait(10000)
				scorep2 = 0
				scorep1 = 0
			ball.velocity[0] = -ball.velocity[0]
		if ball.rect.y > 590:
			ball.velocity[1] = -ball.velocity[1]
		if ball.rect.y < 0:
			ball.velocity[1] = -ball.velocity[1]

		if pygame.sprite.collide_mask(ball,paddle1) or pygame.sprite.collide_mask(ball,paddle2):
			ball.bounce()

		screen.fill(black)
		pygame.draw.line(screen,white,[400,0],[400,600],5)
		
		all_stuff.draw(screen)

		font = pygame.font.Font(None,75)
		text = font.render(str(scorep1),1,white)
		screen.blit(text,(275,10))
		font = pygame.font.Font(None,75)
		text = font.render(str(scorep2),1,white)
		screen.blit(text,(445,10))

		pygame.display.flip()
		clock.tick(60)

	pygame.quit()
