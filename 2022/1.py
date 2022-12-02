# read from the data file
# use a list comprehension to create an array of all elves containing arrays of what individual elves are carrying
with open("1-data") as f:
	elves = [[int(item) for item in elf.split("\n") if item] for elf in f.read().split("\n\n")]
		
# sum over calories carried by each elf and sort it from least to most
cals = [sum(elf) for elf in elves]
cals.sort()

# read the highest amount of calories and the sum of the three highest amounts of calories
print(cals[-1])
print(sum(cals[-3:]))
