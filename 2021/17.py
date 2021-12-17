def update1step(pos,v):
	pos[0] += v[0]
	pos[1] += v[1]
	if v[0] > 0:
		v[0] -= 1
	elif v[0] < 0:
		v[0] += 1
	v[1] -= 1
	return pos,v

# target area: x=253..280, y=-73..-46
target = [[253,280],[-73,-46]]

hits = []
for vy in range(target[1][0],200):
	hit = []
	for vx in range(0,target[0][1]+1):
		pos = [0,0]
		v = [vx,vy]
		ymax = 0
		while pos[1] >= target[1][0] and pos[0] <= target[0][1]:
			pos,v = update1step(pos,v)
			ymax = max(ymax,pos[1])
			if target[0][0] <= pos[0] <= target[0][1] and target[1][0] <= pos[1] <= target[1][1]:
				print('hit target with v0 =',[vx,vy],'; ymax =',ymax)
				hits.append(ymax)
				break

ymaxmax = max(hits)	
print('max altitude:',ymaxmax)
print('number of hits:',len(hits))
