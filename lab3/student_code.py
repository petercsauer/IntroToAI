import common
def astar_search(map):
	found = False
	found = aStar(map)
	return found

class Node:
	def __init__(self, parentNode, x, y, endX, endY):
		self.parent = parentNode
		self.x = x
		self.y = y
		self.endX = endX
		self.endY = endY
		if self.parent == -1:
			self.g = 0
		else:
			self.g = self.parent.g + 1
		distX = abs(endX-x)
		distY = abs(endY-y)
		self.h = distX + distY
		self.f = self.g+self.h

	def checkEnd(self):
		if self.x == self.endX and self.y == self.endY:
			return True
		else:
			return False

	def printNode(self):
		print("("+str(self.x)+", "+str(self.y)+") | " + str(self.checkEnd()))

def findGoals(start, map):
	if start:
		for i in range(len(map)):
			for j in range(len(map[i])):
				if map[i][j] == 2:
					return (i,j)
		return (-1,-1)
	if not start:
		for i in range(len(map)):
			for j in range(len(map[i])):
				if map[i][j] == 3:
					return (i,j)
		return (-1,-1)

def aStar(map):
	found = False
	start = findGoals(True, map)
	end = findGoals(False, map)
	openNodes = []
	closedNodes = []
	startNode = Node(-1, start[1], start[0], end[1], end[0])
	openNodes.append(startNode)
	w = common.constants.MAP_WIDTH
	h = common.constants.MAP_HEIGHT
	while len(openNodes)>0 and found == False:
		minF = 10000
		minFNode = -1
		for i in openNodes:
			if i.f < minF:
				minF = i.f
				minFNode = i
		openNodes.remove(minFNode)
		closedNodes.append(minFNode)
		found = minFNode.checkEnd()
		x = minFNode.x
		y = minFNode.y
		if x-1>=0 and map[y][x-1] != 1 and checkforPos(closedNodes,x-1,y)<0:
			newNode = Node(minFNode, x-1, y, minFNode.endX, minFNode.endY)
			if checkForNode(openNodes,newNode)<0:
				openNodes.append(newNode)
			elif openNodes[checkForNode(openNodes,newNode)].g > newNode.g:
				openNodes.pop(checkForNode(openNodes,newNode))
				openNodes.append(newNode)
		if x+1<w and map[y][x+1] != 1  and checkforPos(closedNodes,x+1,y)<0:
			newNode = Node(minFNode, x+1, y, minFNode.endX, minFNode.endY)
			if checkForNode(openNodes,newNode)<0:
				openNodes.append(newNode)
			elif openNodes[checkForNode(openNodes,newNode)].g > newNode.g:
				openNodes.pop(checkForNode(openNodes,newNode))
				openNodes.append(newNode)
		if y-1>=0 and map[y-1][x] != 1  and checkforPos(closedNodes,x,y-1)<0:
			newNode = Node(minFNode, x, y-1, minFNode.endX, minFNode.endY)
			if checkForNode(openNodes,newNode)<0:
				openNodes.append(newNode)
			elif openNodes[checkForNode(openNodes,newNode)].g > newNode.g:
				openNodes.pop(checkForNode(openNodes,newNode))
				openNodes.append(newNode)
		if y+1<h and map[y+1][x] != 1  and checkforPos(closedNodes,x,y+1)<0:
			newNode = Node(minFNode, x, y+1, minFNode.endX, minFNode.endY)
			if checkForNode(openNodes,newNode)<0:
				openNodes.append(newNode)

	setExploredCells(map,closedNodes)
	if found:
		setFoundPath(map,minFNode)
	return found



def checkForNode(list, node):
	exists = -1
	for i in range(len(list)):
		if list[i].x == node.x and list[i].y == node.y:
			exists = i
	return exists

def checkforPos(list,x,y):
	exists = -1
	for i in range(len(list)):
		if list[i].x == x and list[i].y == y:
			exists = i
	return exists

def setExploredCells(map, list):
	for i in list:
		map[i.y][i.x] = 4

def setFoundPath(map,node):
	while node != -1:
		map[node.y][node.x] = 5
		node = node.parent





