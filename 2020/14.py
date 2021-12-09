def import_data(filename):
	f = open(filename,'r')
	data = []
	d = []
	for line in f:
		if 'mask' in line:
			if d:
				data.append(d)
			d = [line[7:].strip()]
		else:
			d2 = line.strip().split('=')
			m = re.search('mem\[(.+?)\]',d2[0])
			d.append([int(m.group(1)),int(d2[1])])
	data.append(d)
	return data
	
import re

data = import_data('14-data')
mem = {}

i = 0
while i < len(data):
	for m in data[i][0]:
		if m == 'X':
			add0 = data[i][0].replace('X','N',1)
			add1 = data[i][0].replace('X','1',1)
			data.insert(i+1,[add1] + data[i][1:])
			data[i] = [add0] + data[i][1:]
	i += 1
			
for line in data:
	for d in line[1:]:
		add = ''
		val = '{0:b}'.format(d[0])
		val = ('0' * (36-len(val))) + val
		for m,v in zip(line[0],val):
			match m:
				case '1':
					add += '1'
				case 'N':
					add += '0'
				case _:
					add += v
		mem[int(add,2)] = int(d[1])

tot = 0
for i in mem:
	tot += mem[i]
	
print(tot)