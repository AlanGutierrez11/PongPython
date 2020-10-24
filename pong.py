import pygame, sys

pygame.init()
clock = pygame.time.Clock()

screen_width = 1080
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_capation("Mi juego de Pong")

ball=pygame.Rect(screen_width/2 - 11, screen_height -11,22,22)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()


	pygame.display.flip()
	clock.tick(60)
