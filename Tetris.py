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
import random, pygame, time, sys
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
			5:[[0, 1], [1, 1], [1, 0], [2, 0]], \
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
	def move(self, id, speed):
#		print (self.loc)
		temp_loc = self.loc
		try:
			for i in range(4):
				temp_loc[i][id] += speed
#				if grid[temp_loc[i][1]][temp_loc[i][0]] != None or temp_loc[i][1] == 19:
#					print (self.loc)
#					print ("False")
#					return False
		except Exception as err:
			print (err)
			return False
#		temp_loc2 = temp_loc[:]
#		try:
#			for i in range(4):
#				temp_loc2[i][id] += speed
#		except Exception as err:
#			print (err)
		for i in range(4):
			try:
				if grid[temp_loc[i][1] + 1][temp_loc[i][0]] != None:
					print (self.loc)
					print (not grid[temp_loc[i][1]][temp_loc[i][0]] != None)
					return False
			except:
				pass
			if temp_loc[i][1] == 19:
				print (self.loc)
				print (not grid[temp_loc[i][1]][temp_loc[i][0]] != None)
				return False
		print ("Happens")
		self.loc = temp_loc[:]
		return True
def RemovePiece(piece):
	for co in piece.loc:
		grid[co[1]][co[0]] = None
def GridPiece(piece):
	for co in piece.loc:
		grid[co[1]][co[0]] = piece
def Tetris():
	global grid
	blank = pygame.image.load("Blank.png")
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
	pygame.display.set_caption("Tetris")
	move = time.time()
	GridPiece(pieces[-1])
	while True:
		canvas.fill((255, 255, 255))
		RemovePiece(pieces[-1])
		if time.time() - move >= 1:
			move = time.time()
			if not pieces[-1].move(1, 1):
				print (pieces[-1].loc)
				GridPiece(pieces[-1])
				pieces += [Piece(random.randint(1, 7))]
		GridPiece(pieces[-1])
		y = -1
		x = -1
		for l in grid:
			y += 1
			for val in l:
				x += 1
				if val == None:
					canvas.blit(blank, (x*25, y*25))
				else:
					canvas.blit(val.piece, (x*25, y*25))
			x = -1
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		pygame.display.update()
Tetris()
