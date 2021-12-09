def look(gridF,y,x,direction):
	y += direction[0]
	x += direction[1]
	try:
		while gridF[y][x] == '.':
			y += direction[0]
			x += direction[1]
	except IndexError:
		pass
	return [y,x]
	
def visible_seat(gridF,y,x):
	vseats = []
	for direction in directions:
		vseats.append(look(gridF,y,x,direction))
	return vseats
	
	

def update_seats(gridF):
	updated = 0
	gridnew = deepcopy(gridF)
	for y in range(len(gridF)):
		for x in range(len(gridF[0])):
			if gridF[y][x] == '.':
				continue
			nocc = 0
			for seat in visible_seat(gridF,y,x):
				if not (0 <= seat[0] < len(gridF) and 0 <= seat[1] < len(gridF[0])):
					continue
				if gridF[seat[0]][seat[1]] == '#':
					nocc += 1
			if gridF[y][x] == 'L' and nocc == 0:
				gridnew[y][x] = '#'
				updated += 1
			elif gridF[y][x] == '#' and nocc >= 5:
				gridnew[y][x] = 'L'
				updated += 1
	return gridnew,updated

from copy import deepcopy

f = open('11-data','r')

data = []
for line in f:
	l = []
	for n in line.strip():
		l.append(n)
	data.append(l)

directions = []
for a in [-1,0,1]:
	for b in [-1,0,1]:
		if [a,b] != [0,0]:
			directions.append([a,b])

cycle = 0
upd = 1
while upd:
	cycle +=1
	data,upd = update_seats(data)
	print('cycle:',cycle,', seats updated:',upd)
	
nocc = 0
for line in data:
	for seat in line:
		if seat == '#':
			nocc += 1
			
print('occupied seats:',nocc)