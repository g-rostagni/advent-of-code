def test_win(grid):
	for row in grid:
		i = 0
		for n in row:
			if n == 'D':
				i +=1
		if i == 5:	
			return True
	for col in range(5):
		i = 0
		for n in range(5):
			if grid[n][col] == 'D':
				i += 1
		if i == 5:
			return True
	return False

def print_grid(grid):
	print('')
	for row in grid:
		print(row)
	return 0

from copy import deepcopy

f = open('4-data','r')

data = []
l = []

for line in f:
	line = line.strip()
	if line:
		l.append(line)
	else:
		data.append(l)
		l = []
if l:
	data.append(l)
	
nums = data[0][0].split(',')

grids = []
l = []
for grid in data[1:]:
	for line in grid:
		l.append(line.split())
	grids.append(l)
	l = []


for num in nums:
	grids_copy = []
	for g in range(len(grids)):
		grid = grids[g]
		for i in range(5):
			for j in range(5):
				if grid[i][j] == num:
					grids[g][i][j] = 'D'
		if not test_win(grid):
			grids_copy.append(grid)
	grids = deepcopy(grids_copy)
	if len(grids) == 0:
		lastgrid = grid
		break

unmarked = 0
for row in lastgrid:
	for n in row:
		if n != 'D':
			unmarked += int(n)

print(unmarked,int(num),unmarked*int(num))