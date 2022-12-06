# define a function that returns the marker when the first word with non-repeating characters of length l is found
def find_marker(data,l):
	# defing a function that tests whether a string contains repeating characters
	def check_repeat(s):
		for char in s:
			if s.count(char) > 1:
				return True
		return False
	
	word = data[:l]					# define the starting word of length l
	for i in range(l,len(data)):			
		if check_repeat(word):
			word = word[1:] + data[i]	# shift the word by one character to the right if repeating characters are found
		else:
			return i


with open("6-data","r") as f:
	data = f.read()

# print the marker position for non-repeating words of length 4 and 14
print(find_marker(data,4))
print(find_marker(data,14))
