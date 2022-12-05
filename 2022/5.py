# define a function that reads the message formed by the top crate on each stack
def print_message(crates):
	message = ''
	for stack in crates:
		message += stack[-1]
	print(message)
	return 0

crates_raw = []
moves = []
i = 0

# read the file
# the crates positions and the instructions for moves are stored in different arrays
with open("5-data","r") as f:
	for line in f.readlines():
		if not i:
			if line.strip():
				crates_raw.append(line)
			else:
				i = 1
		else:
			moves.append(line.strip().split(' '))
	
# generate 2 lists of lists containing each crate (one for part 1 and one for part 2)
# each list contains a stack of crates with the top one at the end
crates1 = [[] for i in range(9)]
crates2 = [[] for i in range(9)]
for line in reversed(crates_raw[:-1]):
	for i in range(9):
		j = 4*i + 1
		if line[j] != " ":
			crates1[i].append(line[j])
			crates2[i].append(line[j])

# read the moves and perform them
for move in moves:
	n = int(move[1])					# read the number of moves to perform
	orig = int(move[3]) - 1					# read which stack the crates are taken from
	dest = int(move[5]) - 1					# read which stack the crates are moved to
	crates2[dest] += crates2[orig][-n:] 			# add the last n crates of one stack to another at once (part 2)
	for i in range(n):
		crates1[dest].append(crates1[orig].pop(-1))	# move the last n crates of one stack to another one at a time (part 1)
		crates2[orig].pop(-1) 				# remove the last n crates from the origin stack after having added them to the destination stack (part 2)

# print the messages formed by the top crates
print_message(crates1)
print_message(crates2)
