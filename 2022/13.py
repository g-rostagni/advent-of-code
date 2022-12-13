# define a function to recursively read the string input from position i and convert it to a list of lists
def read_rec(i,string):	
	x = []						# the sublist we are looking at
	n = ""						# the number to add (need this to account for 10s in the data)
	while i < len(string):				# while we haven't reached the end of the string
		char = string[i]			
		if char == "[":				# if we are looking at an open bracket
			i,x2 = read_rec(i+1,string)	# new list, so add one level of recursion and read the substring
			x.append(x2)			# add the processed substring to x
		elif char == "]":			# if we are looking at a closed bracket:
			if n:				# process the number if we read one before meeting this closed bracket
				x.append(int(n))
				n = ""
			return i+1,x			# return the processed sublist x
		elif char == ",":			# if we are looking at a comma
			if n:				# process the number if we read one
				x.append(int(n))
				n = ""
			i += 1				# move down one spot in the string
		else:					# if we see a number
			n += char			# add the character to n
			i += 1				# move down one spot
	return i,x					# if we reached the end of the string, return it and the final position
	
# define a function that compares two integers	
def compare_int(int1,int2):
	if int1 > int2:
		return -1	# -1 for wrong order
	elif int1 < int2:
		return 1	# 1 for right order
	else:
		return 0	# 0 if they are equal
			
# define a function that compares two lists
def compare_list(list1,list2):
	for el1,el2 in zip(list1,list2):			# loop over both lists and read elements
		if type(el1) == int and type(el2) == int:	# if they are both integers, compare them
			c = compare_int(el1,el2)
		elif type(el1) == int:				# if one is an integer, convert it to a single element list and compare them
			c = compare_list([el1],el2)
		elif type(el2) == int:				# if the other in an integer, convert it to a single element list and compare them
			c = compare_list(el1,[el2])
		else:						# if they are both lists, compare them
			c = compare_list(el1,el2)
			
		if c:						# if the result of the comparison for the elements is conclusive (either right or wrong), return this result
			return c
		# if the comparison is inconclusive move on, until we reach the end of one the lists
			
	if len(list1) < len(list2):	# if list1 is shorter, they are in the right order
		return 1
	elif len(list1) > len(list2):	# if list1 is longer, they are in the wrong order
		return -1
	else:
		return 0		# otherwise return an inconclusive result

# define a function that performs the quicksort algorithm
def quicksort(data):
	if len(data) < 2:						# if the data is too small, there is nothing to sort
		return data
	pivot = data[-1]						# define the last element of the data as the pivot
	part1 = []
	part2 = []
	for inp in data[:-1]:						# loop over all other elements of the data
		if compare_list(inp,pivot) == 1:			# if they are "smaller" than the pivot:
			part1.append(inp)				# add them to the first partition
		else:							# otherwise:
			part2.append(inp)				# add them to the second partition
	data_sorted = quicksort(part1) + [pivot] + quicksort(part2)	# recursively call the quicksort algorithm on the two partitions and concatenate the resulting sublists together to obtain a sorted list
	return data_sorted
	

# import the input as a string
with open("13-test","r") as f:
	data = [[line for line in pair.split("\n") if line] for pair in f.read().split("\n\n")]
	#inputs = [eval(line) for line in f.readlines() if line.strip()]

inputs = []	# define the list that will contain all the inputs

for pair in data:			# loop over all pairs of inputs
	for inp in pair:		# loop over each individual input
		n,i = read_rec(1,inp)	# transform the raw input into lists of lists (start at 1 to ignore the first bracket)
		inputs.append(i)	# add the formatted input to the "inputs" list

# calculate the sum of indices of sorted pairs
tot = 0
for i in range(0,len(inputs)-1,2):			# loop over inputs 2 by 2
	if compare_list(inputs[i],inputs[i+1]) == 1:	# compare consecutive inputs, and if they are in the right order:
		tot += int(i/2) + 1			# add the position of the pair to the total

# calculate the key for the dividers positions in the sorted inputs
inputs += [[[2]], [[6]]]			# add the two dividers to the input
key = 1
for i,el in enumerate(quicksort(inputs)):	# loop over the sorted input
	if el == [[2]]:				# if one is found update the key
		key *= i+1
	elif el == [[6]]:			# if the other is found update the key
		key *= i+1
		break				# break since the inputs are sorted and we know this is the second divider

print(tot)
print(key)
