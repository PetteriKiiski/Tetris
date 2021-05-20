#Scoring system
#num_rows_cleared-num_points_earned
#1-1
#2-10
#3-100
#4-500
#To do list:
#Add Imaginary pieces
#Add real pieces
#Clears row
import random, pygame, time, sys
from pygame.locals import *
pygame.init()
#---Piece Class---
class Piece:
	def __init__(self, no, x):
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
		self.final = False
		self.loc = self.no_co[no][:]
		self.set_x(x)
		self.piece = pygame.image.load(self.no_img[no])
		self.faded = pygame.image.load(self.no_fade[no])
	#id == 0, x moves
	#id == 1, y moves
	#self.loc = [[0, 0], [1, 0], [0, 1], [1, 1]]
	#x = 5
	def set_x(self, x):
#		print (self.loc)
		RemovePiece(self) #No problems
		move_no = self.loc[0][0] - x #move_no = -5
		for i in range(len(self.loc)): #loopdy loop
			if self.loc[i][0] - move_no > 9 or self.loc[i][0] - move_no < 0:
				return
			if move_no > 0:
				keep_track = 0
				for x in range(self.loc[i][0]-move_no, self.loc[i][0]):
					if grid[self.loc[i][1]][x] != None:
						for i in range(len(self.loc)):
							self.loc[i][0] -= keep_track
						return
					keep_track += 1
				keep_track = 0
			else:
				keep_track = 0
				for x in range(self.loc[i][0], self.loc[i][0]-move_no):
					if grid[self.loc[i][1]][x] != None:
						for i in range(len(self.loc)):
							self.loc[i][0] -= keep_track
						return
					keep_track -= 1
				keep_track = 0
			try:
				if grid[self.loc[i][1]][self.loc[i][0] - move_no] != None:
					return
			except:
				pass
			try:
				if grid[self.loc[i][1] + 1][self.loc[i][0]] != None:
					self.final = True
					return
			except:
				pass
		for i in range(len(self.loc)):
			self.loc[i][0] -= move_no
		GridPiece(self)
	def bottom(self, x):
		self.move(1, 20)
		r_val = self.loc[:]
		self.move(1, -20)
		return r_val
	def move(self, id, speed):
		if self.final:
			return False
		for i in range(abs(speed)):
			temp_loc = self.loc[:]
			try:
				for i in range(len(self.loc)):
					temp_loc[i][id] += 1 if speed > 0 else -1
			except Exception as err:
				print (err)
				self.final = True
				return True
			for i in range(len(self.loc)):
				try:
					if grid[temp_loc[i][1] + 1][temp_loc[i][0]] != None:
						self.final = True
						return True
				except:
					pass
				if temp_loc[i][1] == 19:
					self.final = True
					return True
			self.loc = temp_loc[:]
		return True
def RemovePiece(piece):
	print ("Remove:{}".format(piece.loc))
	for co in piece.loc:
		grid[co[1]][co[0]] = None
def GridPiece(piece):
	print ("Grid:{}".format(piece.loc))
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
	m_pos = pygame.mouse.get_pos()
	pieces = [Piece(random.randint(1, 7), m_pos[0] // 25)]
	canvas = pygame.display.set_mode((250, 500))
	pygame.display.set_caption("Tetris")
	move = time.time()
	GridPiece(pieces[-1])
	while True:
		canvas.fill((255, 255, 255))
		m_pos = pygame.mouse.get_pos()
		pieces[-1].set_x(m_pos[0] // 25)
#		RemovePiece(pieces[-1])
		if pieces[-1].set_x(m_pos[0] // 25):
			GridPiece(pieces[-1])
			pieces += [Piece(random.randint(1, 7), m_pos[0] // 25)]
		RemovePiece(pieces[-1])
		if time.time() - move >= 0.5:
			move = time.time()
			if not pieces[-1].move(1, 1):
				GridPiece(pieces[-1])
				pieces += [Piece(random.randint(1, 7), m_pos[0] // 25)]
		GridPiece(pieces[-1])
#		for piece in pieces:
#			for co in piece.bottom(piece.loc[0][0]):
#				canvas.blit(piece.faded, (co[0] * 25, co[1] * 25))
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
			if event.type == MOUSEBUTTONDOWN:
				RemovePiece(pieces[-1])
				pieces[-1].move(1, 20)
				GridPiece(pieces[-1])
				pieces += [Piece(random.randint(1, 7), m_pos[0] // 25)]
#		for i, row in enumerate(grid):
#			if None not in row:
#				old_row = grid[i][:]
#				grid[i] = [None, None, None, None, None, None, None, None, None, None]
#				for x, piece in enumerate(old_row[:]):
#					if piece.loc[1] == i:
#						del old_row[i].loc[x]
		pygame.display.update()
Tetris()
