import math

f = open('5-data','r')

seats = []

for line in f:
	if line:
		seats.append(line.strip())		
		
IDmax = 0
IDs = set()
		
for seat in seats:
	rowmin = 0
	rowmax = 127
	colmin = 0
	colmax = 7
	for char in seat:
		if char == 'F':
			rowmax = math.floor((rowmin+rowmax)/2)
		elif char == 'B':
			rowmin = math.ceil((rowmin+rowmax)/2)
		elif char == 'L':
			colmax = math.floor((colmin+colmax)/2)
		elif char == 'R':
			colmin = math.ceil((colmin+colmax)/2)
	ID = rowmin * 8 + colmin
	IDs.add(ID)
	IDmax = max(IDmax, ID)
	print(seat,rowmin,colmin)

for i in range(IDmax):
	if i not in IDs:
		if i-1 in IDs and i+1 in IDs:
			print(i)