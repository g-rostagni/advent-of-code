# define a function that returns the marker when the first word with non-repeating characters of length l is found
def find_marker(data,l):
	for i in range(l,len(data)):		
		# convert the last l characters from the i-th position from the buffer into a set
		# if the length of the set is exactly l then there are no repeated characters	
		if len(set(data[i-l:i])) == l:
			return i
	return -1

with open("6-data","r") as f:
	data = f.read()

# print the marker position for non-repeating words of length 4 and 14
print(find_marker(data,4))
print(find_marker(data,14))
