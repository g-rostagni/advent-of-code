# i had no idea how to solve this. i did the first part by hand and bruteforced the second. takes about one hour to run.
  
def get_cost(let):
	match let:
		case 'A':
			return 1
		case 'B':
			return 10
		case 'C':
			return 100
		case 'D':
			return 1000
	
def move_amphipod(origin,dest,cave):
	cavenew = copy.deepcopy(cave)
	let = cave[origin[0]][origin[1]]
	cavenew[origin[0]][origin[1]] = ' '
	cavenew[dest[0]][dest[1]] = let
	pathlen = abs(dest[0] - origin[0]) + abs(dest[1] - origin[1])
	cost = pathlen*get_cost(let)
	return cavenew,cost
	
def is_move_valid(origin,dest,cave):
	# if going over another amphipod
	if origin[0] == 0:
		for i in range(origin[0]+1,dest[0]+1):
			if cave[i][dest[1]] != ' ':
				return False
	else:
		for i in range(dest[0],origin[0]):
			if cave[i][origin[1]] != ' ':
				return False
	if dest[1] > origin[1]:
		for i in range(origin[1]+1,dest[1]+1):
			if cave[0][i] != ' ':
				return False
	else:
		for i in range(dest[1],origin[1]):
			if cave[0][i] != ' ':
				return False
	# if entering the wrong cave
	if dest[0] != 0:
		if cave[origin[0]][origin[1]] != parked[dest[1]]:
			return False
		# if not going to the bottom of a cave or entering a busy cave
		if dest[0] < 4:
			if cave[dest[0]+1][dest[1]] == ' ':
				return False
			else:
				for d in range(dest[0]+1,5):
					if cave[d][dest[1]] != parked[dest[1]]:
						return False
	return True
	

def all_parked(cave):
	for i in parked:
		for j in range(1,5):
			if cave[j][i] != parked[i]:
				return False
	return True
	
def get_origins(cave):
	origins = []
	for i in range(len(cave)):
		for j in range(len(cave[0])):
			if cave[i][j].isalpha():
				if i > 0 and cave[i][j] == parked[j]:
					if i == 4:
						continue
					else:
						notparked = False
						for d in range(i+1,5):
							if cave[d][j] != parked[j]:
								notparked = True
								break
						if not notparked:
							continue	
				origins.append([i,j])
	return origins
	
def get_dests(origin,cave):
	dests = []
	if origin[0] == 0:
		dst = [[1,2],[2,2],[3,2],[4,2],[1,4],[2,4],[3,4],[4,4],[1,6],[2,6],[3,6],[4,6],[1,8],[2,8],[3,8],[4,8]]
	else:
		dst = [[0,0],[0,1],[0,3],[0,5],[0,7],[0,9],[0,10]]
	for d in dst:
		if is_move_valid(origin,d,cave):
			dests.append(d)
	return dests
			
def get_moves(cave,cost):
	global costGLB
	if cost >= costGLB:
		return
	if all_parked(cave):
		print('new minimal cost found:',cost)
		costGLB = cost
		return
	for origin in get_origins(cave):
		for dest in get_dests(origin,cave):			
			cavetemp,costt = move_amphipod(origin,dest,cave)
			get_moves(cavetemp,cost+costt)
			
def get_moves0(cave,cost):
	global costGLB
	if all_parked(cave):
		print('new solution found:',cost)
		costGLB = min(costGLB,cost)
		return
	if cost >= costGLB:
		return
	for origin in get_origins(cave):
		for dest in get_dests(origin,cave):
			print(origin,dest)		
			cavetemp,costt = move_amphipod(origin,dest,cave)
			get_moves(cavetemp,cost+costt)
	
import copy

costGLB = 100000

print('starting cost:',costGLB)
						
parked = {2:'A', 4:'B', 6:'C', 8:'D'}

startcave = [[' ' for i in range(11)] for j in range(5)]

#               0  1  2   3  4   5  6   7  8   9 10
startcave[1]= ['','','A','','D','','B','','D','','']
startcave[2]= ['','','D','','C','','B','','A','','']
startcave[3]= ['','','D','','B','','A','','C','','']
startcave[4]= ['','','B','','C','','A','','C','','']

cave = copy.deepcopy(startcave)

get_moves0(cave,0)
	
print('all done! minimal cost:',costGLB)
