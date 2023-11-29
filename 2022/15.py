# define a function that determines whether a given point is excluded by the sensors
def is_excluded(x,y):
	for beacon in coords:									# loop over all beacons
		range_b = abs(beacon[0][0] - beacon[1][0]) + abs(beacon[0][1] - beacon[1][1])	# calculate the range of the beacon
		if abs(beacon[0][0] - x) + abs(beacon[0][1] - y) <= range_b:			# if the point is within range, it is excluded
			return True
	return False										# if it is not in range of any beacon, then it is not


coords = []	# store the coordinates of the sensors and beacons in a list
with open("15-data","r") as f:
	for line in f.readlines():
		l = line.split(" ")
		xs = int(l[2][2:-1])			# the x coordinate of the sensor
		ys = int(l[3][2:-1])			# the y coordinate of the sensor
		xb = int(l[8][2:-1])			# the x coordinate of the beacon
		yb = int(l[9][2:])			# the y coordinate of the beacon
		coords.append([[xs, ys], [xb, yb]])	# store them in coords
		
# part 1
# for this part we sinply compute every point excluded by the sensors at y = 2,000,000
# this means computing a few million points, but we avoid double counting, or having to figure out the total size of the grid
y0 = 2000000	# set the y coordinate at which to look at 2,000,000
exc = set()	# a set that will contain all excluded points for y = y0, to avoid double counting
for sb in coords:								# for each sensor
	range_s = abs(sb[0][0] - sb[1][0]) + abs(sb[0][1] - sb[1][1])		# calculate the range of the sensor
	if abs(y0 - sb[0][1]) <= range_s:					# if the excluded region by the sensor touches the y = y0 line
		width = range_s - abs(y0 - sb[0][1])				# calculate the width of the exclusion diamond at y = y0
		for x in range(sb[0][0] - width, sb[0][0] + width + 1):	# exclude all the points lying in that diamond
			exc.add(x)
	
for beacon in coords:					# for each beacon
	if beacon[1][1] == y0 and beacon[1][0] in exc:	# if the beacon itself lies on the y=y0 line, remove it from the excluded points
		exc.remove(beacon[1][0])
	
print(len(exc))	# print the number of excluded points

# part 2
# for this part, we make the observation that if there is only one non-excluded point on the grid, then it must be on the boundary of an excluded zone. We use this to restrict the set of points to look at to only the ones lying next to an excluded zone, cutting it down to a few millions
# further the excluded point (if it's not in a corner) will be in several boundaries, making it easier to find
# this code runs in about 20 seconds
# one could probably implement this better using intersections of the boundary lines, represented by parametric equations instead of sets of points
# -> HOWEVER: if the hidden beacon happens to lie on the corner of the grid, this won't work as it could not be at the intersection of 2 boundary zones
found = False								
for sensor in coords:									# loop over all sensors, to find the points lying in their boundary
	range_s = abs(sensor[0][0] - sensor[1][0]) + abs(sensor[0][1] - sensor[1][1])	# calculate the range of the sensor
	y_top = sensor[0][1] + range_s							# calculate the height of the top of the excluded region
	y_bot = sensor[0][1] - range_s							# calculate the height of the bottom of the excluded region 
	for y in range(max(0,y_bot-1), min(4000000,y_top+2)):				# loop over the heights all points that lie one step beyond the range (on the boundary), and on the grid
		width_b = range_s - abs(y - sensor[0][1]) + 1				# calculate the width of the boundary zone at that y
		for k in [-1,1]:							# loop over the points on the left and the right of the boundary zone
			x = sensor[0][0] + k*width_b					# get the x coordinate of the boundary point
			if 0 <= x <= 4000000:						# if the point is on the grid
				if not is_excluded(x,y):				# if the point is not excluded by the sensors
					found = True					# we found it!
					break
		if found:
			break
	if found:
		break
	
print(int(4e6*x + y))	# print the frequency of the hidden beacon



# for a given line on the boundary, instead of testing all the line, find the end of exclusion by gradient descent:
# find the sensor that excludes the start of the line
# see if that sensors excludes the end:
#	if yes all the line is excluded
#	if not, test the middle of the line, go on until we pinpoint the end point of the exclusion zone
# update the line and restrict it to a smaller segment until we get nothing, or a single point
def on_grid(p):
	if p[0] < 0:
	
	elif p[
	
	return True if 0 <= p[0] <= 4000000 and 0 <= p[1] <= 4000000 else False

def to_grid(x):
	if x < 0:
		return 0
	elif x > 4000000:
		return 4000000
	else:
		return x
		
lines = []
for sensor in coords:
	range_s = abs(sensor[0][0] - sensor[1][0]) + abs(sensor[0][1] - sensor[1][1])	# calculate the range of the sensor
	c_lef = [sensor[0][0] - range_s, sensor[0][1]]
	c_top = [sensor[0][0], sensor[0][1] + range_s]
	c_rig = [sensor[0][0] + range_s, sensor[0][1]]							
	c_bot = [sensor[0][0], sensor[0][1] - range_s]
	lines += = [[c_lef,c_top,1], [c_top,c_rig,-1], [c_bot,c_rig,1], [c_lef,c_bot,-1]] # order lines so they go left to right, and add y direction

# restrict lines to the grid
# a line is described by 2 points: a,b
# if xa < 0:
#	need to increase xa to 0, modify ya accordingly
# elif xa > 4e6
#	need to decrease xa to 4e6, modify ya accordingly
# if ya < 0:
#	need to increase ya to 0, modify xa accordingly
# elif ya > 4e6:
#	need to decrease ya to 4e0, modify xa accordingly
# do the same for b
for l in range(len(lines)):	# loop over lines
	for p in lines[l]:	# loop over start and end points
		a = lines[l][p]
		if lines[l][p][0] < 0:
			pass
		elif lines[l][p][0] > 4000000:
			pass
		if lines[l][p][1] < 0:
			pass
		elif lines[l][p][1] > 4000000:
			pass
			
	
