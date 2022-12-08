# define a function that returns the line of sight from a tree in one direction and whether this tree is visible from the outside
def get_LOS(y,x,direction):
	# initialise position of the new tree to compare
	y2 = y + direction[0]
	x2 = x + direction[1]
	los = 0
	while 0 <= y2 < len(grid) and 0 <= x2 < len(grid[0]):	# while we haven't reached the edge
		los += 1					# add one to the line of sight for every tree we compare to
		if grid[y2][x2] >= grid[y][x]:			# if we find a tree that is higher, return the line of sight and that the tree is not visible for this direction
			return los,False
		y2 += direction[0]
		x2 += direction[1]
	return los,True						# if we have not found a higher tree, return the line of sight and that the tree is visible for this direction


with open("8-data","r") as f:
	grid = [[int(tree) for tree in line.strip()] for line in f.readlines()]
	
# initialise variables containing the number of visible trees and the maximum scenic score	
visible = 0			
max_score = 0

for y in range(len(grid)):
	for x in range(len(grid[0])):					# loop over the whole grid
		tot_score = 1
		is_visible = False
		for direction in [[0,1], [0,-1], [1,0], [-1,0]]:	# loop over all four directions
			los,vis = get_LOS(y,x,direction)		# get the line of sight and whether the tree is visible for this particular direction
			if vis:						# if the tree is visible for one direction it is visible for all directions
				is_visible = True
			tot_score *= los				# add the line of sight to the scenic score
		
		if is_visible:						# if the tree is visible, count it
			visible +=1
		if tot_score > max_score:				# if this scenic score is the new highest, keep it
			max_score = tot_score
						
print(visible)
print(max_score)
