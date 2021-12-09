def import_data(filename):
	f = open(filename,'r')
	f.readline()
	b = f.readline().strip().split(',')
	return b
	
def match1(startF,increF,lF):
	i = startF
	matched = 0
	m = []
	while matched < 2:
		if not (i + lF[0]) % lF[1]:
			m.append(i)
			matched += 1
		i += increF
	return m[0],m[1]-m[0]

busses = import_data('13-data')
data = []

for i in range(len(busses)):
	if busses[i] != 'x':
		data.append([i,int(busses[i])])

start = 0
increment = data[0][1]
for l in data:
	start,increment = match1(start,increment,l)

print(start)