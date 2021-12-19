# takes about 3min to run, can't be bothered doing actual optimisation

def import_data(filename):
	f = open(filename,'r')
	data = []
	scanners = []
	scanner = []
	for line in f:
		if not line.strip():
			scanners.append(scanner)
			scanner = []
		elif 'scanner' not in line:
			coords = line.strip().split(',')
			scanner.append(coords)
	return [[[int(c) for c in beacon] for beacon in scanner] for scanner in scanners]

def rel_coords(scanner,refbeacon):
	rel = [[coord - refcoord for coord,refcoord in zip(beacon,refbeacon)] for beacon in scanner]
	return rel

def rotations(scanner,r=-1):
	rots = []
	for i in range(3):
		match i:
			case 0:	
				j,k = 1,2
			case 1:
				j,k = 2,0
			case 2:
				j,k = 0,1
		for sign in [1,-1]:
			for [j2,k2,sign2,sign3] in [[j,k,1,1], [k,j,-1,1], [j,k,-1,-1], [k,j,1,-1]]:
				rot = []
				for b in scanner:
					rot.append([sign*b[i],sign2*b[j2],sign*sign3*b[k2]])
				rots.append(rot)
	if r < 0:
		return rots
	else:	
		return rots[r]

def find_rel_pos(scannerA,scannerB):
	found = False
	for ib in range(len(scannerB)):
		beaconB = scannerB[ib]
		scannerBrot = rotations(rel_coords(scannerB,beaconB))
		for beaconA in scannerA:
			scannerArel = rel_coords(scannerA,beaconA)
			for r in range(24):
				sB = scannerBrot[r]
				common = 0
				for bA in scannerArel:
					for bB in sB:
						if bA == bB:
							common += 1
							if common >= 12:
								return beaconA,ib,r
							break
	return False,False,False


scanners = import_data('19-data')

pos_scan = [[0,0,0] for i in range(len(scanners))]

scanner0 = scanners[0]
notabs = True
while notabs:
	notabs = False
	for i in range(1,len(scanners)):
		if not scanners[i]:
			continue
		scannerB = scanners[i]
		beacon0,ib,r = find_rel_pos(scanner0,scannerB)
		if not beacon0:
			continue
		scannerBrot = rotations(scannerB,r)
		beaconB = scannerBrot[ib]
		pos_scan[i] = [beacon0[k] - beaconB[k] for k in range(3)]
		print('found overlap in scanners 0 and',i)
		
		for b in scanners[i]:
			brot = rotations([b],r)[0]
			babs = [pos_scan[i][k] + brot[k] for k in range(3)]
			if babs not in scanner0:
				scanners[0].append(babs)
		scanners[i] = []
		notabs = True

print(len(scanners[0]))

mmax = 0
for s1 in pos_scan:
	for s2 in pos_scan:
		mdist = 0
		for i in range(3):
			mdist += abs(s1[i] - s2[i])
		mmax = max(mmax,mdist)
		
print(mmax)
