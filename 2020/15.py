data = [0,3,1,6,7,5]

turns = 30000000

spoken = {}
for i in range(len(data)):
	spoken[data[i]] = [i]
	lastn = data[i]
	
first = True
for i in range(len(data),turns):
	if first:
		newn = 0
	else:
		newn = spoken[lastn][-1] - spoken[lastn][-2]
	if newn in spoken:
		spoken[newn].append(i)
		first = False
	else:
		spoken[newn] = [i]
		first = True
	lastn = newn
	
print(lastn)
