f = open('01-12-data','r')
data = []

for line in f:
	n = line.split()
	if n:
		data.append(int(n[0]))
	
windows = []

for i in range(0,len(data)-2):
	windows.append(data[i] + data[i+1] + data[i+2])

inc = 0

for i in range(1,len(windows)):
	if windows[i] > windows[i-1]:
		print(i,windows[i-1],windows[i],'increased')
		inc += 1
	else:
		print(i)
		
print(inc)
print(len(data))
print(len(windows))
