def import_data(filename):
        f = open(filename,'r')
        poly = {}
        letters = {}
        line = f.readline().strip()
        for i in range(len(line)-1):
        	poly = add_to_dict(poly,line[i:i+2])
        	letters = add_to_dict(letters,line[i])
        letters = add_to_dict(letters,line[-1])      
        
        ins = {}
        f.readline()
        line = f.readline()
        while line.strip():
        	l = line.strip().split(' -> ')
        	ins[l[0]] = l[1]
        	line = f.readline()
        return poly, letters, ins
        
def add_to_dict(d,e,n=1):
	if e not in d:
		d[e] = 0
	d[e] += n
	return d

def add_pairs(d,l,i):
	dnew = d.copy()
	for pair in d:
		if d[pair] and pair in i:
			dnew[pair] -= d[pair]
			for newpair in [pair[0] + i[pair], i[pair] + pair[1]]:
				dnew = add_to_dict(dnew,newpair,d[pair])
			l = add_to_dict(l,i[pair],d[pair])
	return dnew,l

polymer, letters, insertions = import_data('14-data')

steps = 40

for step in range(steps):
	polymer,letters = add_pairs(polymer,letters,insertions)

letmax = 0
letmin = 1e20
for let in letters:
	letmax = max(letmax,letters[let])
	letmin = min(letmin,letters[let])
		
print(letmax - letmin)
