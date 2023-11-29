import re
        
def find_instruction(l):
    if re.search('^turn on', line):
        return 0
    elif re.search('^turn off', line):
        return 1
    elif re.search('^toggle',line):
        return 2

with open('6-data','r') as f:
    data = [line.strip() for line in f.readlines()]
    
lights = [[0 for i in range(1000)] for j in range(1000)]

for line in data:
    coord = re.findall('(\d+)',line)
    instr = find_instruction(line)
    for x in range(min(int(coord[0]), int(coord[2])), max(int(coord[0]), int(coord[2]))+1 ):
       for y in range(min(int(coord[1]), int(coord[3])), max(int(coord[1]), int(coord[3]))+1 ):
            if instr == 0:
                lights[x][y] += 1
            elif instr == 1 and lights[x][y]:
                lights[x][y] -= 1
            elif instr == 2:
                lights[x][y] += 2

tot = 0
for line in lights:
    for l in line:
        tot += l
        
print(tot)
