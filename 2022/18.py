# define a function that returns the total number of exposed sides for a set of cubes
def get_sides(cubes):
	sides = 0
	for cube in cubes:								# loop over all cubes
		for adj in [[0,0,1], [0,0,-1], [0,1,0], [0,-1,0], [1,0,0], [-1,0,0]]:	# loop over all neighbouring positions
			if not tuple(cube[i] + adj[i] for i in range(3)) in cubes:	# if there is no neighbour, this side is free
				sides += 1
	return sides

# import the positions of the lava cubes
with open("18-data") as f:
	lavacubes = {tuple(int(c) for c in line.strip().split(",")) for line in f.readlines()}

# get the total number of sides of the lavacubes
lavasides = get_sides(lavacubes)
print(lavasides)

# for part 2, to obtaine trapped cubes, we first generate all the cubes on the grid and subtract the lava cubes and the cubes reachable by the air

# get the size of the 3d grid
xmax = 0
xmin = 1000
ymax = 0
ymin = 1000
zmax = 0
zmin = 1000
for cube in lavacubes:
	xmax = max(cube[0],xmax)
	xmin = min(cube[0],xmin)
	ymax = max(cube[1],ymax)
	ymin = min(cube[1],ymin)
	zmax = max(cube[2],zmax)
	zmin = min(cube[2],zmin)
	
# generate a set containing all cubes filled with air
trappedcubes = set()
for x in range(xmin, xmax+1):					# loop over
	for y in range(ymin, ymax+1):				# the whole
		for z in range(zmin, zmax+1):			# grid
			if not (x,y,z) in lavacubes:		# if the cube isn't filled with lava, add it
				trappedcubes.add((x,y,z))

# generate the set of all cubes that air can reach
# starting with all the cubes on the external sides of the grid
extcubes = set()
for x in range(xmin, xmax+1):
	for y in range(ymin, ymax+1):
		for z in [zmin,zmax]:
			if not (x,y,z) in lavacubes:
				extcubes.add((x,y,z))
for x in range(xmin, xmax+1):
	for y in [ymin,ymax]:
		for z in range(zmin, zmax+1):
			if not (x,y,z) in lavacubes:
				extcubes.add((x,y,z))
for x in [xmin, xmax]:
	for y in range(ymin, ymax+1):
		for z in range(zmin, zmax+1):
			if not (x,y,z) in lavacubes:
				extcubes.add((x,y,z))

# now, iteratively propagate the air from these cubes until we reach a steady state
stable = False
while not stable:													# while new cubes are being filled
	stable = True
	newcubes = {a for a in extcubes}										# make a copy
	for cube in extcubes:												# loop over all cubes we have filled so far
		for adj in [[0,0,1], [0,0,-1], [0,1,0], [0,-1,0], [1,0,0], [-1,0,0]]:					# consider all neighbours
			cubenew = tuple(cube[i] + adj[i] for i in range(3))						# the neighbouring cube
			if xmin <= cubenew[0] <= xmax and ymin <= cubenew[1] <= ymax and zmin <= cubenew[2] <= zmax :	# if it is on the grid
				if not cubenew in extcubes and not cubenew in lavacubes:				# and if is not already filled and not already filled with lava
					newcubes.add(cubenew)								# add it to the new set of cubes
					stable = False
	extcubes = {a for a in newcubes}										# update extcubes

# now, remove all the cubes we filled with air from the outside from the cubes not containing lava, to obtain the cubes trapped by the lava
for cube in extcubes:
	trappedcubes.remove(cube)	
	
trappedsides = get_sides(trappedcubes)	# get the number of exposed sides of the trapped cubes
print(lavasides - trappedsides)		# subtract these from the total number of exposed sides of the lava cubes to obtain the answer
