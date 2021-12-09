f = open('10-data','r')

data = [0]
for line in f:
	data.append(int(line.strip()))
data.append(max(data)+3)
data.sort()

fixed = [True for i in range(len(data))]
for i in range(1,len(data)-1):
	diff1 = data[i+1] - data[i]
	diff2 = data[i] - data[i-1]
	if diff1 != 3 and diff2 != 3:
		fixed[i] = False
	
n = 0
ntot = 1
for i in range(len(data)):
	if fixed[i]:
		match n:
			case 0:
				pass
			case 1:
				ntot *= 2
			case 2:
				ntot *= 4
			case 3:
				ntot *= 7
			case 4:
				ntot *= 13
			case _:
				print('error')
				quit()
		n = 0
	else:
		n += 1
		
print('total:',ntot)