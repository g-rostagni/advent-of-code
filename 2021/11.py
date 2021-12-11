def import_data(filename):
        f = open(filename,'r')
        data = [[int(char) for char in line.strip()] for line in f]
        return data
  

def plus1(data):
	data = [[n+1 for n in line] for line in data]
	return data


def adjacent(y,x,ymax,xmax):
	adj = []
	for i in range(y-1,y+2):
		if 0 <= i < ymax:
			for j in range(x-1,x+2):
				if 0 <= j < xmax:
					if [i,j] != [y,x]:
						adj.append([i,j])
	return adj
	
def printdata(data):
	for line in data:
		print(line)

data = import_data('11-data')

flashes = 0
step = 0

while True:
	data = plus1(data)
	flashing = []
	for y in range(len(data)):
		for x in range(len(data[0])):
			if data[y][x] == 10:
				flashing.append([y,x])
	for f in flashing:
		for a in adjacent(f[0],f[1],len(data),len(data[0])):
			data[a[0]][a[1]] += 1
			if data[a[0]][a[1]] == 10 and a not in flashing:
				flashing.append(a)
	flashes += len(flashing)
	data = [[n if n <= 9 else 0 for n in line] for line in data]
	step += 1
	if len(flashing) == len(data)*len(data[0]):
		break

print('after step:',step)
printdata(data)
print(flashes)
