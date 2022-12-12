# a function that returns all squares we are allowed to reach from a given square
def adjacent(y,x):
	adj = []
	for coord in [[y-1,x], [y+1,x], [y,x-1], [y,x+1]]:				# loop over all direct neighbours
		if 0 <= coord[0] < len(grid) and 0 <= coord[1] < len(grid[0]):		# if the coordinates are valid
			if ord(grid[coord[0]][coord[1]]) >= ord(grid[y][x]) - 1:	# and if the neighbour is not more than 1 step lower than the square (remember we are going in reverse)
				adj.append(coord)					# add to the list of valid neighbours
	return adj

with open("12-data","r") as f:
	grid = [[square for square in line.strip()] for line in f.readlines()]

# start by defining the grid that contains the number of steps to get to a given cell	
steps = [[10000 for p in line] for line in grid]

# find the starting (E) and finishing (S) points for the algorithm
foundE = False
foundS = False
for y in range(len(grid)):
	for x in range(len(grid[0])):
		if grid[y][x] == "E":		# when we find the starting point:
			queue = [[y,x]]		# tell the algorithm to start by looking from there
			steps[y][x] = 0		# 0 steps required to get to the origin
			grid[y][x] = "z"	# replace the E with the height (z) for the algorithm to work when it reaches it
			foundE = True
		if grid[y][x] == "S":		# when we find the finishing point:
			start = [y,x]		# write down its coordinates for later
			grid[y][x] = "a"	# replace the S with the height (a) for the algorithm to work when it reaches it
			foundS = True
		if foundE and foundS:
			break
	if foundE and foundS:
		break
	
# Djikstra's algorithm, but in reverse: starting from the finishing point and finding the shortest path to the starting point
while queue:								# if there are no more squares to look at, we have found the shortest path to the goal
	queuenext = []
	for square in queue:						# loop over all squares we need to look at
		for p in adjacent(square[0],square[1]):			# find all squares we are allowed to go to from here
			newcost = steps[square[0]][square[1]] + 1	# it takes one more step to get to the next square
			if newcost < steps[p[0]][p[1]]:			# if the number of steps taken to reach the next square is lower than we previously found:
				steps[p[0]][p[1]] = newcost		# update the number of steps needed with the new value
				queuenext.append(p)			# look at the next square as a starting point for next time
	queuenext.sort(key=lambda steps:steps)				# sort the list of squares to look at next to make sure we look at the cheaper ones first
	queue = [q for q in queuenext]					# update the queue with the squares to look at for the next cycle

# find the shortest path from the end E to any square with height a
costmin = 10000
for y in range(len(grid)):
	for x in range(len(grid[0])):	
		if grid[y][x] == "a" and steps[y][x] < costmin:
			costmin = steps[y][x]

print(steps[start[0]][start[1]])
print(costmin)
