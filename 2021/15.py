def import_data(filename):
        f = open(filename,'r')
        data = [line.strip() for line in f]
        return data
        
def big_grid(data):
	biggrid = []
	for y in range(5*len(data)):
		line = []
		for x in range(5*len(data[0])):
			val = int(data[y%len(data)][x%len(data[0])]) + int(y/len(data)) + int(x/len(data[0]))
			if val > 9:
				val %= 9
			line.append(val)
		biggrid.append(line)
	return biggrid

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
	
def update1gen(queue,costs,data):
	def keycost(p):
		return costs[p[0]][p[1]]
	queuenext = []
	for parent in queue:
		if parent == [len(costs)-1, len(costs[0])-1]:
			break
		for p in adjacent(parent[0],parent[1],len(data),len(data[0])):
			newcost = costs[parent[0]][parent[1]] + int(data[p[0]][p[1]])
			if newcost < costs[p[0]][p[1]]:
				costs[p[0]][p[1]] = newcost
				queuenext.append(p)
	queuenext.sort(key=keycost)
	return queuenext,costs

data = import_data('15-data')

data = big_grid(data)

costs = [[10000 for p in line] for line in data]
costs[0][0] = 0
queue = [[0,0]]

while queue:
	queue,costs = update1gen(queue,costs,data)
		
print(costs[len(costs)-1][len(costs[0])-1])
