def line_c(c1,c2):
	l = []
	if c1 <= c2:
		for c in range(c1,c2+1):
			l.append(int(c))
	else:
		for c in range(c1,c2-1,-1):
			l.append(int(c))
	return l
	
def diag_xy(x1,x2,y1,y2):
	d = []
	xs = line_c(x1,x2)
	ys = line_c(y1,y2)
	for i in range(len(xs)):
		d.append([xs[i],ys[i]])
	return d

f = open('5-data','r')

data = []

xmax = 0
ymax = 0
for line in f:
	l = line.strip().split('->')
	l2 = [l[0].split(','), l[1].split(',')]
	for i in range(len(l2)):	
		for j in range(len(l2[i])):
			l2[i][j] = int(l2[i][j])
		xmax = max(xmax,l2[i][0])
		ymax = max(ymax,l2[i][1])
	data.append(l2)

grid = [[0 for x in range(xmax+1)] for y in range(ymax+1)]

for pair in data:
	x1 = pair[0][0]
	x2 = pair[1][0]
	y1 = pair[0][1]
	y2 = pair[1][1]
	if x1 == x2:
		for y in line_c(y1,y2):
			grid[y][x1] += 1
	elif y1 == y2:
		for x in line_c(x1,x2):
			grid[y1][x] += 1
	elif abs(x2 - x1) == abs(y2 - y1):
		for x,y in diag_xy(x1,x2,y1,y2):
			grid[y][x] += 1
	else:
		pass

overlap = 0
for line in grid:
	for n in line:
		if n >= 2:
			overlap += 1
			
print(overlap)