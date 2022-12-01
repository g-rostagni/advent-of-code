elves = []
elf = []

# read from the data file
# use a list comprehension to create an array of all elves containing arrays of what individual elves are carrying
with open("1-data") as f:
	data = f.read()
	elves = [[int(item) if item else 0 for item in elf.split("\n")] for elf in data.split("\n\n")]
		
# sum over calories carried by each elf and sort it from least to most
cals = [sum(elf) for elf in elves]
cals.sort()

# read the highest amount of calories and the sum of the three highest amounts of calories
print(cals[-1])
print(sum(cals[-3:]))
