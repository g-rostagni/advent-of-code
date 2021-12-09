def printgrid(grid):
	print('')
	for flatgrid in grid:
		print('/////////////////////////////////////////////////')
		for line in flatgrid:
			for char in line:
				print(char,end='')
			print('')
		
def neighbours(w,z,y,x):
	nb = []
	for l in range(w-1,w+2):
		for k in range(z-1,z+2):
			for j in range(y-1,y+2):
				for i in range(x-1,x+2):
					if [l,k,j,i] != [w,z,y,x]:
						nb.append([l,k,j,i])
	return nb
		
def update(gridF,w,z,y,x):
	act = 0
	for l,k,j,i in neighbours(w,z,y,x):
		if gridF[l][k][j][i] == '#':
			act += 1
	if gridF[w][z][y][x] == '#':
		if act == 2 or act == 3:
			return '#'
		else:
			return '.'
	else:
		if act == 3:
			return '#'
		else:
			return '.'
			
def update_grid(gridF):
	wsize = len(gridF)
	zsize = len(gridF[0])
	ysize = len(gridF[0][0])
	xsize = len(gridF[0][0][0])
	gridnew = [[[['.' for x in range(xsize)] for y in range(ysize)] for z in range(zsize)] for w in range(wsize)]
	for w in range(1,wsize-1):
		for z in range(1,zsize-1):
			for y in range(1,ysize-1):
				for x in range(1,xsize-1):
					gridnew[w][z][y][x] = update(gridF,w,z,y,x)
	return gridnew


from copy import deepcopy

f = open('17-data','r')

cycles = 6
grid_input = []

for line in f:
	grid_input.append(line.strip())

wsize = 2*cycles + 3
zsize = 2*cycles + 3
ysize = len(grid_input) + 2*cycles + 2
xsize = len(grid_input[0]) + 2*cycles + 2

grid0 = [[[['.' for x in range(xsize)] for y in range(ysize)] for z in range(zsize)] for w in range(wsize)]

wnew = int((wsize-1)/2)
znew = int((zsize-1)/2)
for y in range(len(grid_input)):
	ynew = y + cycles + 1
	for x in range(len(grid_input[0])):
		xnew = x + cycles + 1
		grid0[wnew][znew][ynew][xnew] = grid_input[y][x]

grid = deepcopy(grid0)

for i in range(cycles):
	print('cycle',i+1)
	grid = update_grid(grid)

# printgrid(grid)

actcubes = 0
for w in range(len(grid)):
	for z in range(len(grid[0])):
		for y in range(len(grid[0][0])):
			for x in range(len(grid[0][0][0])):
				if grid[w][z][y][x] == '#':
					actcubes += 1

print('active cubes:',actcubes)