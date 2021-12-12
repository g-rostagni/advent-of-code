def import_data(filename):
        f = open(filename,'r')
        connections = {}
        for line in f:
        	l = line.strip().split('-')
        	if not l[0] in connections:
        		connections[l[0]] = []
        	connections[l[0]].append(l[1])
        	if not l[1] in connections:
        		connections[l[1]] = []
        	connections[l[1]].append(l[0])
        return connections

def isvalid(path,cave):
	if cave in path:
		if cave == 'start':
			return False
		for cave2 in path:
			if cave2.islower() and path.count(cave2) == 2:
				return False
	return True

import copy

data = import_data('12-data')

paths = [['start']]
pathscompleted = []

while True:
	pathsnew = []
	for path in paths:
		for cave in data[path[-1]]:
			if cave.isupper() or isvalid(path,cave):
				p = path.copy()
				p.append(cave)
				if cave == 'end':
					pathscompleted.append(p)
				else:
					pathsnew.append(p)
	if not pathsnew:
		print('no new path found')
		break
	paths = copy.deepcopy(pathsnew)
	
print('total paths:',len(pathscompleted))
