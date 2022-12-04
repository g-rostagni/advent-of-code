# function that determines whether range2 is fully contained within range1
def is_contained(range1,range2):
	if range2[0] >= range1[0] and range2[1] <= range1[1]:
		return True
	else:
		return False

# function that determines whether range1 and range2 overlap
def does_overlap(range1,range2):
	if range2[0] >= range1[0] and range2[0] <= range1[1]:
		return True
	elif range2[1] >= range1[0] and range2[1] <= range1[1]:
		return True
	elif range1[0] >= range2[0] and range1[0] <= range2[1]:
		return True
	elif range1[1] >= range2[0] and range1[1] <= range2[1]:
		return True
	else:
		return False
		
	
assignments = []

# reads the data into an array containing the ranges for each assignment
with open("4-data","r") as f:
	for line in f.readlines():
		l = line.strip().split(",")
		assign = []
		for sections in l:
			s = sections.split("-")
			a = [int(n) for n in s]
			assign.append(a)
		assignments.append(assign)
	
contained = 0
overlap = 0
	
# for every elf pair, count the number of fully contained and overlapping pairs
for pair in assignments:
	if is_contained(pair[0],pair[1]) or is_contained(pair[1],pair[0]):
		contained += 1
	if does_overlap(pair[0],pair[1]):
		overlap += 1
		
print(contained)
print(overlap)