import common
import queue as q

def df_search(map):
	found = False
	height = common.constants.MAP_HEIGHT-1
	width = common.constants.MAP_WIDTH-1
	start = (-1,-1)
	for i in range(width):
		for j in range(height):
			if map[j][i] == 2:
				start = (j,i)
	dfs(start[1],start[0],map,[])
	if any(5 in sublist for sublist in map):
		return True
	else:
		return False


def dfs(x, y, map, visited):
	#base case
	if visited.count((x,y))>0:
		return 0

	visited.append((x,y))

	if map[y][x] == 3:
		map[y][x] = 5
		return 1
	elif map[y][x]==1:
		return 0
	else:
		if x+1<common.constants.MAP_WIDTH and dfs(x+1,y,map,visited)==1:
			map[y][x] = 5
			return 1
		elif y+1<common.constants.MAP_HEIGHT and dfs(x,y+1,map,visited)==1:
			map[y][x] = 5
			return 1
		if x-1>=0 and dfs(x-1,y,map,visited)==1:
			map[y][x] = 5
			return 1
		elif y-1>=0 and dfs(x,y-1,map,visited)==1:
			map[y][x] = 5
			return 1
		else:
			map[y][x] = 4

class Node:
	def __init__(self, x, y, prev, depth):
		self.x = x
		self.y = y
		self.prev = prev
		self.depth = depth

	def nodeprint(self):
		print("("+str(self.x)+" ,"+str(self.y)+") depth = "+str(self.depth))


def bf_search(map):
	found = False
	height = common.constants.MAP_HEIGHT - 1
	width = common.constants.MAP_WIDTH - 1
	start = (-1, -1)
	for i in range(width):
		for j in range(height):
			if map[j][i] == 2:
				start = (i, j)

	visited = []
	depth = []
	path = []

	curr_depth = 0
	queue = q.Queue()
	start_n = Node(start[0],start[1],-1,0)
	queue.put(start_n)
	visited.append((start_n.x,start_n.y))
	depth.append(curr_depth)
	while not queue.empty():
		p = queue.get()
		(x, y) = (p.x,p.y)
		if map[y][x]==3:
			while p.prev != -1:
				path.append(p)
				p = p.prev
			found = True
			break

		if x+1 <= width and visited.count((x+1,y))==0 and map[y][x+1]!=1:
			queue.put(Node(x+1,y, p, p.depth+1))
			visited.append((x+1,y))
			depth.append(p.depth+1)

		if y+1 <= height and visited.count((x,y+1))==0 and map[y+1][x]!=1:
			queue.put(Node(x,y+1, p, p.depth+1))
			visited.append((x,y+1))
			depth.append(p.depth+1)

		if x-1 >= 0 and visited.count((x-1,y))==0 and map[y][x-1]!=1:
			queue.put(Node(x-1,y, p, p.depth+1))
			visited.append((x-1,y))
			depth.append(p.depth+1)

		if y-1 >= 0 and visited.count((x,y-1))==0 and map[y-1][x]!=1:
			queue.put(Node(x,y-1, p, p.depth+1))
			visited.append((x,y-1))
			depth.append(p.depth+1)

	for i in range(len(visited)):
		x_c = visited[i][0]
		y_c = visited[i][1]
		if len(path)>0:
			if(map[y_c][x_c]==3 or map[y_c][x_c]==2):
				map[y_c][x_c] = 5
			elif depth[i]<=path[0].depth:
				map[y_c][x_c] = 4
		else:
			map[y_c][x_c] = 4

	for i in path:
		map[i.y][i.x] = 5
	return found

