f = open('2-data','r')

valid = 0

for line in f:
	n = line.split()
	if n:
		num = n[0].split('-')
		if bool(n[2][int(num[0])-1] == n[1][0]) ^ bool(n[2][int(num[1])-1] == n[1][0]):
			print(n,n[1][0],num)
			valid += 1
			
		
print(valid)
