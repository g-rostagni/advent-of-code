def import_data(filename):
	f = open(filename,'r')
	data = []
	for line in f:
		if line.strip():
			data.append(line.strip())
	return data
	
def get_bracket(line,i):
	opened = 0
	for j in range(i,len(line)):
		char = line[j]
		if char == '(':
			opened += 1
		elif char == ')':
			opened -= 1
		if not opened:
			return line[i+1:j],j
	return False,False
	
def get_bracketR(line,i):
	closed = 0
	for j in range(i,-1,-1):
		char = line[j]
		if char == ')':
			closed += 1
		elif char == '(':
			closed -= 1
		if not closed:
			return line[j+1:i],j
	return False,False
	
	
def op_l2r(line):
	nums = []
	op = ''
	i = 0
	while i < len(line):
		char = line[i]
		if char in '0123456789(':
			if char == '(':
				brackets, i = get_bracket(line,i)
				nums.append(op_l2r(brackets))
			else:
				nums.append(int(char))
			if op == '+':
				nums = [nums[0] + nums[1]]
			elif op == '*':
				nums = [nums[0] * nums[1]]
		elif char in '+*':
			op = char
		i += 1
	return nums[0]
	
def add_brackets(line,pos):
	if line[pos+2] == '(':
		b,splitend = get_bracket(line,pos+2)
	else:
		splitend = pos+3
	if line[pos-2] == ')':
		b,splitstart = get_bracketR(line,pos-2)
	else:
		splitstart = pos-2
	l = line[:splitstart] + '(' + line[splitstart:splitend] + ')' + line[splitend:]
	return l
	
def generate_brackets(line):
	i = 0
	while i < len(line):
		if line[i] == '+':
			line = add_brackets(line,i)
			i += 1
		i += 1
	return line
	
data = import_data('18-data')

tot = 0
for line in data:
	tot += op_l2r(line)
print(tot)

tot = 0
for line in data:
	tot += op_l2r(generate_brackets(line))
print(tot)
