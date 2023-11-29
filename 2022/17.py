def move_LR(block,direc):
	blocknew = [[a for a in b] for b in block]
	for i in range(len(block)):
		blocknew[i][1] += direc
		blocknew[i][2] += direc
		if blocknew[i][1] < 0 or blocknew[i][2] > 6:
			return block
		if chamber[blocknew[i][0]][blocknew[i][1]] == "#" or chamber[blocknew[i][0]][blocknew[i][2]] == "#":
			return block
	return blocknew
	
def check_hit(block):
	for i in range(len(block)):
		if block[i][0] == -1:
			return True
		for x in range(block[i][1], block[i][2]+1):
			if chamber[block[i][0]][x] == "#":
				return True
	return False

def move_down(block):
	blocknew = [[a for a in b] for b in block]
	for i in range(len(block)):
		blocknew[i][0] -= 1
	if check_hit(blocknew):
		rock_rest(block)
		return block,True
	else:
		return blocknew,False

def rock_rest(block):
	for i in range(len(block)):
		for x in range(block[i][1], block[i][2]+1):
			chamber[block[i][0]] = chamber[block[i][0]][:x] + "#" + chamber[block[i][0]][x+1:]

def drop_blocks():
	global blocks_fallen
	global top
	global j
	block = blocks[blocks_fallen%len(blocks)]

	for i in range(len(block)):
		block[i][0] = top + 3 + i
	
	while len(chamber) <= block[-1][0]:
		chamber.append(".......")

	# move block
	stopped = False
	while not stopped:
		# move block sideways
		if jets[j%len(jets)] == "<":
			# move left
			block = move_LR(block,-1)
		else:
			# move right
			block = move_LR(block,1)
		j += 1
		
		# move down
		block,stopped = move_down(block)
	
	blocks_fallen += 1
	for i in range(len(chamber)-1,-1,-1):
		if "#" in chamber[i]:
			top = i+1
			break
	





with open("17-data","r") as f:
	jets = f.read().strip()
	

chamber = []
top = 0

# blocks are written as a list of each of their line, with the lowest line first
# then the format is [height, leftmost position, rightmost position]
blocks = [[[0,2,5]],
	[[0,3,3], [0,2,4], [0,3,3]],
	[[0,2,4], [0,4,4], [0,4,4]],
	[[0,2,2], [0,2,2], [0,2,2], [0,2,2]],
	[[0,2,3], [0,2,3]]]


blocks_tot = 3512
#blocks_tot = 1000000000000

j = 0	
blocks_fallen = 0
skip = False

filled = False
periods = []
while True:
	if blocks_fallen%len(blocks) == 0:
		periods.append([j%len(jets),blocks_fallen,top])
		for p in periods[:-1]:
			if j%len(jets) == p[0]:
				period_start = p[1]
				period_blocks = blocks_fallen - p[1]
				period_jet = p[0]
				period_height = top - p[2]
				print("period found, at",period_start,"with periodicity",period_blocks,"and height",period_height,"and jet number",period_jet)
				skip = True
				break
		
	if skip:
		break
	
	drop_blocks()
	

	
# compute height with one period
chamber = []
top = 0
j = 0
blocks_fallen = 0
while blocks_fallen < period_start + period_blocks:
	drop_blocks()
top_1per = top	
chamber_1per = [a for a in chamber]
j_1per = j

print("Blocks fallen after 1 period:\t", blocks_fallen)
print("Height reached after 1 period:\t", top)
print("Jet number after 1 period:\t", j%len(jets))

# add another period on top to get the true period height
blocks_fallen = 0
while blocks_fallen < period_blocks:
	drop_blocks()

true_height = top - top_1per
print(true_height)

top_before = top
blocks_before = blocks_fallen
	


cycles = int( (blocks_tot-period_start) / period_blocks) - 1

print("")
print("Cycles to perform:\t", cycles)
print("Height added by these cycles:\t", true_height*cycles)

chamber = [a for a in chamber_1per]
for l in reversed(chamber[-15:]):
	print(l)	
	
top = top_1per
j = j_1per
blocks_fallen = 0
while blocks_fallen < blocks_tot - period_start - (cycles+1)*period_blocks:
	drop_blocks()

for l in reversed(chamber[-15:]):
	print(l)	
	
	
print("")
print("Blocks fallen after period ended:\t", blocks_fallen)
print("Height reached after period ended:\t", top- top_1per)
	
tot_height = top_1per + true_height*(cycles) + top - top_1per
print(tot_height)

chamber = []
j = 0
blocks_fallen = 0
top = 0
while blocks_fallen < period_start + 3*period_blocks:
	drop_blocks()
print(top)


for l in reversed(chamber[-15:]):
	print(l)	


# find period
# compute height before period starts
# compute height of periods times number of cycles
# compute height of leftover pattern







