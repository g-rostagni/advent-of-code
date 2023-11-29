def wrap_face(pos,direc):
	match [int(pos[i]/50) for i in range(2)]:
		case [0,1]:
			# cube 1
			if direc == 2:
				# 4 left
				p = [149 - pos[0]%50, 0]
				d = 0
			elif direc == 3:
				# 6 left
				p = [150 + pos[1]%50, 0]
				d = 0
		case [0,2]:
			# cube 2
			if direc == 0:
				# 5 right
				p = [149 - pos[0]%50, 99]
				d = 2
			elif direc == 1:
				# 3 right
				p = [50 + pos[1]%50, 99]
				d = 2
			elif direc == 3:
				# 6 down
				p = [199, pos[1]%50]
				d = 3
		case [1,1]:
			# cube 3
			if direc == 0:
				# 2 down
				p = [49, 100 + pos[1]%50]
				d = 3
			elif direc == 2:
				# 4 up
				p = [100, pos[0]%50]
				d = 1
		case [2,0]:
			# cube 4
			if direc == 2:
				# 1 left
				p = [49 - pos[0]%50, 50]
				d = 0
			elif direc == 3:
				# 3 left
				p = [50 + pos[1]%50, 50]
				d = 0
		case [2,1]:
			# cube 5
			if direc == 0:
				# 2 right
				p = [49 - pos[0]%50, 149]
				d = 2
			elif direc == 1:
				# 6 right
				p = [150 + pos[1]%50, 49]
				d = 2
		case [3,0]:
			# cube 6
			if direc == 0:
				# 5 down
				p = [149, 50 + pos[0]%50]
				d = 3
			elif direc == 1:
				# 2 up
				p = [0, 100 + pos[1]%50]
				d = 1
			elif direc == 2:
				# 1 up
				p = [0, 50 + pos[0]%50]
				d = 1
		case _:
			raise Exception("Coordinates do not correspond to any cube.")
	return p,d
			
			
#  12
#  3
# 45
# 6
#
# 1 left	->	4 left
# 1 up 		->	6 left

# 2 up 		->	6 down
# 2 right	->	5 right
# 2 down	->	3 right

# 3 left	->	4 up
# 3 right	->	2 down

# 4 left 	->	1 left
# 4 up		->	3 left

# 5 right	->	2 right
# 5 down	->	6 right

# 6 left	->	1 up
# 6 right	->	5 down
# 6 down	->	2 up

with open("22-data","r") as f:
	d = f.read().split("\n\n")
	grid = [[x for x in l] for l in d[0].split("\n")]
	path = d[1].strip().replace("R", " R ").replace("L", " L ").split(" ")
	
lenmax = max([len(l) for l in grid])
for line in grid:
	while len(line) < lenmax:
		line.append(" ")

walls = []
for y in range(len(grid)):
	for x in range(len(grid[y])):
		if grid[y][x] == "#":
			walls.append([y,x])

pos = [0,grid[0].index(".")]
posnew = [0,0]
dirs = [[0,1], [1,0], [0,-1], [-1,0]]
direc = 0

for move in path:
	if move == "R":
		direc = (direc+1) % 4
	elif move == "L":
		direc = (direc-1) % 4
	else:
		for _ in range(int(move)):
			posnew = [pos[i] + dirs[direc][i] for i in range(2)]
			direcnew = direc
			
			if not 0 <= posnew[0] < len(grid) or not 0 <= posnew[1] < lenmax or grid[posnew[0]][posnew[1]] == " ":
				posnew, direcnew = wrap_face(pos,direc)
			
			# if the next move meets a wall
			if posnew in walls:
				break
		
			pos = [posnew[i] for i in range(2)]
			direc = direcnew

pw = 1000 * (pos[0]+1) + 4*(pos[1]+1) + direc
print(pw)
