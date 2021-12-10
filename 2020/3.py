f = open('3-data','r')

data = []

for line in f:
	line = line.rstrip()
	if line:
		data.append(line)

slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
tot = 1

for slope in slopes:
	y = 0
	x = 0
	trees = 0
	
	while y < len(data):
		if data[y][x % len(data[0])] == "#": trees += 1
		x += slope[0]
		y += slope[1]
	
	print(trees)
	tot *= trees
	
print(tot)
