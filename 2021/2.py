f = open('2-data','r')
data = []

for line in f:
	n = line.split()
	if n:
		print(n,n[0],n[1])
		data.append([n[0],int(n[1])])
		
depth = 0
dist = 0
aim = 0

for line in data:
	print(line)
	if line[0] == 'up':
		aim -= line[1]
	elif line[0] == 'down':
		aim += line[1]
	elif line[0] == 'forward':
		dist += line[1]
		depth += aim*line[1]

print(depth)
print(dist)
print(depth*dist)
