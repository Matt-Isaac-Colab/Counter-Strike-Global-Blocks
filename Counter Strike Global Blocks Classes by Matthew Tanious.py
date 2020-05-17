import random, pygame, math, sys
from random import seed
from random import randint
import os.path
from os import path
import winsound


class CSGB:
	white = (255,255,255)
	black = (0,0,0)
	red = ( 255,0,0)
	green = ( 0,255,0)
	blue = (0,0,255)
	brown = (150,75,0)
	gray = (112.95,112.95,112.95)
	yellow = (255,255,0)

	def __init__(self, width, height):
		self.width = width
		self.height = height
		gameDisplay = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption("Counter Strike Global Blocks")

		pygame.init()
		gameDisplay.fill(black)

	def run_game():
		player1 = player((20,20), [(0,0), (self.width, self.height)], pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
		player2 = player((20,20), [(0,0), (self.width, self.height)], pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
		while(1):




class bullet:
	def __init__(self, position, direction, color, ):
		self.position = position


class player:
	def __init__(self, position, boundary, up, down, left, right, shoot):
		self.position
		self.boundary
		self.up = up
		self.down = down
		self.left = left
		self.right = right




game = CSGB(800, 600)
game.run_game()