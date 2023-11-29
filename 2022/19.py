def ceil(x):
	if int(x) > x:
		return int(x) + 1
	else:
		return int(x)


blueprints = []
with open("19-data","r") as f:
	for line in f.readlines():
		l = line.strip().split(" ")
		blueprints.append([int(l[6]), int(l[12]), [int(l[18]), int(l[21])], [int(l[27]), int(l[30])]])
		
blueprint = [2, 3, [3,8], [3,12]]

# let time loop
# if you have enough resources to build a geode robot, build one
# if you have enough resources to build a obsidian robot, build one
# build clay robots if we have enough
# don't bother with ore robots
# if we predict we will have enough resources to build a geode/obsidian robot, save them until then

# need to see how much time it takes us to get x obsidian/clay
# if we can get more than enough ore in that time, then we can spend it

resources = [[0,0,0,0]]
robots = [[1,0,0,0]]
for minute in range(24):
	resourcesnew = []
	robotsnew = []
	for res,rob in zip(resources,robots):
		resnew = []
		robnew = []
			
		# build geode collecting robot
		if res[0] >= blueprint[3][0] and res[2] >= blueprint[3][1]:
			robnew.append([rob[0], rob[1], rob[2], rob[3]+1])
			resnew.append([res[0]-blueprint[3][0], res[1], res[2]-blueprint[3][1], res[3]])
			
			
		if res[0] >= blueprint[2][0] and res[1] >= blueprint[2][1]:
			robnew.append([rob[0], rob[1], rob[2]+1, rob[3]])
			resnew.append([res[0]-blueprint[2][0], res[1]-blueprint[2][1], res[2], res[3]])
			
			
		if res[0] >= blueprint[1]:
			robnew.append([rob[0], rob[1]+1, rob[2], rob[3]])
			resnew.append([res[0]-blueprint[1], res[1], res[2], res[3]])
	
		if False and res[0] >= blueprint[0]:
			robnew.append([rob[0]+1, rob[1], rob[2], rob[3]])
			resnew.append([res[0]-blueprint[0], res[1], res[2], res[3]])
			
		robnew.append(rob)
		resnew.append(res)
		
		for i in range(len(resnew)):
			for j in range(4):
				resnew[i][j] += rob[j]

		resourcesnew += [[a for a in b] for b in resnew]
		robotsnew += [[a for a in b] for b in robnew]
	
	resources = [[a for a in b] for b in resourcesnew]
	robots = [[a for a in b] for b in robotsnew]
	
	print(minute,len(resources))
	
gmax = 0
for r in resources:
	if r[3] > gmax:
		gmax = r[3]
print(gmax)
	
	
	
