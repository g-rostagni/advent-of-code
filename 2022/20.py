# import the data
with open("20-data","r") as f:
	numbers = [int(n) for n in f.readlines()]

file_len = len(numbers)
mixes = 1

# define a list that contains the order according to which we need to move the numbers
# ie: [2,0,3,1] means we need to move the second entry first, then the fourth and so on...
moved = [i for i in range(file_len)]

# changes for part 2, comment these out to obtain the result for part 1
mixes = 10
numbers = [n*811589153 for n in numbers]

for _ in range(mixes):									# how many times to mix the array
	for m in range(file_len):							# loop over the m-th number to move
		for i in range(file_len):						# loop over all the numbers
			if moved[i] != m:						# if we have not found the m-th number to move, keep looking
				continue
			
			n = numbers[i]							# the number that we are moving around
			newpos = i+n							# the new position of the number, obtained by adding it to its current position
					
			while newpos < 0:						# if the new position is smaller than 0, shift it to bring it back into the correct range
				newpos += (file_len-1) * (-int(newpos/file_len)+1)	# account for the fact that the first and last positions are the same
			while newpos >= file_len:					# if the new position is greater than the size of the list, shift it to bring it back into the correct range
				newpos -= (file_len-1) * int(newpos/file_len)
			if n != 0 and newpos == 0:					# if the new position is 0, this means putting the number at the end of the list; unless we have a 0 as the first entry, then it stays
				newpos = file_len
			
			numbers.insert(newpos,numbers.pop(i))				# shift the number into its new position
			moved.insert(newpos,moved.pop(i))				# shift the order of the number into its new position
			
			break								# move on to the m+1-th number to shift

i0 = numbers.index(0)								# note the position of the zero
sum_n = sum([numbers[(i*1000 + i0) % file_len] for i in range(1,4)])	# add together the positions of the 1000th, 2000th and 3000th numbers after the zero
print(sum_n)
