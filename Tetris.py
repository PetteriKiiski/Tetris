#Scoring system
#num_rows_cleared-num_points_earned
#1-1
#2-10
#3-100
#4-500
#To do list:
#Create Grid
#Add Imaginary pieces
#Piece falls in place because of out of time
#Add real pieces
#Clears row
import random, pygame
from pygame.locals import *
#---Piece Class---
class Piece:
	def __init__(self, no):
		#XY pos's for each piece
		self.no_co = {1:[[0, 0], [1, 0], [0, 1], [1, 1]], \
			2:[[0, 0], [1, 0], [2, 0], [3, 0]], \
			3:[[0, 0], [0, 1], [1, 1], [2, 1]], \
			4:[[0, 1], [1, 1], [2, 1], [2, 0]], \
			5:[[0, 1], [1, 1], [0, 1], [0, 2]], \
			6:[[0, 1], [1, 1], [1, 0], [2, 1]], \
			7:[[0, 0], [1, 0], [1, 1], [2, 1]]}
		self.no_img = {1:"Yellow.png", 2:"Turqoise.png", 3:"Blue.png", 4:"Orange.png", 5:"Green.png", 6:"Purple.png", 7:"Red.png"}
		self.no_fade = {1:"FadedYellow.png", 2:"FadedTurqoise.png", 3:"FadedBlue.png", 4:"FadedOrange.png", 5:"FadedGreen.png", 6:"FadedPurple.png", 7:"FadedRed.png"}
		self.orig_loc = self.no_co[no]
		self.loc = self.no_co[no][:]
		self.piece = pygame.image.load(self.no_img[no])
		self.faded = pygame.image.load(self.no_fade[no])
	def move(self, id, speed):pass
def Tetris():
	grid = [ \
	[None, None, None, None, None, None, None, None, None, None], \
	[None, None, None, None, None, None, None, None, None, None], \
	[None, None, None, None, None, None, None, None, None, None], \
	[None, None, None, None, None, None, None, None, None, None], \
	[None, None, None, None, None, None, None, None, None, None], \
	[None, None, None, None, None, None, None, None, None, None], \
	[None, None, None, None, None, None, None, None, None, None], \
	[None, None, None, None, None, None, None, None, None, None], \
	[None, None, None, None, None, None, None, None, None, None], \
	[None, None, None, None, None, None, None, None, None, None], \
	[None, None, None, None, None, None, None, None, None, None], \
	[None, None, None, None, None, None, None, None, None, None], \
	[None, None, None, None, None, None, None, None, None, None], \
	[None, None, None, None, None, None, None, None, None, None], \
	[None, None, None, None, None, None, None, None, None, None], \
	[None, None, None, None, None, None, None, None, None, None], \
	[None, None, None, None, None, None, None, None, None, None], \
	[None, None, None, None, None, None, None, None, None, None], \
	[None, None, None, None, None, None, None, None, None, None], \
	[None, None, None, None, None, None, None, None, None, None]]
Tetris()
