# define a function that returns the priority for a given input character
def get_priority(item):
	if ord(item) <= 90: # need to subtract different numbers to the ascii code of a character depending on whether it is a uppercase or lowercase letter
		return ord(item)-38
	else:
		return ord(item)-96


with open("3-data","r") as f:
	rucksacks = [line.strip() for line in f.readlines()]
	
common = 0
	
# loop over every rucksack and split them into two equal compartments
# find the item commone to both compartments and add its priority to the total
for rucksack in rucksacks:
	middle = int(len(rucksack)/2)
	comp1 = rucksack[:middle]
	comp2 = rucksack[middle:]
	for item in comp1:
		if item in comp2:
			common += get_priority(item)
			break

# print the total priority of common items in every rucksack
print(common)

badges = 0

# loop over every group of 3 rucksacks
# find the common item to every group and add its priority to the total
for i in range(0,len(rucksacks)-1,3):
	for item in rucksacks[i]:
		if item in rucksacks[i+1]:
			if item in rucksacks[i+2]:
				badges += get_priority(item)
				break

# print the total priority of every common item in groups of 3 rucksacks
print(badges)