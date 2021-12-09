def is_infinite(dataIN):
	data = deepcopy(dataIN)
	i = 0
	acc = 0
	while True:
		try:
			instr = data[i]
		except IndexError:	
			return acc
		if len(instr) == 3:
			return True
			
		data[i].append(1)
		if instr[0] == 'acc':
			acc += instr[1]
		elif instr[0] == 'jmp':
			i += instr[1] - 1
		elif instr[0] == 'nop':
			pass
		i += 1
	
def switch_instr(instr):
	if instr == 'jmp':
		return 'nop'
	elif instr == 'nop':
		return 'jmp'
	else:
		return instr

from copy import deepcopy

f = open('8-data','r')

data = []

for line in f:
	data.append([line[0:3], int(line[4:].strip())])


i = 0
acc = 0
for i in range(len(data)):
	instr = data[i].copy()
	if instr[0] != 'acc':	
		data[i][0] = switch_instr(instr[0])
		acc = is_infinite(data)
		if type(acc) == int:
			break
		data[i][0] = switch_instr(data[i][0])

print('changed',i+1,'th instruction from',switch_instr(data[i][0]),'to:')
print(data[i])
print('acc =',acc)
