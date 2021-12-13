def import_data(filename):
        f = open(filename,'r')
        data = set()
        data2 = []
        line = f.readline()
        while line.strip():
        	l = line.strip().split(',')
        	data.add((int(l[0]), int(l[1])))
        	line = f.readline()
        line = f.readline()
        while line.strip():
        	l = line.strip().split(' ')
        	ll = l[2].split('=')
        	data2.append([ll[0], int(ll[1])])
        	line = f.readline()
        return data, data2

def x_fold(x0,data):
	datanew = set()
	for p in data:
		if p[0] < x0:
			datanew.add(p)
		elif p[0] > x0:
			datanew.add((2*x0 - p[0], p[1]))
	return datanew
	
def y_fold(y0,data):
	datanew = set()
	for p in data:
		if p[1] < y0:
			datanew.add(p)
		elif p[1] > y0:
			datanew.add((p[0], 2*y0 - p[1]))
	return datanew


data, folds = import_data('13-data')

for fold in folds:
	if fold[0] == 'x':
		data = x_fold(fold[1],data)
	else:
		data = y_fold(fold[1],data)

xmax = 0
ymax = 0
for p in data:
	xmax = max(xmax,p[0])
	ymax = max(ymax,p[1])

grid = [' '*(xmax+1) for i in range(ymax+1)]

for p in data:
	grid[p[1]] = grid[p[1]][:p[0]] + '#' + grid[p[1]][p[0]+1:]

for line in grid:
	print(line)
