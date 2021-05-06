import common

def minmax_tictactoe(board, turn):
	# common.print_board(board)
	currentStatus = common.constants.NONE
	if turn == common.constants.X:
		currentStatus = maxA(board)

	if turn == common.constants.O:
		currentStatus = minA(board)

	if currentStatus == 1:
		return common.constants.X
	elif currentStatus == -1:
		return common.constants.O

	return common.constants.NONE

def abprun_tictactoe(board, turn):
	a = -1000
	b = 1000
	currentStatus = common.constants.NONE
	if turn == common.constants.X:
		currentStatus = maxAB(board,a,b)

	if turn == common.constants.O:
		currentStatus = minAB(board,a,b)

	if currentStatus == 1:
		return common.constants.X
	elif currentStatus == -1:
		return common.constants.O

	return common.constants.NONE

def continueGame(board):
	for i in board:
		if i == 0:
			return True
	return False


def maxA(board):
	currentState = common.game_status(board)

	# X WINS
	if currentState == 1:
		return 1

	# O WINS
	if currentState == 2:
		return -1

	# TIE
	if not continueGame(board):
		return 0

	best = -1000
	for j in range(3):
		for i in range(3):
			if common.get_cell(board, j, i) == 0:
				common.set_cell(board, j, i, 1)
				best = max(best, minA(board))
				common.set_cell(board, j, i, 0)

	return best

def minA(board):
	currentState = common.game_status(board)

	# X WINS
	if currentState == 1:
		return 1

	# O WINS
	if currentState == 2:
		return -1

	# TIE
	if not continueGame(board):
		return 0

	best = 1000
	for j in range(3):
		for i in range(3):
			if common.get_cell(board, j, i) == 0:
				common.set_cell(board, j, i, 2)
				best = min(best, maxA(board))
				common.set_cell(board, j, i, 0)

	return best

def maxAB(board, a, b):
	currentState = common.game_status(board)

	# X WINS
	if currentState == 1:
		return 1

	# O WINS
	if currentState == 2:
		return -1

	# TIE
	if not continueGame(board):
		return 0

	best = -1000
	for j in range(3):
		for i in range(3):
			if common.get_cell(board, j, i) == 0:
				common.set_cell(board, j, i, 1)
				best = max(best, minAB(board, a, b))
				common.set_cell(board, j, i, 0)
				if best >= b:
					return best
				a = max(a, best)

	return best

def minAB(board, a, b):
	currentState = common.game_status(board)

	# X WINS
	if currentState == 1:
		return 1

	# O WINS
	if currentState == 2:
		return -1

	# TIE
	if not continueGame(board):
		return 0

	best = 1000
	for j in range(3):
		for i in range(3):
			if common.get_cell(board, j, i) == 0:
				common.set_cell(board, j, i, 2)
				best = min(best, maxAB(board,a,b))
				common.set_cell(board, j, i, 0)
				if best <= a:
					return best
				b = min(b, best)
	return best













