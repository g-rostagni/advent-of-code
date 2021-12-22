def import_data(filename):
	f = open(filename,'r')
	data = []
	for line in f:
		d = []
		l = line.split(' ')
		if l[0] == 'on':
			d.append(1) 
		else:
			d.append(0)
		ll = l[1].split(',')
		for coord in ll:
			c = coord.split('=')
			cc = c[1].split('..')
			d.append([int(cc[0]),int(cc[1])])
		data.append(d)
	return data
	
def get_cuboid_size(cuboid):
	size = 1
	for c in cuboid:
		size *= c[1] - c[0] +1
	return size
	
def find_1_overlap(stepA,stepB):
	overlap = []
	for c0,c1 in zip(stepA,stepB):
		ol = [max(c0[0],c1[0]),min(c0[1],c1[1])]
		if ol[0] > ol[1]:
			return False
		overlap.append(ol)
	return overlap
	
def subtract_cube(cubeA,cubeB,allcubes):
	overlap = find_1_overlap(cubeA,cubeB)
	if overlap:
		allcubes.remove(cubeA)
		chopped = []
		chopped.append([[cubeA[0][0],cubeA[0][1]], [cubeA[1][0],cubeA[1][1]], [cubeA[2][0],overlap[2][0]-1]])
		chopped.append([[cubeA[0][0],cubeA[0][1]], [cubeA[1][0],cubeA[1][1]], [overlap[2][1]+1,cubeA[2][1]]])
		chopped.append([[cubeA[0][0],cubeA[0][1]], [cubeA[1][0],overlap[1][0]-1], [overlap[2][0],overlap[2][1]]])
		chopped.append([[cubeA[0][0],cubeA[0][1]], [overlap[1][1]+1,cubeA[1][1]], [overlap[2][0],overlap[2][1]]])
		chopped.append([[cubeA[0][0],overlap[0][0]-1], [overlap[1][0],overlap[1][1]], [overlap[2][0],overlap[2][1]]])
		chopped.append([[overlap[0][1]+1,cubeA[0][1]], [overlap[1][0],overlap[1][1]], [overlap[2][0],overlap[2][1]]])
		for smallcube in chopped:
			if get_cuboid_size(smallcube):
				allcubes.append(smallcube)
	return allcubes
  
def subtract_all_cubes(allcubes,step):
	ac = allcubes.copy()
	for cube in allcubes:
		ac = subtract_cube(cube,step,ac)
	return ac

def get_lit_cubes(allcubes):
	nlit = 0
	for cube in allcubes:
		nlit += get_cuboid_size(cube)
	return nlit
	
	
steps = import_data('22-data')

allcubes = [steps[0][1:]]

for i in range(1,len(steps)):
	step = steps[i][1:]
	allcubes = subtract_all_cubes(allcubes,step)		
	if steps[i][0] == 1:
		allcubes.append(step)

print(get_lit_cubes(allcubes))
