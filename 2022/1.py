elves = []
elf = []

# read from the data file
# temporarily stores the indiviual foodstuff carried by one elf in an array
# when meeting an empty line, store the calories carried by one elf into the elves array and move on
with open("1-data") as f:
	for line in f:
		if line.strip():
			elf.append(int(line.strip()))
		else:
			elves.append(elf)
			elf = []
		
# sum over calories carried by each elf and sort it from least to most
cals = [sum(elf) for elf in elves]
cals.sort()

# read the highest amount of calories and the sum of the three highest amounts of calories
print(cals[-1])
print(sum(cals[-3:]))
