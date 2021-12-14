def import_data(filename):
        f = open(filename,'r')
        starting = f.readline().strip()
        data = []
        f.readline()
        line = f.readline()
        while line.strip():
        	data.append(line.strip().split(' -> '))
        	line = f.readline()
        return starting,data
        
def add_to_dict(d,e,n=1):
	if e not in d:
		d[e] = 0
	d[e] += n
	return d

def add_pairs(d,l,insertions):
	dnew = d.copy()
	for pair in d:
		if d[pair]:
			for insertion in insertions:
				if insertion[0] == pair:
					dnew[pair] -= d[pair]
					for newpair in [insertion[0][0] + insertion[1], insertion[1] + insertion[0][1]]:
						dnew = add_to_dict(dnew,newpair,d[pair])
					l = add_to_dict(l,insertion[1],d[pair])
	return dnew,l

polymer, data = import_data('14-data')

polymerD = {}
for i in range(len(polymer)-1):
	polymerD = add_to_dict(polymerD,polymer[i:i+2])
	
letters = {}
for let in polymer:
	letters = add_to_dict(letters,let)

steps = 40

for step in range(steps):
	polymerD,letters = add_pairs(polymerD,letters,data)

letmax = ['',0]
letmin = ['',1e20]
for let in letters:
	if letters[let] > letmax[1]:
		letmax[1] = letters[let]
		letmax[0] = let
	if letters[let] < letmin[1]:
		letmin[1] = letters[let]
		letmin[0] = let	
		
print(letmin,letmax,letmax[1] - letmin[1])
