def printgrid(grid):
	print('')
	for flatgrid in grid:
		print('/////////////////////////////////////////////////')
		for line in flatgrid:
			for char in line:
				print(char,end='')
			print('')
		
def neighbours(z,y,x):
	nb = []
	for k in range(z-1,z+2):
		for j in range(y-1,y+2):
			for i in range(x-1,x+2):
				if not [k,j,i] == [z,y,x]:
					nb.append([k,j,i])
	return nb
		
def update(gridF,z,y,x):
	act = 0
	for k,j,i in neighbours(z,y,x):
		if gridF[k][j][i] == '#':
			act += 1
	if gridF[z][y][x] == '#':
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
	zsize = len(gridF)
	ysize = len(gridF[0])
	xsize = len(gridF[0][0])
	gridnew = [[['.' for x in range(xsize)] for y in range(ysize)] for z in range(zsize)] 
	for z in range(1,zsize-1):
		for y in range(1,ysize-1):
			for x in range(1,xsize-1):
				gridnew[z][y][x] = update(gridF,z,y,x)
	return gridnew

from copy import deepcopy
f = open('17-data','r')

cycles = 6
grid_input = []

for line in f:
	grid_input.append(line.strip())

zsize = 2*cycles + 3
ysize = len(grid_input) + 2*cycles + 2
xsize = len(grid_input[0]) + 2*cycles + 2

grid0 = [[['.' for x in range(xsize)] for y in range(ysize)] for z in range(zsize)]

znew = int((zsize-1)/2)
for y in range(len(grid_input)):
	ynew = y + cycles + 1
	for x in range(len(grid_input[0])):
		xnew = x + cycles + 1
		grid0[znew][ynew][xnew] = grid_input[y][x]

grid = deepcopy(grid0)

for i in range(cycles):
	print('')
	print('cycle',i+1)
	grid = update_grid(grid)

printgrid(grid)

actcubes = 0
for z in range(len(grid)):
	for y in range(len(grid[0])):
		for x in range(len(grid[0][0])):
			if grid[z][y][x] == '#':
				actcubes += 1

print('active cubes:',actcubes)