def import_data(filename):
	f = open(filename,'r')
	line = 'a'
	data1 = []
	data2 = []
	data3 = []
	while line:
		line = f.readline().strip()
		if line:
			data1.append(line)
	line = 'b'
	while line:
		line = f.readline().strip()
		if line:
			data2.append(line)
	line = 'c'
	while line:
		line = f.readline().strip()
		if line:
			data3.append(line.split(','))
	return [data1,data2,data3]

def read_ranges(data):
	allowed = []
	for line in data:
		ll = line.split(':')
		l = ll[1].strip(' ').split('or')
		r = [l[0].split('-'),l[1].split('-')]
		allowed.append([ll[0],[int(r[0][0]),int(r[0][1])], [int(r[1][0]),int(r[1][1])]])
	return allowed
		
data = import_data('16-data')


allowed = read_ranges(data[0])
tot = 0
validtickets = []
for ticket in data[2][1:]:
	invalid = False
	for n in ticket:
		err = 0
		for a in allowed:
			if not a[1][0] <= int(n) <= a[1][1] and not a[2][0] <= int(n) <= a[2][1]:
				err += 1
		if err == len(allowed):
			tot += int(n)
			invalid = True
	if not invalid:
		validtickets.append(ticket)

print('error rate:',tot)

ticketform = ['' for i in range(len(validtickets[0]))]
for k in range(len(validtickets[0])):
	for j in range(len(allowed)):	
		if allowed[j][0]:
			a = allowed[j]
			match = 0
			for i in range(len(validtickets[0])):
				err = 0
				for ticket in validtickets:
					if not a[1][0] <= int(ticket[i]) <= a[1][1] and not a[2][0] <= int(ticket[i]) <= a[2][1]:
						err += 1
				if not err:
					match += 1
					matchcol = i
			if match == 1:
				ticketform[matchcol] = a[0]
				allowed[j][0] = ''
				for ticket in validtickets:
					ticket[matchcol] = -1
				break

tot = 1
myticket = data[1][1].split(',')
	
for i in range(len(ticketform)):
	if 'departure' in ticketform[i]:
		#print(ticketform[i],myticket[i])
		tot *= int(myticket[i])
print('departures product:',tot)