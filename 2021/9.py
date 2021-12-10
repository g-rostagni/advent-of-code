def import_data(filename):
        f = open(filename,'r')
        return [line.strip() for line in f]

def adjacent(y,x,ymax,xmax):
	adj = []
	if y-1 >= 0:
		adj.append([y-1,x])
	if y+1 < ymax:	
		adj.append([y+1,x])
	if x-1 >= 0:
		adj.append([y,x-1])
	if x+1 < xmax:
		adj.append([y,x+1])
	return adj
	
def basin(y,x,dataF):
	b = []
	b.append([y, x, int(data[y][x])])
	for p in b:
		for a in adjacent(p[0],p[1],len(dataF),len(dataF[0])):
			l = [a[0], a[1], int(dataF[a[0]][a[1]])]
			if l[2] != 9 and l not in b:
				b.append(l)
	return b

        
data = import_data('9-data')
lows = []
		
for i in range(len(data)):
	for j in range(len(data[0])):
		adjlower = 0
		for a in adjacent(i,j,len(data),len(data[0])):
			if data[a[0]][a[1]] <= data[i][j]:	
				adjlower += 1
		if not adjlower:
			lows.append([i,j,int(data[i][j])])

tot = 0
for low in lows:
	tot += low[2] + 1
print('lows:',tot)


basins = []
for y in range(len(data)):
	for x in range(len(data[0])):
		if data[y][x] != '9':
			b = basin(y,x,data)
			basins.append(b)
			for p in b:
				data[p[0]] = data[p[0]][:p[1]] + '9' + data[p[0]][p[1]+1:]

basins.sort(key=len,reverse=True)
tot = 1
for b in basins[:3]:
	tot *= len(b)
print('lens product:',tot)
