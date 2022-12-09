# define a function that calculates the position of the tail based on that of the head
def move_tail(t_pos,h_pos):
	if abs(t_pos.real - h_pos.real) > 1 or abs(t_pos.imag - h_pos.imag) > 1:	# check whether the tail actually needs to move
		if t_pos.real != h_pos.real:						# move the x position if they are different 
			t_pos += 1 if h_pos.real > t_pos.real else -1			
		if t_pos.imag != h_pos.imag:						# move the y position if they are different
			t_pos += 1j if h_pos.imag > t_pos.imag else -1j
	return t_pos
	

with open("9-data","r") as f:
	motions = [[l for l in line.strip().split(" ")] for line in f.readlines()]
	
rope_pos = [0 for i in range(10)]	# define an array containing the position of the rope of length 10, from the head (0) to the tail (9), as complex numbers
visited1 = {0}				# define a set containing all positions of the second segment of the rope (the tail in part 1)
visited9 = {0}				# define a set containing all positions of the last segment of the rope

# loop over the motions from the input
for move in motions:
	match move[0]:								# match the 4 possible directions to a heading
		case 'U':
			heading = 1j
		case 'D':
			heading = -1j
		case 'R':
			heading = 1
		case 'L':
			heading = -1
			
	for n in range(int(move[1])):						# repeat the following as many times as needed for one instruction
		rope_pos[0] += heading						# update the head position
		
		for i in range(1,10):						# successively update the positions of all the other segments of the rope
			rope_pos[i] = move_tail(rope_pos[i],rope_pos[i-1])

		visited1.add(rope_pos[1])					# add the new position of the 'first tail' to the set
		visited9.add(rope_pos[9])					# add the new position of the tail to the set
		
# print the number of visited positions for both parts of the problem
print(len(visited1))
print(len(visited9))
