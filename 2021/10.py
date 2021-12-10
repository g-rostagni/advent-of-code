def import_data(filename):
        f = open(filename,'r')
        return [line.strip() for line in f if line.strip()]
        
def matchbracket(char):
	if char == '(':
		return ')'
	elif char == '[':
		return ']'
	elif char == '{':
		return '}'
	elif char == '<':
		return '>'
	elif char == ')':
		return '('
	elif char == ']':
		return '['
	elif char == '}':
		return '{'
	elif char == '>':
		return '<'
	else:
		quit()
		

def is_corrupt(char,op):
	for i in '([{<':
		if op[-1] == i and char != matchbracket(i):
			return True
	return False
		
def score_corrupt(char):
	match char:
		case ')':
			return 3
		case ']':
			return 57
		case '}':
			return 1197
		case '>':
			return 25137
			
def score_missing(char):
	match char:	
		case ')':
			return 1
		case ']':
			return 2
		case '}':
			return 3
		case '>':
			return 4

data = import_data('10-data')
validdata = []

score1 = 0
scores2 = []

for line in data:
	valid = True
	validdata.append(line)
	op = ''
	for char in line:
		if char in '([{<':
			op += char
		elif is_corrupt(char,op):
			score1 += score_corrupt(char)
			validdata = validdata[:-1]
			valid = False
			break
		else:
			op = op[:-1]
			
	if valid:
		missing = ''
		for char in reversed(op):
			missing += matchbracket(char)
		s2 = 0
		for char in missing:
			s2 = s2*5 + score_missing(char)
		scores2.append(s2)	

print(score1)

score2 = sorted(scores2)[int(len(scores2)/2)] 
print(score2)


