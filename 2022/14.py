# read the data
with open("14-data","r") as f:
	data = [[coord.strip().split(",") for coord in line.split("->")] for line in f.readlines()]
	data = [[[int(n) for n in coord] for coord in line] for line in data]

filled = set()	# define a set containing all filled points
y_abyss = 0	# define a variable that will contain the height of the floor

# generate the set of filled points
for line in data:							# loop over all lines
	for i in range(len(line) - 1):					# loop over all points in a line
		if line[i][0] == line[i+1][0]:				# horizontal rock line
			ymin = min(line[i][1],line[i+1][1])
			ymax = max(line[i][1],line[i+1][1])
			for y in range(ymin, ymax+1):			# add all the points in the rock line to the set
				filled.add((line[i][0],y))
		elif line[i][1] == line[i+1][1]:			# vertical rock line
			xmin = min(line[i][0],line[i+1][0])
			xmax = max(line[i][0],line[i+1][0])
			for x in range(xmin, xmax+1):			# add all the points in the rock line to the set
				filled.add((x,line[i][1]))
		y_abyss = max(y_abyss, line[i][1], line[i+1][1])	# update the maximum depth
	
y_abyss += 2							# set the depth of the floor
n_sand = 0							# count the grains of sand that came to a rest
into_the_abyss = False						# define a variable to tell us when the first grain of sand reaches the floor/abyss
while True:							# while we haven't filled up the cave
	sand = (500,0)						# set the source
	if sand in filled:					# if the pile of sand goes up to the source, stop
		break
	while True:						# while the sand is stll falling
		if not (sand[0], sand[1]+1) in filled:		# if nothing underneath, fall straight down
			sand = (sand[0], sand[1]+1)
		elif not (sand[0]-1, sand[1]+1) in filled:	# if the left is free, fall to the left
			sand = (sand[0]-1, sand[1]+1)
		elif not (sand[0]+1, sand[1]+1) in filled:	# if the right is free, fall to the right
			sand = (sand[0]+1, sand[1]+1)
		else:						# if nothing is free, come to a rest
			filled.add(sand)			# add the grain to the filled set
			n_sand += 1				# add one to the sand count
			break					# move on to the next grain
			
		if sand[1]+1 == y_abyss:			# if we have reached the floor
			if not into_the_abyss:			# if we have reached the floor for the first time
				n_abyss = n_sand		# note the number of grains that fell before we reached the floor/abyss
				into_the_abyss = True
			filled.add(sand)			# add the grain to the filled set
			n_sand += 1				# add one to the sand count
			break					# move on to the next grain
			
print(n_abyss)
print(n_sand)
