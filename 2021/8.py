def import_data(filename):
        f = open(filename,'r')
        data = []
        for line in f:
        	if line.strip():
        		d1 = line.strip().split('|')
        		data.append([d1[0].split(), d1[1].split()])
        return data
        
def id1478(digit):
	match len(digit):
		case 2:
			return 1
		case 3:
			return 7
		case 4:
			return 4
		case 7:
			return 8
		case _:
			return False

def id9(digit,digits):
	def top(digits):
		for i in digits[7]:
			if i not in digits[1]:
				return i
	n = 0
	top4 = digits[4] + top(digits)
	if len(digit) == 6:
		for i in digit:
			if i not in top4:
				n += 1
		if n==1:
			return 9
	return False

def id60(digit,digits):
	if digit != digits[9] and len(digit) == 6:
		for i in digits[7]:
			if i not in digit:
				return 6
		return 0
	return False
	
def id235(digit,digits):
	if len(digit) == 5:
		n = 0
		for i in digits[7]:
			if i in digit:
				n += 1
		if n == len(digits[7]):
			return 3
		n = 0
		for i in digit:	
			if i not in digits[9]:
				return 2
		return 5
	return False
		
def idall(l):
	digits = ['' for i in range(10)]
	for digit in l[0]:	
		i = id1478(digit)
		if i:
			digits[i] = digit
	for digit in l[0]:
		i = id9(digit,digits)
		if i:
			digits[i] = digit
	for digit in l[0]:
		i = id60(digit,digits)
		if type(i) != bool:
			digits[i] = digit
	for digit in l[0]:
		i =  id235(digit,digits)
		if i:
			digits[i] = digit
	return digits

data = import_data('8-data')
for i in range(len(data)):
	for j in range(len(data[i])):
		for k in range(len(data[i][j])):
			data[i][j][k] = ''.join(sorted(data[i][j][k]))

sumdigits = [0 for i in range(10)]
tot = 0
for d in data:
	digits = idall(d)
	output = ''
	for digit in d[1]:
		for i in range(len(digits)):	
			if digit == digits[i]:
				output += str(i)
	tot += int(output)
		
print(tot)
