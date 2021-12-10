f = open('01-12-data','r')
data = []

for line in f:
	n = line.split()
	if n:
		data.append(int(n[0]))
	
inc = 0

for i in range(1,len(data)):
	if data[i] > data[i-1]:
		print(i,data[i-1],data[i],'increased')
		inc += 1
	else:
		print(i)
		
print(inc)
