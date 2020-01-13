# Tic Tac Toe
# Author: Kaizanna
import random

 # Print the board for the user
def drawBoard(board):
 print('   |   | ')
 print(' {0} | {1} | {2}'.format(board[0], board[1], board[2]))
 print('   |   | ')
 print('----------')
 print('   |   | ')
 print(' {0} | {1} | {2}'.format(board[3], board[4], board[5]))
 print('   |   | ')
 print('----------')
 print('   |   | ')
 print(' {0} | {1} | {2}'.format(board[6], board[7], board[8]))
 print('   |   | ')	

# drawBoard(['0', '1', '2', '3', '4', '5', '6', '7', '8'])

# Sets a letter in the board
def makeMove(board, move, letter):
	board[move] = letter

# Returns boolean on whether a space is empty or not
def isSpaceFree(board, move):
	return board[move] == ' '

# Get whether the player wants to play X or O
def inputPlayerLetter():
	letter = ''
	print('Do you want to be X or O?')
	while not (letter == 'X' or letter == 'O'):
		letter = input().upper()

	# Player is always the first element of this list
	if letter == 'X':
		return ['X', 'O']
	else:
		return ['O', 'X']	

# Ask a player for a move
def getPlayerMove(board):
	move = ' '
	print('What is your next move? (1-9)')
	while move not in '1 2 3 4 5 6 7 8 9'.split(' ') or not isSpaceFree(board, int(move) - 1):
		move = input()
	return int(move) - 1	

# Determine who goes first
def whoGoesFirst():
	if random.randint(0, 1) == 0:
		return 'computer'
	else:
		return 'player'

# Ask the player if they want to play again
# Returns boolean
def playAgain():
	print('Do you want to play again? (y/n)')
	return input().lower().startswith ('y')

# Given a board and a letter determine if the letter has a winning state
# b stands for Board, l stands for letter
# Returns a boolean
def isWinner(b, l):
	return (
			(b[0] == l and b[1] == l and b[2] == l) or # top
			(b[3] == l and b[4] == l and b[5] == l) or # middle
			(b[6] == l and b[7] == l and b[8] == l) or # bottom
			(b[0] == l and b[3] == l and b[6] == l) or # left
			(b[1] == l and b[4] == l and b[7] == l) or # center
			(b[2] == l and b[5] == l and b[8] == l) or # right
			(b[0] == l and b[4] == l and b[8] == l) or # top left to bottom right
			(b[2] == l and b[4] == l and b[6] == l))  # bottom left to top right

# Checks if the board is full, checks for tie
# Returns a boolean
def isBoardFull(board):
	for i in range(0, 9):
		if isSpaceFree(board, i):
			return False
	return True
	
# Next time
# We're going to program a basic AI (canonical) and a perfect AI (canonical)
# Make the basic AI
# Make the game loop
# Make the advanced AI
# Modify the game loop to use it
		
#Duplicate the board, to avoid a reference error
def  getBoardCopy(board):
	bus = []
	for i in board:
		bus.append(i)
	return bus

# Most basic canonical AI
def getRandomMove(board):
	if isBoardFull(board):
		return None
	while True:
		move = random.randint(0, 8)
		if isSpaceFree(board, move):
			return move

def chooseRandomMoveFromList(board, movesList):
	possibleMoves = []
	for i in movesList:
		if isSpaceFree(board, i):
			possibleMoves.append(i)
	if 	len(possibleMoves) > 0:	
		return random.choice(possibleMoves)

def getComputerMove(board, computerLetter):
	# Get the player letter
	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'
	# If there is a winning move, do it
	for i in range(0,9):
		copy = getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, i, computerLetter)
			if isWinner(copy, computerLetter):
				return i

	# If they are going to win, block
	for i in range(0,9):
		copy = getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, i, playerLetter)
			if isWinner(copy, playerLetter):
				return i			

	# Grab a corner
	move = chooseRandomMoveFromList(board, [0, 2, 6, 8])
	if move != None:
		return move

	# Grab the center
	if isSpaceFree(board, 4):
		return 4

	# Grab a side
	return chooseRandomMoveFromList(board, [1, 3, 5, 7])

# Main Code
print('Welcome to Tic Tac Toe!')
while True:
	theBoard = [' '] * 9
	playerLetter, computerLetter = inputPlayerLetter()
	turn = whoGoesFirst()
	print('The ' + turn + ' will go first.')
	gameIsPlaying = True

	while gameIsPlaying:
		if turn == 'player':
			# Players turn
			drawBoard(theBoard) # See the board
			move = getPlayerMove(theBoard) # Pick a spot
			makeMove(theBoard, move, playerLetter) # Write it down

			if isWinner(theBoard, playerLetter):
				drawBoard(theBoard)
				print('Hurray! You won!')
				gameIsPlaying = False
			else:
				turn = 'computer'
		else:
			# Computer turn
			move = getComputerMove(theBoard, computerLetter)
			if move != None:
				makeMove(theBoard, move, computerLetter)

			if isWinner(theBoard, computerLetter):
				drawBoard(theBoard)
				print('The computer won, you suck dick.')
				gameIsPlaying = False
			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print('Tie!')
					break
				else:
					turn = 'player'		

	if not playAgain():
		break