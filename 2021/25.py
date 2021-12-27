# why was this one so easy?

def import_data(filename):
	f = open(filename,'r')
	data = [[c for c in line.strip()] for line in f]
	return data
	
	
def printgrid(grid):
	print('')
	for line in grid:
		for c in line:
			print(c,end='')
		print('')
		
def move_east(grid):
	moved = False
	gridnew = copy.deepcopy(grid)
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			jplus = j+1 if j < len(grid[0])-1 else 0	
			if grid[i][j] == '>' and grid[i][jplus] == '.':
				gridnew[i][j] = '.'
				gridnew[i][jplus] = '>'
				moved = True
	return gridnew,moved

def move_south(grid):
	moved = False
	gridnew = copy.deepcopy(grid)
	for i in range(len(grid)):
		iplus = i+1 if i < len(grid)-1 else 0
		for j in range(len(grid[0])):	
			if grid[i][j] == 'v' and grid[iplus][j] == '.':
				gridnew[i][j] = '.'
				gridnew[iplus][j] = 'v'
				moved = True
	return gridnew,moved


import copy
import os

grid = import_data('25-data')
printgrid(grid)

step = 0
movedE = True
movedS = True
while movedE or movedS:
	grid,movedE = move_east(grid)
	grid,movedS = move_south(grid)
	step += 1
	os.system('clear')
	printgrid(grid)

print('step:',step)
