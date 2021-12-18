def import_data(filename):
	f = open(filename,'r')
	data = []
	for line in f:
		l = []
		for char in line.strip():
			try:
				l.append(int(char))
			except ValueError:
				l.append(char)
		data.append(l)
	return data
	
def add_n(n1,n2):
	added = ['['] + n1 + [','] + n2 + [']']
	return added
	
def explode_all(line):
	def explode(line,i):
		def find_left_n(line,pos):
			i = pos-4
			while type(line[i]) != int:
				i -= 1
				if i == -1:
					return False
			return i
		def find_right_n(line,pos):
			i = pos+1
			while type(line[i]) != int:
				i += 1
				if i == len(line):
					return False
			return i
		j = find_left_n(line,i)
		if j:
			line[j] += line[i-3]
		j = find_right_n(line,i)
		if j:
			line[j] += line[i-1]
		return line[:i-4] + [0] + line[i+1:]
	op = 0
	i = 0
	while i < len(line):
		char = line[i]
		if char == '[':
			op += 1
		elif char == ']':
			if op >= 5:
				return explode(line,i),True
			op -= 1
		i += 1
	return line,False
	
def split_all(line):
	def split_n(line,i):
		newpair = ['[', int(char/2), ',', int(char/2+0.5), ']']
		return line[:i] + newpair + line[i+1:]
	i = 0
	while i < len(line):
		char = line[i]
		if type(char) == int and char >= 10:
			return split_n(line,i),True
		i += 1
	return line,False
	
def reduce_n(added):
	doneexplode = True
	donesplit = True
	while doneexplode or donesplit:
		added,doneexplode = explode_all(added)
		if doneexplode:
			continue
		added,donesplit = split_all(added)
	return added
	
def get_score(line):
	i = 0
	while i < len(line):
		if line[i] == ']':
			line = line[:i-4] + [3*line[i-3] + 2*line[i-1]] + line[i+1:]
			i = 0
			continue
		i += 1
	return line[0]

data = import_data('18-data')

magmax = 0
for n1 in data:
	for n2 in data:
		if n2 == n1:
			continue
		added = reduce_n(add_n(n1,n2))
		magmax = max(magmax,get_score(added))

print(magmax)
