def is_sum(n,nums):
	for i in range(len(nums)):
		for j in range(i,len(nums)):
			if nums[i] + nums[j] == n:
				return True
	return False

f = open('9-data','r')

data = []

for line in f:
	data.append(int(line))

for i in range(25,len(data)):
	if not is_sum(data[i],data[i-25:i]):
		break
		
invalid = data[i]
print(invalid)

for i in range(len(data)):
	j = i
	summed = 0
	contig = []
	while summed < invalid:
		summed += data[j]
		contig.append(data[j])
		j += 1
	if summed == invalid:
		break

nmin = min(contig)
nmax = max(contig)
print(nmin,nmax,nmin+nmax)