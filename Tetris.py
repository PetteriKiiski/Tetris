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
import random, pygame, time
from pygame.locals import *
#---Piece Class---
class Piece:
	def __init__(self, no):
		#XY pos's for each piece
		self.no = no
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
	#id == 0, x moves
	#id == 1, y moves
	def move(self, id, speed):pass
		for i in range(4):
			self.loc[i][id] += speed
def RemovePiece(self, piece):
	for co in piece.loc:
		grid[co[1]][co[0]] = None
def GridPiece(self, piece):
	colorDict = {1:'O', 2:'I', 3:'L', 4:'J', 5:'S', 6:'T', 7:'Z'}
	color = colorDict[piece.no]
	for co in piece.loc:
		grid[co[1]][co[0]] = color
def Tetris():
	global grid
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
	pieces = [Piece(random.randint(1, 7))]
	canvas = pygame.display.set_mode((250, 500))
	clock = pygame.time.Clock()
	move = time.time()
	while True:
		clock.tick(50)

		if time.time() - move >= 1:
			pieces[-1].move(1, 1)
Tetris()
