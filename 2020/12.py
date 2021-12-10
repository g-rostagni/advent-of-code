def import_data(filename):
        f = open(filename,'r')
        data = [[line[0],int(line[1:].strip())] for line in f if line.strip()]
        return data

def rotate_wayp(pos,heading):
	n = pos[0] * math.cos(math.radians(heading)) - pos[1] * math.sin(math.radians(heading))
	e = pos[0] * math.sin(math.radians(heading)) + pos[1] * math.cos(math.radians(heading))
	return [n,e]

import math
    
data = import_data('12-data')

ship_pos = [0,0]
wayp_pos = [1,10]
for line in data:
        match line[0]:
                case 'N':
                	wayp_pos[0] += line[1]
                case 'S':
                	wayp_pos[0] -= line[1]
                case 'E':
                	wayp_pos[1] += line[1]
                case 'W':
                	wayp_pos[1] -= line[1]
                case 'L':
                	wayp_pos = rotate_wayp(wayp_pos,-line[1])
                case 'R':
                	wayp_pos = rotate_wayp(wayp_pos,line[1])
                case 'F':
                	ship_pos[0] += wayp_pos[0] * line[1] 
                	ship_pos[1] += wayp_pos[1] * line[1]
                case _:
                	print('error')
                	quit()
        print(ship_pos,wayp_pos)

dist = abs(ship_pos[0]) + abs(ship_pos[1])
print(ship_pos,dist)
