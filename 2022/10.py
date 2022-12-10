with open("10-data","r") as f:
	instructions = [[l for l in line.strip().split(" ")] for line in f.readlines()]

# initialise a bunch of stuff
x = 1			# X, the position of the sprite
cyc = 0			# the current cycle
line = 0		# the line of the instructions to read
adding = False	# whether the CPU is busy adding a number for this cycle
strength = 0	# the total strength for part 1
crt = ""		# the CRT display for part 2
	
# loop through CPU cycles while we haven't reached the end of the instructions
while line < len(instructions):
	cyc += 1									# update the CPU cycle
	
	# update the CRT
	pix = (cyc-1) % 40							# determine the position of the pixel
	if not pix:									# add a new line when we need to start a new line
		crt += "\n"
	crt += "#" if x-1 <= pix <= x+1 else " "	# print a lit pixel if the sprite is in the right position
	
	# add the strength for the 20th, 60th... cycles
	if not (cyc - 20) % 40:
		strength += cyc*x
	
	# at the end of the cycle, read the instruction
	if not adding:								# if the CPU is not busy adding
		if instructions[line][0] == "noop":		# if noop, just move on to the next line
			line += 1
		elif instructions[line][0] == "addx":	# if addx, the CPU is busy and will do the addition next cycle
			adding = True
			added = int(instructions[line][1])
	else:
		x += added								# add to x
		adding = False							# CPU not busy anymore
		line += 1								# move on to the next line of instructions
		
print(strength)
print(crt)